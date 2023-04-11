# lit-mining

🎯 **Goal:** Applying text mining techniques to make a literature review more productive.

🙋 **Author:** Inês G. Gonçalves

📅 **Date:** March 2021

☑️ **Requisites**:

- APIs (see the [requests](https://requests.readthedocs.io/en/master/) library)
- The BioC file type
- Text mining/Natural Language Processing (see the [spaCy](https://spacy.io/) library)
- **Libraries**  `numpy`, `pandas`, `matplotlib`, `seaborn`, `spacy`, `requests`, `biopython`, `bioc`

## Approach

- Using the [Entrez module form BioPython](https://biopython.org/docs/1.75/api/Bio.Entrez.html) to automatically gather relevant articles on neuroblastoma from PubMed;
- Processing the articles with [PubTator]((https://www.ncbi.nlm.nih.gov/research/pubtator/api.html) to get data on species, dieseases, genes,...;
- Using the [bioc package](https://pypi.org/project/bioc/) to parse the PubTator data (BioCJSON files);
- Transforming the data into a Pandas DataFrame and doing some data exploration and visualisation (Which cell line/gene is referenced the most; Are other diseases associated with neuroblastoma?);
- Extras: Using tools like Entrez/[Cellosaurus](https://web.expasy.org/cellosaurus/) to get additional data on genes, species and cell lines.
