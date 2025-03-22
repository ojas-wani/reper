import arxiv
import time


class ArxivSearch:
    def __init__(self):
        self.client = arxiv.Client()

    def find_papers_by_str(self, query, N=5):
        search = arxiv.Search(
            query=f"abs:{query}",
            max_results=N,
            sort_by=arxiv.SortCriterion.Relevance
        )

        paper_sums = []
        for result in self.client.results(search):
            paperid = result.pdf_url.split("/")[-1]
            pubdate = str(result.published).split(" ")[0]
            summary = (
                f"Title: {result.title}\n"
                f"Summary: {result.summary}\n"
                f"Publication Date: {pubdate}\n"
                f"Categories: {' '.join(result.categories)}\n"
                f"arXiv ID: {paperid}\n"
            )
            paper_sums.append(summary)
            time.sleep(1)

        return "\n\n".join(paper_sums)
