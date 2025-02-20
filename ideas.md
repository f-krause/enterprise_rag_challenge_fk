# Brainstorming

## Ad Rinat:
- will questions/generator be known in advance?
- public evaluation set?
- how similar to old challenge?

## Ideas
- Evaluation set?
- Haystack!
- file format -> well formatted/easier to interpret than pdf
  - Check: https://www.reddit.com/r/LangChain/comments/1dzj5qx/best_pdf_parser_for_rag/
  - Check: https://github.com/NirDiamant/RAG_Techniques
  - [Docling](https://github.com/DS4SD/docling)? 
  - [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)
  - -> Experiment: how tables are outputted
  - convert PDFs to latex?
- document preprocess -> table vs. text
	- process tables separately?
	- flag tables over multiple pages and then extract tables manually
- In context: financial synonyms/domain knowledge in context?
- Solution pipeline
	1. Lookup tables like Daniel
		- split tables from text?
		- more sophisticated processing pipeline of PDFs/tables (how?) 	
	2. If fails: backup plan (Multiagent approach with classic RAG)
		- Improve context (chapter headers, reranking?)
		- Router to specialised RAG systems 
		- RAG with high accuracy (less optimized on speed) -> Chroma
	3. If fails: agent loop with full text search? (LOW PRIO)
		- Iterative: output why failed before and what to do better 
		- PostgresSQL (full text + vector db)
			- let LLM search for keywords + context
		- iterating search queries until solution found
- Pipeline tools
	- Calculator/python kernel -> ratio computation
	- Websearch tool? (duckduckgo?)


At inference time: load chunks, store with index (see [here](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/context_enrichment_window_around_chunk.ipynb)) 
and then ask LLM if it thinks a table has been cut and if necessary information could be useful, allow to receive 
continuation of chunk and combine them. -> necessary with PyMuPDF4LLM?

[Reranking](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/reranking.ipynb)

Rephrasing - rephrase user query in simpler terms for RAG retrieval (than for final answer use original query?)

Idea: add to each chunk, chapter (and subchapter) headers (or split by chapters altogether)
-> should be possible with PyMuPDF4LLM (as markdown files, just need logic to retrieve headers and attach them to chunks)


fusion search (key word and vector based) - [here](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/fusion_retrieval.ipynb)



TODO: try claude citations (for proper referencing - should work well according to daniel if data is already chunked)

TODO: check if can inject code to count pages in docling md from within source code when parsing pdf page by page?
