# Systematic Literature Review: Tools for the literature review. Similar to automated systematic review.
*Generated on 2025-03-23*

## Abstract
## Abstract

This literature review investigates the landscape of tools designed to automate and enhance the systematic literature review (SLR) process. With the exponential growth of scientific publications, traditional manual methods are increasingly time-consuming and prone to bias. This review systematically examines tools across several key sub-topics: AI-powered literature screening, automated data extraction, citation network analysis, bias detection, machine learning for topic modeling, systematic review automation platforms, and natural language processing (NLP) for text summarization. The methodology involved a comprehensive search of academic databases (e.g., Scopus, Web of Science, PubMed) using pre-defined keywords and inclusion/exclusion criteria to identify relevant studies evaluating or applying these tools. Key findings reveal that while AI-powered screening tools can significantly reduce the workload in identifying relevant articles, their performance varies depending on the algorithm and the specificity of the research question. Automated data extraction tools demonstrate potential for efficiency gains, but often require substantial manual refinement to ensure accuracy. Citation network analysis offers valuable insights into the evolution of research fields and the identification of influential publications. Emerging techniques in bias detection show promise in identifying potential biases within reviews, but require further validation. Machine learning for topic modeling facilitates the identification of key themes and research trends within large corpora of text. Systematic review automation platforms integrate multiple functionalities, streamlining the review process, but their usability and customizability remain key challenges. Finally, NLP-based text summarization tools offer potential for accelerating the synthesis of information, but concerns remain regarding the preservation of nuanced meaning and contextual understanding. This review highlights the potential of these tools to enhance the efficiency, transparency, and rigor of SLRs. However, it also identifies critical research gaps, including the need for standardized evaluation metrics, improved algorithm transparency, and greater attention to the integration of qualitative evidence. The implications of this review suggest that the effective adoption of these tools requires a critical understanding of their strengths and limitations, alongside the development of robust training programs for researchers. Ultimately, these advancements pave the way for more timely, comprehensive, and reliable evidence syntheses, informing both research and practice.


## Thematic Analysis

### AI-powered literature screening
## Critical Analysis of AI-Powered Literature Screening Tools

This report analyzes three papers focusing on the application of Artificial Intelligence (AI) to literature screening, a crucial and time-consuming step in systematic literature reviews (SLRs). The papers explore different approaches, ranging from Large Language Model (LLM)-based systems to web-based applications, and address the critical need for standardized datasets. This analysis will compare the methodologies, major findings, and limitations of each study, and identify potential research gaps.

**1. Streamlining Systematic Reviews: A Novel Application of Large Language Models (arxiv_id: 2412.15247v1)**

*   **Key Methodologies:** This paper presents an in-house system leveraging LLMs for both title/abstract and full-text screening. For title/abstract screening, the system utilizes prompt engineering. Full-text screening employs Retrieval-Augmented Generation (RAG). The system was evaluated using a completed SR on Vitamin D and falls, comprising 14,439 articles. The performance was compared against traditional methods and the commercial tool Rayyan.
*   **Major Findings:** The LLM-based system achieved impressive results: a 99.5% article exclusion rate (AER), 99.6% specificity, 0% false negative rate (FNR), and 100% negative predictive value (NPV). This significantly reduced the manual screening time by 95.5%, requiring manual review of only 78 articles.  The LLM-based system outperformed Rayyan, particularly in full-text screening, a phase often lacking automation.
*   **Limitations:** The study focuses on a single systematic review. While the results are promising, the generalizability to other topics and research areas needs further investigation. The reliance on prompt engineering raises concerns about the robustness and transferability of the prompts across different datasets and research questions. The in-house nature of the system and the lack of publicly available code limit reproducibility and wider adoption. It is unclear what specific LLM model was used and what hardware configuration was utilized, hindering comparison and replication efforts.
*   **Relationships to other studies:** This study directly compares its performance against Rayyan, a widely used commercial tool. This provides a concrete benchmark and highlights the potential advantages of LLM-based approaches.  The focus on automating *both* title/abstract and full-text screening distinguishes it from many other studies that primarily concentrate on the initial screening phase. The use of RAG for full-text screening aligns with the broader trend of leveraging LLMs with external knowledge bases for improved performance.

**2. CRUISE-Screening: Living Literature Reviews Toolbox (arxiv_id: 2309.01684v1)**

*   **Key Methodologies:** This paper introduces CRUISE-Screening, a web-based application designed for conducting living literature reviews. It connects to multiple search engines via APIs for continuous updating of search results.  The application utilizes text classification and question answering models to facilitate the screening process.
*   **Major Findings:** CRUISE-Screening offers a platform for researchers to conduct continuously updated literature reviews.  It aims to enhance efficiency and effectiveness through automation techniques. The application is open-source and a demo is available, promoting accessibility and collaboration.
*   **Limitations:** The paper lacks quantitative performance evaluations. While it describes the functionality of the tool, it does not provide empirical evidence of its effectiveness in reducing screening time or improving accuracy compared to traditional methods.  The specific text classification and question answering models used are not detailed, making it difficult to assess their capabilities and limitations.  The appendix mentions limitations of the tool, but these are not explicitly discussed in the main body of the paper, reducing their impact on the reader.
*   **Relationships to other studies:** This paper takes a different approach by focusing on a web-based platform rather than a specific algorithm or model.  It aligns with the growing interest in "living" literature reviews, which require continuous updating and screening of new publications.  The open-source nature of the project encourages community involvement and further development.

**3. CSMeD: Bridging the Dataset Gap in Automated Citation Screening for Systematic Literature Reviews (arxiv_id: 2311.12474v1)**

*   **Key Methodologies:** This paper addresses the lack of standardized evaluation datasets for automated citation screening. It analyzes existing datasets and identifies limitations such as small size, data leakage, and limited applicability.  The authors introduce CSMeD, a meta-dataset consolidating nine publicly released collections, providing unified access to 325 SLRs.  They also introduce CSMeD-FT, a new dataset specifically designed for evaluating full-text screening.  Experiments are conducted to establish baselines on the new datasets.
*   **Major Findings:** The paper highlights the critical need for standardized and comprehensive evaluation datasets in the field of automated citation screening. CSMeD and CSMeD-FT offer valuable resources for training and evaluating models, addressing a significant bottleneck in the development and comparison of different approaches.  The experiments conducted demonstrate the utility of the datasets and provide baseline performance metrics.
*   **Limitations:** While the paper introduces valuable datasets, it does not propose a specific screening algorithm or system.  The baselines established are likely to be surpassed as more advanced models are developed and trained on these datasets.  The focus is primarily on medicine and computer science, limiting the generalizability to other disciplines.
*   **Relationships to other studies:** This paper provides the necessary infrastructure for evaluating systems like the one presented in (arxiv_id: 2412.15247v1) and for developing models that could be integrated into platforms like CRUISE-Screening (arxiv_id: 2309.01684v1). It directly addresses a weakness in the field by providing standardized datasets, enabling more rigorous comparisons and advancements.

**Comparative Analysis and Research Gaps:**

These three papers represent different but complementary approaches to AI-powered literature screening. (arxiv_id: 2412.15247v1) demonstrates the potential of LLMs to significantly reduce screening time while maintaining high accuracy. However, its limited scope and lack of generalizability are limitations. (arxiv_id: 2309.01684v1) provides a platform for conducting living literature reviews, but lacks empirical validation. (arxiv_id: 2311.12474v1) addresses a critical gap by providing standardized datasets for training and evaluation.

Several research gaps emerge from this analysis:

*   **Generalizability of LLM-based systems:** Further research is needed to assess the performance of LLM-based screening systems across different topics, research areas, and systematic review methodologies.  Studies should investigate the robustness and transferability of prompts and fine-tuning strategies.
*   **Empirical validation of literature review platforms:**  Platforms like CRUISE-Screening require rigorous empirical evaluation to demonstrate their effectiveness in improving the efficiency and accuracy of literature reviews.  Controlled experiments comparing platform-assisted reviews with traditional methods are needed.
*   **Development of more sophisticated evaluation metrics:** Beyond AER, specificity, FNR, and NPV, more nuanced metrics are needed to capture the qualitative aspects of literature screening, such as the ability to identify relevant but less obvious studies.
*   **Integration of AI with existing systematic review workflows:** Research should focus on seamlessly integrating AI-powered tools into existing systematic review workflows, addressing practical challenges such as data import/export, collaboration, and audit trails.
*   **Bias detection and mitigation:**  AI models can perpetuate and amplify biases present in the training data.  Research is needed to develop methods for detecting and mitigating bias in AI-powered literature screening tools.
*   **Explainability and transparency:**  Understanding *why* an AI model makes a particular screening decision is crucial for building trust and ensuring accountability.  Research should focus on developing explainable AI (XAI) techniques for literature screening.

**Conclusion:**

The papers analyzed demonstrate the transformative potential of AI in streamlining the literature screening process. LLMs, web-based platforms, and standardized datasets are all valuable tools for researchers conducting systematic reviews. However, significant research gaps remain, particularly in the areas of generalizability, empirical validation, bias detection, and explainability. Addressing these gaps will be crucial for realizing the full potential of AI-powered literature screening and improving the efficiency and quality of evidence-based research.

### Automated data extraction tools
## Critical Analysis of Automated Data Extraction Tools: A Systematic Review

This report presents a critical analysis of three recent studies focusing on automated data extraction tools, spanning diverse applications from deep learning pipelines to materials science and medical record digitization. The analysis will examine the methodologies employed, major findings, limitations, and inter-study relationships, ultimately identifying potential research gaps and future directions.

**1. Key Methodologies and Major Findings:**

*   **"Automated data processing and feature engineering for deep learning and big data applications: a survey" (arxiv:2403.11395v2):** This paper presents a comprehensive review of existing techniques for automating data processing within deep learning pipelines. The methodology involves a thorough survey of literature focusing on automated data preprocessing (cleaning, labeling, imputation, encoding), data augmentation (including generative AI), and feature engineering (extraction, construction, selection). The major finding is the identification and categorization of various approaches within each of these automated data processing stages, highlighting the progress towards end-to-end AutoML systems capable of handling raw data for big data tasks.

*   **"Automated split Hopkinson pressure bar for high throughput dynamic experiments" (arxiv:2502.02729v1):** This study focuses on the development of a fully automated Split Hopkinson Pressure Bar (SHPB) system for high-throughput dynamic compression experiments. The methodology centers on the design and integration of electromechanical systems for automated sample handling, striker launch, and data acquisition. A key component is the development of an automated data analysis tool for post-processing the experimental data, including stress-strain curve extraction. The major finding is the successful implementation of an automated SHPB system capable of performing dynamic compression experiments at a rate of 60 samples per hour, validated through experiments on Copper 101 and 3D-printed resin samples. The automated data analysis tool's efficiency was confirmed through comparison with existing methods.

*   **"MedPromptExtract (Medical Data Extraction Tool): Anonymization and Hi-fidelity Automated data extraction using NLP and prompt engineering" (arxiv:2405.02664v3):** This paper introduces MedPromptExtract, an automated tool for extracting data from medical discharge summaries (DS) while maintaining patient confidentiality. The methodology involves a multi-stage pipeline: 1) Anonymization using a pre-existing semi-supervised learning tool (EIGEN); 2) NLP-based extraction of structured data; and 3) Prompt engineering and Large Language Model (LLM) utilization for extracting custom clinical information from free text. The LLM used was Gemini Pro. The extracted data was validated against clinician annotations. The major findings include the successful anonymization of DS, high accuracy in extracting structured data via NLP (100%), and promising results from the LLM pipeline, with seven out of twelve features achieving AUCs above 0.9 when compared to clinician annotations.

**2. Limitations:**

*   **"Automated data processing and feature engineering for deep learning and big data applications: a survey":** As a survey paper, the primary limitation is the potential for bias in the selection and interpretation of reviewed literature. The paper could benefit from a more critical comparison of the surveyed techniques, including their computational costs, scalability, and applicability to different types of data and tasks. Furthermore, the survey lacks empirical validation of the discussed techniques, relying solely on reported results from individual studies.

*   **"Automated split Hopkinson pressure bar for high throughput dynamic experiments":** The study's limitation lies in the scope of materials tested. While the system was validated with Copper 101 and 3D-printed resin, its performance and reliability with a wider range of materials remain unexplored. Furthermore, the paper provides limited detail on the robustness and error handling capabilities of the automated data analysis tool. The long-term reliability and maintenance requirements of the automated SHPB system are also not addressed.

*   **"MedPromptExtract (Medical Data Extraction Tool): Anonymization and Hi-fidelity Automated data extraction using NLP and prompt engineering":** The study is limited by its reliance on a single dataset (discharge summaries from one hospital). The generalizability of the MedPromptExtract tool to other medical record formats and patient populations is uncertain.  The choice of Gemini Pro as the LLM might limit reproducibility due to potential API changes and evolving model versions. The study could benefit from a more detailed analysis of the types of errors made by the LLM pipeline and a comparison with other LLMs. The computational cost and scalability of the LLM-based extraction process are also not thoroughly discussed.

**3. Relationships Between Studies:**

While seemingly disparate, these studies share a common thread: the automation of data extraction and processing to improve efficiency and scalability. The survey paper (arxiv:2403.11395v2) provides a broad overview of techniques relevant to both the SHPB automation (arxiv:2502.02729v1) and the medical data extraction tool (arxiv:2405.02664v3). For example, feature engineering techniques discussed in the survey could potentially be applied to the data generated by the automated SHPB system to identify material properties or predict material behavior. Similarly, data cleaning and imputation techniques from the survey could be used to improve the quality of the medical discharge summaries before processing by MedPromptExtract.

The MedPromptExtract study (arxiv:2405.02664v3) leverages NLP and LLMs, representing a specific application of automated feature extraction from unstructured text, a topic covered in the broader survey. The SHPB automation (arxiv:2502.02729v1) focuses on automating data acquisition and pre-processing for a specific experimental setup, demonstrating the potential for automation in scientific research.

**4. Research Gaps and Future Directions:**

Several research gaps emerge from this analysis:

*   **Robustness and Generalizability:**  A significant gap exists in the evaluation of the robustness and generalizability of automated data extraction tools across different datasets, domains, and experimental conditions. Future research should focus on developing techniques that are less sensitive to variations in data quality, format, and content.

*   **Explainability and Interpretability:** As automated data extraction tools become more complex, particularly those relying on LLMs, the need for explainability and interpretability becomes crucial. Future research should explore methods for understanding the decision-making processes of these tools and identifying potential biases or errors.

*   **Integration of Automated Data Extraction with Downstream Tasks:**  More research is needed on the seamless integration of automated data extraction tools with downstream tasks, such as machine learning model training, data analysis, and decision-making. This includes developing standardized data formats and APIs that facilitate data exchange between different tools and systems.

*   **Cost-Benefit Analysis:** A comprehensive cost-benefit analysis of automated data extraction tools is lacking. Future research should quantify the economic benefits of automation, including reduced labor costs, improved data quality, and faster turnaround times, while also considering the costs of development, implementation, and maintenance.

*   **Ethical Considerations:** As automated data extraction tools are increasingly used in sensitive domains, such as healthcare and finance, it is crucial to address the ethical implications of these technologies, including privacy, security, and fairness. Future research should focus on developing guidelines and best practices for the responsible use of automated data extraction tools.

In conclusion, the reviewed studies highlight the increasing importance of automated data extraction tools across various domains. While significant progress has been made, several research gaps remain, particularly in the areas of robustness, generalizability, explainability, integration, and ethical considerations. Addressing these gaps will be crucial for realizing the full potential of automated data extraction tools and ensuring their responsible and effective use.

### Citation network analysis software
## Critical Analysis of Citation Network Analysis Software and Applications

This report analyzes three papers employing citation network analysis, focusing on methodologies, findings, limitations, and inter-study relationships. The papers cover diverse applications, ranging from legal precedent analysis to characterizing health informatics journals and identifying seminal works in scientometrics.  While each paper utilizes citation network analysis, they differ significantly in their focus, methodology, and the types of inferences drawn.

**Paper 1: Generative Dynamics of Supreme Court Citations: Analysis with a New Statistical Network Model (Zhang et al., 2021)**

*   **Key Methodologies:** This paper introduces a citation exponential random graph model (CERGM) for analyzing citations between US Supreme Court opinions. The CERGM operates at the dyadic level, analyzing individual citations rather than aggregating them to the case level. This allows for the incorporation of both case characteristics (exogenous covariates) and complex network dependencies (reciprocity, transitivity, popularity) into the analysis of citation formation. The authors also provide user-friendly software to implement the CERGM.
*   **Major Findings:** The study reveals significant evidence for dependence processes in Supreme Court citation patterns, including reciprocity (cases citing each other), transitivity (if A cites B and B cites C, then A is more likely to cite C), and popularity (highly cited cases are more likely to be cited).  These network dependence effects are found to be as significant as the effects of exogenous covariates, suggesting that models of legal precedent should consider both case characteristics and the structure of past citations.
*   **Limitations:** The model, while sophisticated, is still a simplification of the complex dynamics influencing legal citation.  The choice of covariates included in the model can significantly affect the results.  Furthermore, the analysis is limited to Supreme Court cases between 1950 and 2015, potentially overlooking earlier or later trends. The inherent assumption is that citation equals influence, which may not always hold true. Citations can be negative or perfunctory.
*   **Relationships to other studies:** This study builds upon existing work on Supreme Court citations by addressing the limitations of aggregating citations and treating them as independent events.  It leverages the power of exponential random graph models, commonly used in social network analysis, to provide a more nuanced understanding of citation dynamics in the legal domain.

**Paper 2: Characterizing health informatics journals by subject-level dependencies: a citation network analysis (Liang et al., 2018)**

*   **Key Methodologies:** This study analyzes citation statistics from health informatics journals using data extracted from CrossRef. It focuses on characterizing journals based on their citation patterns to and from different fields, including computer science, medicine/clinical medicine, and other health informatics journals. The analysis involves comparing in-citations, out-citations, and self-citations among different journals.
*   **Major Findings:** The study reveals differences in citation patterns among health informatics journals. For example, JAMIA has more in-citations than JMIR, while JMIR has a higher number of out-citations and self-citations. JMS cites more articles from computer science journals compared to other health informatics journals. These findings provide insights into the disciplinary connections and knowledge flow patterns of different journals within the health informatics field.
*   **Limitations:** The study is limited by its reliance on CrossRef data and the specific set of journals included in the analysis.  The categorization of citations into broad subject areas (computer science, medicine, etc.) may oversimplify the complex relationships between disciplines.  The study does not delve into the content of the cited articles, potentially missing nuances in the nature of the citations. The study also doesn't account for the influence of article type (e.g., review articles are likely to be cited more).
*   **Relationships to other studies:** This study aligns with other research characterizing scientific fields and journals based on citation patterns.  It contributes to the understanding of the multidisciplinary nature of health informatics and the roles of different journals in knowledge dissemination.

**Paper 3: Reference Publication Year Spectroscopy (RPYS) in practice: A software tutorial (Marx & Bornmann, 2021)**

*   **Key Methodologies:** This paper presents a tutorial on Reference Publication Year Spectroscopy (RPYS), a method for identifying seminal papers in a given field or topic by analyzing the distribution of cited reference years. The paper demonstrates the application of RPYS to three case studies: papers published in the Journal of Informetrics, papers on altmetrics, and papers published by Ludo Waltman.
*   **Major Findings:** The RPYS analyses identify different sets of seminal papers for each of the three case studies. The analysis of the Journal of Informetrics retrieved foundational papers in scientometrics, while the altmetrics analysis retrieved papers discussing the limitations of citation-based metrics. The Waltman analysis retrieved papers on network analysis, citation relations, and citation impact measurement.  The paper highlights the utility of RPYS for understanding the historical roots and intellectual foundations of different research areas.
*   **Limitations:** RPYS is sensitive to the choice of the analyzed publication set and the parameters used in the analysis. The method primarily identifies papers that are frequently cited, which may not always correspond to the most conceptually influential or groundbreaking works.  The interpretation of RPYS results requires expert knowledge of the field being analyzed. The reliance on citation counts alone can be misleading, as older papers have had more time to accumulate citations.
*   **Relationships to other studies:** This paper builds upon the existing literature on citation analysis and scientometrics.  It provides a practical guide to using RPYS, a technique that complements other methods for identifying influential publications and mapping the evolution of scientific fields.

**Comparative Analysis and Research Gaps:**

These three papers illustrate the versatility of citation network analysis in different contexts. Zhang et al. (2021) focuses on developing a sophisticated statistical model to understand the generative dynamics of citations, while Liang et al. (2018) uses a more descriptive approach to characterize journals based on their citation profiles. Marx & Bornmann (2021) provides a practical application of RPYS for identifying seminal works.

**Methodological Comparison:**

*   **Zhang et al. (2021)** employs a complex statistical model (CERGM) requiring specialized software and expertise. Its strength lies in its ability to model network dependencies and control for various factors influencing citation.
*   **Liang et al. (2018)** uses a simpler, more descriptive approach based on citation counts and categorization. This approach is easier to implement but provides less nuanced insights into citation dynamics.
*   **Marx & Bornmann (2021)** utilizes RPYS, which is a specific technique for identifying seminal papers. It requires specialized software but is relatively straightforward to apply and interpret.

**Research Gaps:**

1.  **Qualitative analysis of citations:**  All three studies primarily rely on quantitative analysis of citation counts.  Future research could benefit from incorporating qualitative analysis of the *content* of citations to understand the nature of the relationship between citing and cited works (e.g., supportive, critical, or merely perfunctory).
2.  **Dynamic Citation Networks:** Most analyses treat citation networks as static snapshots.  Developing methods to analyze the evolution of citation networks over time could provide insights into the changing landscape of scientific fields.  This would involve time-series analysis of citation patterns and the identification of emerging research trends.
3.  **Integration of Text Mining:** Combining citation network analysis with text mining techniques could allow for a more comprehensive understanding of the relationship between publications.  For example, text mining could be used to identify the specific concepts or arguments that are being cited, providing a richer understanding of the influence of different works.
4.  **Software Accessibility and Interoperability:** While Zhang et al. provide software for their CERGM, the field as a whole would benefit from more accessible and interoperable software tools for citation network analysis.  This would facilitate the wider adoption of these methods and encourage interdisciplinary collaboration.

**Conclusion:**

Citation network analysis is a powerful tool for understanding the structure and dynamics of scientific knowledge. The papers reviewed here demonstrate the diverse applications of this methodology, ranging from legal precedent analysis to characterizing journals and identifying seminal works. While significant progress has been made, future research should focus on incorporating qualitative analysis, developing dynamic models, integrating text mining techniques, and improving software accessibility to unlock the full potential of citation network analysis.

### Bias detection in reviews
## Critical Analysis of Bias Detection in Reviews: A Systematic Literature Review

This report analyzes three papers focusing on bias detection, encompassing media bias and bias in facial analysis. The analysis will cover key methodologies, major findings, limitations, and relationships between the studies, ultimately identifying research gaps and potential future directions.

**1. Key Methodologies and Major Findings:**

*   **"The Media Bias Taxonomy: A Systematic Literature Review on the Forms and Automated Detection of Media Bias" (Arxiv: 2312.16148v3):** This paper presents a systematic literature review of 3140 research papers published between 2019 and 2022, focusing on computational methods for detecting media bias. The core methodology involves a structured review process to categorize and analyze existing research. The key deliverable is the "Media Bias Taxonomy," which aims to provide a coherent framework for understanding different types of media bias. The major findings highlight the active nature of the field, the dominance of transformer-based classification approaches, and their success in improving classification accuracy and detecting fine-grained biases. However, the review also identifies a lack of interdisciplinarity and a need for more comprehensive bias assessment strategies.
*   **"Introducing MBIB -- the first Media Bias Identification Benchmark Task and Dataset Collection" (Arxiv: 2304.13148v1):** This paper introduces the Media Bias Identification Benchmark (MBIB), a unified benchmark for evaluating media bias detection techniques across different types of bias (linguistic, cognitive, political). The methodology involves reviewing 115 datasets and selecting 22 datasets associated with nine tasks. State-of-the-art transformer techniques (T5, BART) are used to evaluate the benchmark. The major findings reveal that while some bias types (hate speech, racial bias, gender bias) are easier to detect, models struggle with cognitive and political bias. The study also notes an uneven distribution of research interest and resource allocation across different bias types.
*   **"Anatomizing Bias in Facial Analysis" (Arxiv: 2112.06522v1):** This paper focuses on bias detection and mitigation in facial analysis systems. The methodology involves a systematic review of algorithms for understanding bias, along with a taxonomy and overview of existing bias mitigation algorithms. The paper encapsulates bias detection/estimation and mitigation algorithms for facial analysis. The major findings highlight the existence of biases in facial analysis systems against certain demographic subgroups, emphasizing the need for fairness and non-discrimination. The paper also discusses open challenges in the field of biased facial analysis.

**2. Limitations:**

*   **"The Media Bias Taxonomy"**: The sheer volume of papers reviewed (3140) could introduce limitations in the depth of analysis for each individual study. While the taxonomy provides a valuable overview, it may not capture the nuances of specific research contributions. Furthermore, the focus on papers published between 2019 and 2022 might exclude relevant earlier work.
*   **"Introducing MBIB"**: The selection of datasets and tasks for the MBIB benchmark could be subjective and might not fully represent the entire spectrum of media bias. The benchmark's reliance on transformer-based techniques might limit its applicability to other types of models. The uneven distribution of research interest and resource allocation to the individual tasks in media bias means the benchmark may be more robust for some bias types than others.
*   **"Anatomizing Bias in Facial Analysis"**: The paper's scope is limited to facial analysis, potentially overlooking broader implications of bias in AI systems. The rapid advancements in facial analysis technology might render some of the discussed algorithms outdated.

**3. Relationships Between Studies:**

*   **Complementary Focus:** The papers complement each other by addressing bias detection in different domains. "The Media Bias Taxonomy" and "Introducing MBIB" focus on media bias, while "Anatomizing Bias in Facial Analysis" addresses bias in facial recognition.
*   **Taxonomy and Benchmarking:** "The Media Bias Taxonomy" provides a conceptual framework for understanding media bias, which can inform the design and evaluation of benchmarks like MBIB.
*   **Shared Goal:** All three papers share the common goal of identifying and mitigating bias in AI systems, emphasizing the importance of fairness and non-discrimination.
*   **MBIB as a practical application:** The MBIB benchmark can be seen as a practical application of the theoretical frameworks discussed in "The Media Bias Taxonomy". It provides a concrete way to evaluate the performance of bias detection techniques.

**4. Research Gaps and Future Directions:**

*   **Interdisciplinarity:** "The Media Bias Taxonomy" highlights the lack of interdisciplinarity in media bias detection research. Future research should integrate insights from various disciplines, such as journalism, political science, and psychology, to develop more comprehensive and nuanced bias detection methods.
*   **Cognitive and Political Bias:** "Introducing MBIB" reveals that models struggle to detect cognitive and political bias. Future research should focus on developing techniques specifically tailored to address these challenging bias types.
*   **Bias Mitigation:** While "Anatomizing Bias in Facial Analysis" discusses bias mitigation algorithms, further research is needed to develop more effective and robust mitigation strategies. This includes exploring techniques such as adversarial training, data augmentation, and fairness-aware model design.
*   **Explainable Bias Detection:** Future research should focus on developing explainable bias detection methods that can provide insights into the underlying reasons for bias. This would enable more targeted and effective mitigation strategies.
*   **Longitudinal Studies:** There is a need for longitudinal studies that track the evolution of bias in media and AI systems over time. This would help to identify emerging biases and assess the effectiveness of mitigation efforts.
*   **Ethical Considerations:** Further research is needed to address the ethical considerations associated with bias detection, such as the potential for misuse of bias detection tools and the impact of bias detection on freedom of expression.

**5. Conclusion:**

The three papers analyzed in this report provide valuable insights into the challenges and opportunities of bias detection in reviews. While significant progress has been made in developing computational methods for detecting media bias and bias in facial analysis, several research gaps remain. Future research should focus on promoting interdisciplinarity, addressing challenging bias types, developing effective mitigation strategies, and addressing the ethical considerations associated with bias detection. By addressing these gaps, we can move closer to building fairer and more equitable AI systems.

### Machine learning for topic modeling
## Critical Analysis of Machine Learning for Topic Modeling: A Systematic Review

This report analyzes three papers focusing on the application of machine learning (ML) to topic modeling, a technique used to discover abstract "topics" within a collection of documents. The analysis will cover the methodologies employed, major findings, limitations, and relationships between the studies, highlighting research gaps and potential future directions.

**1. Methodologies and Major Findings:**

*   **"Theme and Topic: How Qualitative Research and Topic Modeling Can Be Brought Together" (2022):** This paper takes a design-oriented approach, focusing on bridging the gap between qualitative research methods and machine learning-based topic modeling.

    *   **Methodology:** The authors propose a "Theme and Topic" system, an interactive tool designed for qualitative researchers. Their methodology involves: (1) investigating the workflows of qualitative researchers, (2) designing a system that integrates topic modeling into these workflows, and (3) creating interfaces that map qualitative research concepts onto ML concepts.
    *   **Major Findings:** The primary finding is the successful development of a system that makes topic modeling more accessible and understandable to qualitative researchers. The paper emphasizes the importance of aligning ML tools with existing human professional processes to facilitate adoption and learning. The focus is on the *process* of integration rather than evaluating the performance of any specific topic model.

*   **"The Top 10 Topics in Machine Learning Revisited: A Quantitative Meta-Study" (2017):** This paper adopts a quantitative approach to identify prevalent research topics within the field of machine learning.

    *   **Methodology:** The authors collected 54,000 abstracts from leading ML journals and conferences (2007-2016). They then applied machine learning techniques (unspecified in the abstract, but presumed to be topic modeling algorithms) to extract the top 10 research topics.
    *   **Major Findings:** The study provides a data-driven perspective on the most actively researched areas in machine learning during the specified period. This allows researchers to identify popular and emerging topics. The paper highlights the potential of quantitative methods to reduce the bias inherent in traditional qualitative surveys. The specific topics identified are not detailed in the abstract.

*   **"The Geometric Structure of Topic Models" (2024):** This paper focuses on improving the interpretability of topic models by analyzing their geometric structure.

    *   **Methodology:** The authors propose an "incidence-geometric method" based on conceptual scaling to derive an ordinal structure from topic models (specifically non-negative matrix factorization). This allows for analysis in higher dimensions and the extraction of conceptual relationships between topics. They then introduce a novel visualization paradigm based on ordinal motifs to represent concept hierarchies. The approach is demonstrated using a corpus of scientific papers from 32 top machine learning venues.
    *   **Major Findings:** The study demonstrates that analyzing the geometric structure of topic models can reveal conceptual relationships between topics that are not apparent through traditional methods like similarity matrices or top-term lists. The proposed visualization paradigm offers a top-down view of topic spaces, improving interpretability.

**2. Limitations:**

*   **"Theme and Topic" (2022):** The abstract lacks detail regarding the specific topic modeling algorithms used within the system. The evaluation of the system's effectiveness is not discussed, leaving questions about its impact on qualitative research practices. The focus is on usability and accessibility rather than quantitative performance.
*   **"Top 10 Topics" (2017):** The abstract does not specify the machine learning techniques used for topic extraction, nor does it list the identified top 10 topics. This limits the ability to critically assess the results. The study is also limited by its reliance on abstracts, which may not fully represent the content of the papers.
*   **"Geometric Structure" (2024):** While the paper presents a novel approach to topic model interpretation, the abstract does not discuss the computational complexity of the proposed method. The generalizability of the approach to different types of corpora and topic models beyond non-negative matrix factorization is unclear. The abstract focuses on the theoretical framework and visualization, with limited discussion of practical application or comparative performance against other interpretation methods.

**3. Relationships Between Studies:**

*   The papers represent different facets of research on topic modeling. "Theme and Topic" (2022) focuses on *bridging the gap* between ML and qualitative methods, while "Top 10 Topics" (2017) uses topic modeling as a tool for *meta-analysis* of the ML field itself. "Geometric Structure" (2024) focuses on *improving the interpretability* of topic models.
*   "Theme and Topic" (2022) implicitly acknowledges the need for more accessible and user-friendly topic modeling tools, a challenge that "Geometric Structure" (2024) addresses by improving interpretability through novel visualization techniques.
*   The "Top 10 Topics" (2017) paper provides a broad overview of research trends in ML, which could inform the development of more targeted and relevant topic models for specific subfields, as explored in "Geometric Structure" (2024) within the context of top ML venues.

**4. Research Gaps and Future Directions:**

*   **Evaluation of Integrated Systems:** There is a need for rigorous evaluation of systems like "Theme and Topic" (2022) to assess their impact on qualitative research outcomes. This should include quantitative measures of efficiency and qualitative assessments of the insights gained.
*   **Comparative Analysis of Topic Modeling Techniques:** The "Top 10 Topics" (2017) paper highlights the need for more detailed analysis of different topic modeling algorithms and their suitability for specific tasks and datasets. Future research should compare the performance of various techniques across different domains.
*   **Scalability and Generalizability:** The "Geometric Structure" (2024) paper presents a promising approach to improving interpretability. Future research should investigate the scalability of the method to larger datasets and its applicability to different types of topic models and corpora.
*   **Addressing Bias in Topic Modeling:** The "Top 10 Topics" (2017) paper mentions the reduction of bias through quantitative methods. However, more research is needed to address potential biases in topic modeling algorithms themselves, particularly in relation to sensitive topics and demographic groups.
*   **Explainable AI (XAI) for Topic Models:** Further research is needed to develop more explainable AI (XAI) techniques for topic models. This would involve not only visualizing the topic structure but also providing justifications for the assigned topics and their relationships to the underlying documents.

**5. Conclusion:**

These three papers highlight the diverse applications of machine learning in topic modeling, ranging from facilitating qualitative research to analyzing research trends and improving model interpretability. While each paper contributes valuable insights, there are limitations and research gaps that need to be addressed. Future research should focus on rigorous evaluation, comparative analysis, scalability, bias mitigation, and the development of XAI techniques to further enhance the utility and trustworthiness of topic modeling. The field would benefit from studies that not only develop novel algorithms but also rigorously evaluate their practical impact and address potential ethical concerns.

### Systematic review automation platforms
## Critical Analysis of Systematic Review Automation Platforms in the Context of IoT and Security Orchestration

This report analyzes three papers focusing on automation platforms, specifically within the contexts of home automation security and security orchestration. We examine their methodologies, findings, limitations, and inter-relationships to identify research gaps and potential future directions.

**1. A Study of Data Store-based Home Automation (Alrawi et al., 2018)**

*   **Key Methodologies:** This paper employs a semi-automated security evaluation of two popular home automation platforms, Google's Nest and Philips Hue. The methodology involves analyzing platform access control enforcement, non-system enforcement procedures, and potential misuse of routines. The analysis appears to be primarily static analysis of the platforms' architecture and API interactions.
*   **Major Findings:** The study identifies ten key security vulnerabilities, including lateral privilege escalation through misuse of routines, ineffective product review systems, and the potential for arbitrary app manipulation. These findings highlight security flaws inherent in centralized data store-based home automation platforms.
*   **Limitations:** The study focuses on only two specific platforms, limiting the generalizability of the findings to other home automation systems. The semi-automated approach might have missed subtle vulnerabilities that a manual, in-depth penetration test could uncover. The study also lacks quantitative performance metrics for the identified security vulnerabilities. Furthermore, the long time since publication means these vulnerabilities may have been patched.
*   **Relationship to Other Studies:** This study provides a concrete security analysis of specific home automation platforms, complementing the broader discussion on security orchestration. It highlights the importance of securing individual components within a larger automated ecosystem.

**2. Can Commercial Testing Automation Tools Work for IoT? A Case Study of Selenium and Node-Red (Rathore et al., 2021)**

*   **Key Methodologies:** The research adopts a design science approach. It begins with a systematic literature review (SLR) to identify requirements and challenges for IoT testing automation.  Based on the SLR, a testing automation tool is built using Selenium for IoT applications written in Node-Red. The framework is then functionally tested on multiple browsers, with preliminary evaluation on maintainability, browser capability, and comprehensiveness.
*   **Major Findings:** The study concludes that using commercial tools like Selenium for testing automation in IoT is feasible.  However, it acknowledges significant challenges related to high data volumes and parallel data processing that need to be addressed for complete integration.
*   **Limitations:**  The evaluation of the proposed framework is preliminary and lacks rigorous quantitative analysis. The focus on Node-Red limits the generalizability of the findings to other IoT platforms. The study also does not delve into the security aspects of the automated testing process itself, which could introduce new vulnerabilities. The systematic literature review is not presented in detail, making it difficult to assess its rigor and comprehensiveness.
*   **Relationship to Other Studies:** This paper directly addresses the practical application of automation tools in the IoT domain. It provides a concrete example of integrating a commercial testing tool with an IoT platform, which can inform the development of more robust and scalable testing solutions. It also highlights the challenges related to data volume and parallel processing, which are relevant to security orchestration.

**3. A Multi-Vocal Review of Security Orchestration (Khan et al., 2020)**

*   **Key Methodologies:** This paper presents a multivocal literature review (MLR) of security orchestration. The review systematically selects and analyzes both academic and grey literature (blogs, web pages, white papers) published from January 2007 to July 2017. The MLR approach aims to provide a comprehensive overview of the field, including both formal research and practical insights.
*   **Major Findings:** The review provides a working definition of security orchestration and classifies its functionalities into unification, orchestration, and automation. It identifies core components of a security orchestration platform and categorizes the drivers based on technical and socio-technical aspects.  The paper also proposes a taxonomy of security orchestration based on execution environment, automation strategy, deployment type, mode of task, and resource type.
*   **Limitations:** The MLR approach, while comprehensive, is inherently subjective in the selection and interpretation of grey literature. The review period ends in 2017, potentially missing recent advancements in the field.  The paper focuses on defining and categorizing security orchestration, but it does not provide a detailed analysis of specific platforms or their effectiveness.
*   **Relationship to Other Studies:** This paper provides a high-level overview of security orchestration, setting the stage for more specific investigations. It identifies key areas of research and development, such as the need for better integration between different security tools and the importance of considering socio-technical factors. It also provides a framework for understanding the different types of security orchestration solutions.

**Comparison of Methodologies and Results:**

All three papers employ systematic literature reviews (SLRs) or a variant thereof (MLR), demonstrating the importance of understanding the existing body of knowledge before conducting further research or developing new solutions. However, the scope and focus of each review differ significantly. Alrawi et al. (2018) focuses on the security aspects of specific home automation platforms, while Rathore et al. (2021) investigates the feasibility of using commercial testing tools for IoT applications. Khan et al. (2020) takes a broader perspective, aiming to define and categorize the field of security orchestration.

The findings of the three papers are complementary. Alrawi et al. (2018) highlights the security risks associated with poorly designed automation platforms. Rathore et al. (2021) demonstrates the potential of using commercial tools for automating testing in IoT, but also acknowledges the challenges involved. Khan et al. (2020) provides a framework for understanding how security orchestration can address these challenges by integrating different security tools and automating security tasks.

**Research Gaps:**

Based on the analysis of these three papers, several research gaps can be identified:

*   **Security of Automation Platforms:** Further research is needed to develop secure-by-design principles for automation platforms, addressing the vulnerabilities identified by Alrawi et al. (2018). This includes exploring techniques for enforcing access control, validating user inputs, and preventing privilege escalation.
*   **Scalability and Performance of IoT Testing Automation:** Rathore et al. (2021) highlights the challenges of testing IoT applications with high data volumes and parallel processing. Further research is needed to develop scalable and performant testing automation solutions that can handle these challenges. This includes exploring techniques for data reduction, parallel testing, and distributed testing.
*   **Evaluation of Security Orchestration Platforms:** Khan et al. (2020) provides a framework for understanding security orchestration, but it does not provide a detailed analysis of specific platforms or their effectiveness. Further research is needed to evaluate the performance, scalability, and security of different security orchestration platforms. This includes developing metrics for measuring the effectiveness of security orchestration and conducting case studies to assess the impact of security orchestration on real-world security operations.
*   **Integration of Security and Testing Automation:** There is a lack of research on the integration of security and testing automation. Further research is needed to develop automated security testing tools that can be integrated into the CI/CD pipeline. This includes exploring techniques for vulnerability scanning, penetration testing, and security code review.
*   **Human Factors in Security Orchestration:** Khan et al. (2020) identifies the importance of socio-technical factors in security orchestration. Further research is needed to understand how human factors, such as user experience and training, impact the effectiveness of security orchestration. This includes exploring techniques for designing user-friendly security orchestration platforms and providing effective training for security personnel.

**Practical and Theoretical Implications:**

The findings of these papers have several practical and theoretical implications:

*   **Practical Implications:**
    *   Developers of automation platforms should prioritize security by design, addressing the vulnerabilities identified by Alrawi et al. (2018).
    *   Organizations deploying IoT applications should invest in robust testing automation solutions that can handle high data volumes and parallel processing.
    *   Security operations centers should consider adopting security orchestration platforms to improve the efficiency and effectiveness of their security operations.
*   **Theoretical Implications:**
    *   The research highlights the need for a holistic approach to security, considering both the technical and socio-technical aspects of automation platforms.
    *   The research contributes to the development of a theoretical framework for understanding security orchestration, including its functionalities, components, and drivers.
    *   The research identifies several research gaps that can inform future research on automation platforms and security orchestration.

**Conclusion:**

This analysis has highlighted the importance of automation platforms in various contexts, including home automation, IoT, and security operations. The papers reviewed demonstrate the potential benefits of automation, but also the challenges and risks involved. By addressing the research gaps identified in this report, we can pave the way for the development of more secure, scalable, and effective automation solutions.

### NLP tools for text summarization
## Critical Analysis of NLP Tools for Text Summarization: A Comparative Review

This report analyzes three recent papers focusing on Natural Language Processing (NLP) tools for text summarization, with a particular emphasis on addressing challenges related to language diversity, computational efficiency, and ethical considerations. The papers explore diverse methodologies, ranging from traditional extractive summarization techniques enhanced by Large Language Models (LLMs) to the application of open-source and closed-source LLMs in low-resource language scenarios. This analysis will compare the methodologies and results presented, identify research gaps, and discuss the practical and theoretical implications of each study.

**1. Survey of Pseudonymization, Abstractive Summarization & Spell Checker for Hindi and Marathi (arxiv_id: 2412.18163v1)**

*   **Key Methodologies:** This paper outlines the development of a platform integrating pseudonymization, abstractive summarization, and spell-checking tools for English, Hindi, and Marathi. The specific techniques used for abstractive summarization are not detailed in the abstract, which is a significant limitation. The focus is on building a platform for enterprise and consumer clients using Indian regional languages.
*   **Major Findings:** The primary finding is the development of a functional platform. However, the lack of specific performance metrics or comparative analysis against existing summarization techniques makes it difficult to assess the effectiveness of the proposed system.
*   **Limitations:** The major limitation is the absence of detailed information regarding the summarization algorithms employed. Without this, it is impossible to evaluate the novelty or efficiency of the approach. Furthermore, the abstract lacks quantitative results, making it difficult to gauge the platform's performance. The paper is framed as a survey and platform development announcement rather than a rigorous experimental evaluation.
*   **Relationships to other studies:** This paper highlights the need for NLP tools tailored to low-resource languages like Hindi and Marathi. It connects to the "Open or Closed LLM for Lesser-Resourced Languages? Lessons from Greek" paper (discussed below) by emphasizing the challenges of adapting NLP techniques to languages with limited resources. However, it lacks the methodological depth and experimental rigor of the other two studies.

**2. Scaling Up Summarization: Leveraging Large Language Models for Long Text Extractive Summarization (arxiv_id: 2408.15801v1)**

*   **Key Methodologies:** This paper introduces EYEGLAXS, an extractive summarization framework that leverages LLMs (LLAMA2-7B and ChatGLM2-6B) for long text documents.  It utilizes Flash Attention and Parameter-Efficient Fine-Tuning (PEFT) to address computational challenges. The framework focuses on extractive methods to avoid the factual inaccuracies often associated with abstractive techniques. The experimental design includes benchmarking on PubMed and ArXiv datasets.
*   **Major Findings:** EYEGLAXS sets new performance benchmarks on PubMed and ArXiv datasets. The research demonstrates the adaptability of LLMs in handling different sequence lengths and their efficiency in training on smaller datasets. The study shows that extractive summarization using LLMs can be both efficient and accurate.
*   **Limitations:** While the paper reports improved performance, the abstract doesn't specify the evaluation metrics used (e.g., ROUGE scores). A more detailed description of the evaluation process and a comparison with other state-of-the-art extractive summarization methods would strengthen the findings. Furthermore, the study focuses solely on extractive summarization, neglecting the potential benefits of hybrid approaches that combine extractive and abstractive techniques.
*   **Relationships to other studies:** This paper builds upon the growing body of research exploring the application of LLMs to NLP tasks. It directly addresses the limitations of abstractive summarization, specifically factual inaccuracies, and proposes an alternative extractive approach. It contrasts with the first paper by providing a concrete methodology, experimental results, and a clear focus on performance optimization.

**3. Open or Closed LLM for Lesser-Resourced Languages? Lessons from Greek (arxiv_id: 2501.12826v1)**

*   **Key Methodologies:** This study compares the performance of open-source (Llama-70b) and closed-source (GPT-4o mini) LLMs on seven core NLP tasks for Modern Greek. It also explores authorship attribution as a method to assess potential data usage by LLMs in pre-training. Additionally, it presents a legal NLP case study using a Summarize, Translate, and Embed (STE) methodology for clustering long legal texts, comparing it to the traditional TF-IDF approach.
*   **Major Findings:** The study reveals task-specific strengths and weaknesses of open-source and closed-source LLMs for Greek, demonstrating parity in their overall performance. The high 0-shot accuracy in authorship attribution raises ethical concerns about data provenance. The STE methodology outperforms TF-IDF for clustering long legal texts, highlighting the potential of LLMs for domain-specific applications in low-resource languages.
*   **Limitations:** The generalizability of the findings to other low-resource languages may be limited due to the specific characteristics of the Greek language and the available datasets. While the study explores ethical implications, it does not delve into specific mitigation strategies for addressing potential data provenance issues.  The scope of the legal NLP case study is limited to clustering, and further research is needed to explore other legal NLP tasks.
*   **Relationships to other studies:** This paper directly addresses the challenges of applying LLMs to low-resource languages, a concern also raised in the first paper. It provides a rigorous comparative analysis of open-source and closed-source models, offering valuable insights for researchers working with similar languages. The ethical considerations regarding data provenance are particularly relevant in the context of rapidly evolving LLM technology.

**Comparative Analysis and Research Gaps:**

| Feature           | Survey of Pseudonymization, Abstractive Summarization & Spell Checker | Scaling Up Summarization: Leveraging Large Language Models for Long Text Extractive Summarization | Open or Closed LLM for Lesser-Resourced Languages? Lessons from Greek |
|-------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| **Methodology**   | Platform development (details lacking)                                  | Extractive summarization with LLMs (LLAMA2-7B, ChatGLM2-6B), Flash Attention, PEFT                   | Comparative analysis of LLMs, authorship attribution, STE methodology   |
| **Focus**         | Low-resource languages (Hindi, Marathi)                                | Efficient extractive summarization of long texts                                                     | Low-resource language (Greek), ethical considerations, legal NLP         |
| **Evaluation**    | Not specified                                                           | Benchmarking on PubMed and ArXiv datasets                                                              | Performance on 7 NLP tasks, authorship attribution accuracy, clustering performance |
| **Limitations**    | Lack of detail, no quantitative results                                | Focus on extractive summarization only, limited metric specification                                   | Generalizability to other languages, limited ethical mitigation strategies |

**Research Gaps:**

1.  **Hybrid Summarization Techniques:** Further research is needed to explore hybrid summarization approaches that combine the strengths of both extractive and abstractive methods, particularly for low-resource languages.
2.  **Ethical Considerations:**  More research is needed to develop practical mitigation strategies for addressing ethical concerns related to data provenance and bias in LLMs, especially when applied to low-resource languages.
3.  **Domain-Specific Adaptation:**  Further investigation is required to develop effective methods for adapting LLMs to specific domains in low-resource languages, beyond the legal domain explored in the Greek study.
4.  **Explainability and Interpretability:**  Future studies should focus on improving the explainability and interpretability of LLM-based summarization models, enabling users to understand the reasoning behind the generated summaries.
5.  **Resource-Efficient Techniques:**  Exploring more resource-efficient techniques for training and deploying LLMs in low-resource settings is crucial to democratize access to advanced NLP tools.

**Conclusion:**

The three papers reviewed highlight the ongoing research efforts to develop effective and ethical NLP tools for text summarization. While the first paper focuses on platform development for Indian regional languages, it lacks the methodological rigor and experimental validation of the other two studies. The second paper demonstrates the potential of LLMs for efficient extractive summarization, while the third paper provides valuable insights into the performance of open-source and closed-source LLMs for a low-resource language, raising important ethical considerations. By addressing the identified research gaps, future research can further advance the field of NLP and ensure that its benefits are accessible to all languages and communities. The need for robust evaluation metrics, explainable models, and ethically sound practices remains paramount in this rapidly evolving field.


## References
- A Multi-Vocal Review of Security Orchestration (2020-02-21). http://arxiv.org/abs/2002.09190v1
- A Study of Data Store-based Home Automation (2018-12-04). http://arxiv.org/abs/1812.01597v1
- Anatomizing Bias in Facial Analysis (2021-12-13). http://arxiv.org/abs/2112.06522v1
- Automated data processing and feature engineering for deep learning and big data applications: a survey (2024-03-18). http://arxiv.org/abs/2403.11395v2
- Automated split Hopkinson pressure bar for high throughput dynamic experiments (2025-02-04). http://arxiv.org/abs/2502.02729v1
- CRUISE-Screening: Living Literature Reviews Toolbox (2023-09-04). http://arxiv.org/abs/2309.01684v1
- CSMeD: Bridging the Dataset Gap in Automated Citation Screening for Systematic Literature Reviews (2023-11-21). http://arxiv.org/abs/2311.12474v1
- Can Commercial Testing Automation Tools Work for IoT? A Case Study of Selenium and Node-Red (2021-07-09). http://arxiv.org/abs/2107.04246v1
- Characterizing health informatics journals by subject-level dependencies: a citation network analysis (2018-07-23). http://arxiv.org/abs/1807.08841v2
- Generative Dynamics of Supreme Court Citations: Analysis with a New Statistical Network Model (2021-01-15). http://arxiv.org/abs/2101.07197v1
- Introducing MBIB -- the first Media Bias Identification Benchmark Task and Dataset Collection (2023-04-25). http://arxiv.org/abs/2304.13148v1
- MedPromptExtract (Medical Data Extraction Tool): Anonymization and Hi-fidelity Automated data extraction using NLP and prompt engineering (2024-05-04). http://arxiv.org/abs/2405.02664v3
- Open or Closed LLM for Lesser-Resourced Languages? Lessons from Greek (2025-01-22). http://arxiv.org/abs/2501.12826v1
- Reference Publication Year Spectroscopy (RPYS) in practice: A software tutorial (2021-09-02). http://arxiv.org/abs/2109.00969v3
- Scaling Up Summarization: Leveraging Large Language Models for Long Text Extractive Summarization (2024-08-28). http://arxiv.org/abs/2408.15801v1
- Streamlining Systematic Reviews: A Novel Application of Large Language Models (2024-12-14). http://arxiv.org/abs/2412.15247v1
- Survey of Pseudonymization, Abstractive Summarization & Spell Checker for Hindi and Marathi (2024-12-24). http://arxiv.org/abs/2412.18163v1
- The Geometric Structure of Topic Models (2024-03-06). http://arxiv.org/abs/2403.03607v1
- The Media Bias Taxonomy: A Systematic Literature Review on the Forms and Automated Detection of Media Bias (2023-12-26). http://arxiv.org/abs/2312.16148v3
- The Top 10 Topics in Machine Learning Revisited: A Quantitative Meta-Study (2017-03-29). http://arxiv.org/abs/1703.10121v1
- Theme and Topic: How Qualitative Research and Topic Modeling Can Be Brought Together (2022-10-03). http://arxiv.org/abs/2210.00707v1