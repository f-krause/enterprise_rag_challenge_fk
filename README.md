# Enterprise RAG Challenge - Solutions
by Felix Krause

<img width="2446" height="993" alt="project12" src="https://github.com/user-attachments/assets/ce79fac1-0541-49c4-b34f-1ec88c07826f" />


Solutions to the [Enterprise RAG Challenge](https://www.timetoact-group.at/details/enterprise-rag-challenge) of Timetoact Austria on 27.02.2025.

[BLOG POST](https://www.timetoact-group.at/en/techblog/techblog/8th-place-in-enterprise-rag-challenge-2025-answering-business-questions-with-llms) explaining the solutions here.


## Current Solutions
- [Google Gemini 2.0 Flash - Naive Approach](solutions/gemini_naive.ipynb): full PDF(s) in context 
- Multi-agent approaches (openAI based router to extend and specialise queries for each company)
  - [Qdrant RAG](solutions/1_create_qdrant_db.ipynb)
    - Custom chunking of markdown file obtained via [docling](https://github.com/DS4SD/docling) parser
    - Then [Qdrant](https://qdrant.tech/) for vector database retrieval of chunks (top 5)
    - [openAI o4](solutions/2_main_agents_OPENAI.ipynb) or [IBM granite-20b-code-instruct](solutions/2_main_agents_IBM.ipynb) based answer generation per specialised company query, and o4 based final answer generation
  - [Gemini Retrieval and openAI Generation](solutions/2_gemini_openai.ipynb)
    - Gemini 2.0 Flash with full PDF in context for retrieval
    - OpenAI for final answer generation based on Gemini's company specific answers



## Environment
Create environment from environment.yml file:
```bash
mamba env create -f environment.yml
```

Export environment.yml:
```bash
mamba env export > environment.yml
```


## Tracing
To trace, first start a trace server:
```bash
python -m phoenix.server.main serve
```
