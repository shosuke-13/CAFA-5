# CAFA 5 Protein Function Prediction (Ongoing)
### *Kaggle Competition about bioinfomatics & machine-learning*

## Protein sequences embedding, EDA train dataset, Dimensionality Reduction is ongoing.
## if some analysis have done, I will upload source code.

![CAFA 5 Protein Function Prediction](https://storage.googleapis.com/kaggle-competitions/kaggle/41875/logos/thumb76_76.png?t=2023-02-28-14-18-54)


## [Competition Overview](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/overview)

>  Goal of the Competition
>  The goal of this competition is to predict the function of a set of proteins. You will develop a model trained on the amino-acid sequences of the proteins and on other data. Your work will help ​​researchers better understand the function of proteins, which is important for discovering how cells, tissues, and organs work. This may also aid in the development of new drugs and therapies for various diseases.


### Summarize Overview

1.  The competition aims to predict the function of proteins using models trained on amino-acid sequences and other data.
2.  This will aid researchers in understanding protein function, leading to the development of new drugs and therapies for diseases. (Reference: Research paper)

### Dataset Background

1.  The Gene Ontology (GO) is a hierarchy that describes the biological function of genes and gene products at different levels of abstraction.
2.  The protein's function is represented by a subset of one or more of the subontologies, and annotations are supported by evidence codes. (Ashburner et al., 2000)

###  Files
More details is available on [competition data page](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/data).

| File | Contents |
|---|-----|
|**train_sequences.fasta**|amino acid sequences for proteins in training set|
|**train_terms.tsv**|the training set of proteins and corresponding annotated GO terms|
|**train_taxonomy.tsv**|taxon ID for proteins in training set|
|**go-basic.obo**|ontology graph structure|
|**testsuperset.fasta**|amino acid sequences for proteins on which the predictions should be made|
|**testsuperset-taxon-list.tsv**|taxon ID for proteins in test superset (Note: you may need to use `encoding="ISO-8859-1"` to read this file in `pandas`)|
|**IA.txt** |Information Accretion for each term. This is used to weight precision and recall (see Evaluation)|
|**sample_submission.csv**|a sample submission file in the correct format|

### Protein sequences embedding

1.  ProtVec (word2vec) : Continuous distributed representation of biological sequences for deep proteomics and genomics. [https://arxiv.org/abs/1503.05140](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)
2.  SeqVec (ELMo) : Modeling aspects of the language of life through transfer-learning protein sequences. [https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-3220-8](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)
3.  ESM‐1b (Transformer) : TRANSFORMER PROTEIN LANGUAGE MODELS ARE  
    UNSUPERVISED STRUCTURE LEARNERS. [https://openreview.net/pdf?id=fylclEqgvgd](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)
4.  ProtTrans (BERT) : Towards cracking the language of life’s code through self-supervised deep  
    learning and high performance computing. [https://arxiv.org/abs/2007.06225](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)
5.  UDSMProt (AWD‐LSTM) : Universal deep sequence models for protein classification. [https://academic.oup.com/bioinformatics/article/36/8/2401/5698270](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)
6.  UniRep (mLSTM) : Unified rational protein engineering with sequence-based deep representation learning. [https://www.nature.com/articles/s41592-019-0598-1](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)


### What is gene onthology (GO)

Gene Ontology (GO) is a widely used resource in bioinformatics that provides structured and standardized descriptions of genes and their associated biological functions, cellular components, and molecular processes. It serves as a controlled vocabulary to annotate and characterize genes and gene products across different organisms.

The Gene Ontology Consortium develops and maintains GO, and it consists of three main categories or branches:

1. Biological Process (BP): This branch describes the series of events or activities that occur within a cell or an organism, contributing to a specific biological function. Examples of biological processes include cell division, metabolism, signal transduction, and immune response.

2. Cellular Component (CC): This branch represents the subcellular structures, locations, and complexes where gene products are active or present. Examples of cellular components include the nucleus, mitochondria, cytoskeleton, and plasma membrane.

3. Molecular Function (MF): This branch describes the specific biochemical activities or properties of gene products, such as catalytic or binding activities. Examples of molecular functions include enzyme activity, receptor binding, DNA binding, and transporter activity.

The GO terms are organized in a hierarchical structure, with broader terms at the top and more specific terms at the lower levels. This hierarchical structure allows for the representation of relationships between different terms. Additionally, each term is assigned a unique identifier, allowing researchers to refer to specific terms in their analyses.

Gene Ontology analysis involves the systematic examination of gene lists or expression data to uncover functional annotations, biological themes, and relationships within the data. It helps researchers make sense of large-scale genomic or transcriptomic datasets and gain insights into the underlying biology.

There are several approaches to conducting Gene Ontology analysis:

1. Enrichment Analysis: This approach determines whether certain GO terms are overrepresented or significantly enriched in a given gene list compared to what would be expected by chance. It helps identify the biological processes, cellular components, or molecular functions that are most relevant to the genes under study.

2. Functional Annotation Clustering: This method groups similar GO terms into clusters based on their semantic similarity. It helps identify coherent sets of functionally related genes within a dataset and provides a broader view of the functional landscape.

3. GO-Term Interrelationship Analysis: This analysis focuses on exploring relationships and dependencies between different GO terms. It can reveal connections between biological processes, cellular components, and molecular functions, providing a more comprehensive understanding of gene interactions.

Gene Ontology analysis tools and software packages, such as DAVID, Panther, and topGO, are available to facilitate these analyses. These tools typically integrate statistical algorithms to evaluate significance, visualize results, and generate functional annotation charts or networks.

In summary, Gene Ontology and its analysis provide a standardized vocabulary and computational framework to characterize and understand the functions of genes and gene products. It aids researchers in interpreting large-scale genomic data, identifying biologically relevant features, and generating hypotheses for further experimental investigation.
