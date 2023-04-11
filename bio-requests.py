# Script to get PubTator data from an initial query.
# Author: Inês G. Gonçalves
# Date: Feb 2021

from Bio import Entrez
import requests
import bioc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def search(query, max_results='20'):
    """Returns a list with the PMIDs gathered from the input query."""

    # PubMed notifies users with excessive requests
    # (Enter email)
    Entrez.email = "..."
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax=max_results,
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results


def get_pubtator_data(ids, id_type='pmids', export_format='biocxml', bioconcept=''):
    id_string = ','.join(ids)
    base_url = 'https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/'
    url = base_url + '{}?{}={}&concepts={}'.format(export_format, id_type, id_string, bioconcept)
    session = requests.Session()
    response = session.get(url)
    bioc_data = bioc.loads(response.text, bioc.BioCFileType.BIOC_XML)

    return bioc_data


def get_annotation_list(bioc_data):
    annotations = []
    for annotation in bioc.annotations(bioc_data):
        ann_text = annotation.text
        ann_infons = annotation.infons
        if len(list(ann_infons.keys())) > 1:
            ann_identifier = ann_infons[list(ann_infons.keys())[0]]
            ann_type = ann_infons[list(ann_infons.keys())[1]]
        else:
            ann_identifier = 'NULL'
            ann_type = list(ann_infons.keys())[0]

        annotations.append([ann_text, ann_identifier, ann_type])

    return annotations


query = 'neuroblastoma'
results = search(query, '100')
pmids = results['IdList']
bioc_data = get_pubtator_data(pmids)
annotations = get_annotation_list(bioc_data)
df = pd.DataFrame(annotations, columns=['text', 'identifier', 'type'])
