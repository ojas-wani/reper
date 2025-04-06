import arxiv
import numpy as np
from sentence_transformers import SentenceTransformer


class ArxivSearch:
    def __init__(self):
        self.client = arxiv.Client()
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')

    def find_papers_by_str(self, query, start_year, end_year, N=5):
        try:
            search = arxiv.Search(
                query=f"abs:{query}",
                max_results=N,
                sort_by=arxiv.SortCriterion.Relevance
            )
            results = list(self.client.results(search))
            filtered_results = self._filter_by_date(
                results, start_year, end_year)
            return "\n\n".join([self._format_result(r) for r in filtered_results])
        except Exception as e:
            print(f"arXiv search failed: {e}")
            return ""

    def _filter_by_date(self, results, start_year, end_year):
        filtered_results = []
        for result in results:
            published_year = result.published.year
            if start_year <= published_year <= end_year:
                filtered_results.append(result)
        return filtered_results

    def _format_result(self, result):
        return (
            f"Title: {result.title}\n"
            f"ID: {result.get_short_id()}\n"
            f"Published: {result.published.date()}\n"
            f"Summary: {result.summary}\n"
            f"Link: {result.entry_id}"
        )

    def rank_papers(self, papers, research_topic, top_n=10):
        if not papers:
            return []

        try:
            topic_embed = self.embedder.encode(research_topic)
            summaries = [p.split("Summary: ")[1].split("\n")[0]
                         for p in papers if "Summary: " in p]
            paper_embeds = self.embedder.encode(summaries)
            scores = np.dot(paper_embeds, topic_embed)
            return [papers[i] for i in np.argsort(scores)[-top_n:]]
        except Exception as e:
            print(f"Ranking failed: {e}")
            return papers[:top_n]
