# Enterprise RAG Challenge - Solutions
by Felix Krause

Approaches to the [enterprise RAG challenge](https://www.timetoact-group.at/details/enterprise-rag-challenge) of Timetoact Austria on 27.02.2025.


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
