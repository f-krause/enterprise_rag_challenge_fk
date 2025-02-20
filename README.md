# Enterprise RAG Challenge - Solutions
by Felix Krause

Solutions to the [Enterprise RAG Challenge](https://www.timetoact-group.at/details/enterprise-rag-challenge) of Timetoact Austria on 27.02.2025.


## Current Solutions
- [Google Gemini 2.0 Flash](solutions/gemini.ipynb): full PDF in context
- [OpenAI + qdrant RAG](solutions/openAI-qdrant.ipynb): Custom chunking of markdown file obtained via Docling, then RAG with qdrant for retrieval and openAI o4 for generation
- [IBM WatsonX](solutions/ibm_watsonx.ipynb): TODO



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
