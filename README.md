# CAFA 5 Protein Function Prediction 
*Overview & Analyssis Soureces*

##### Protein sequences embedding, EDA train dataset, Dimensionality Reduction is ongoing. If some analysis have done, I will upload source code.

## [Competition Overview](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/overview)
1.  The competition aims to predict the function of proteins using models trained on amino-acid sequences and other data.
2.  This will aid researchers in understanding protein function, leading to the development of new drugs and therapies for diseases. (Reference: Research paper)

>  Goal of the Competition
>  The goal of this competition is to predict the function of a set of proteins. You will develop a model trained on the amino-acid sequences of the proteins and on other data. Your work will help ​​researchers better understand the function of proteins, which is important for discovering how cells, tissues, and organs work. This may also aid in the development of new drugs and therapies for various diseases.


## Dataset Background

1.  The Gene Ontology (GO) is a hierarchy that describes the biological function of genes and gene products at different levels of abstraction.
2.  The protein's function is represented by a subset of one or more of the subontologies, and annotations are supported by evidence codes. (Ashburner et al., 2000)

##  Files

More details is available on [competition data page](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/data).

| File | Contents |
|:---:|---|
|**train_sequences.fasta**|amino acid sequences for proteins in training set|
|**train_terms.tsv**|the training set of proteins and corresponding annotated GO terms|
|**train_taxonomy.tsv**|taxon ID for proteins in training set|
|**go-basic.obo**|ontology graph structure|
|**testsuperset.fasta**|amino acid sequences for proteins on which the predictions should be made|
|**testsuperset-taxon-list.tsv**|taxon ID for proteins in test superset (Note: you may need to use `encoding="ISO-8859-1"` to read this file in `pandas`)|
|**IA.txt** |Information Accretion for each term. This is used to weight precision and recall (see Evaluation)|
|**sample_submission.csv**|a sample submission file in the correct format|

## Protein Sequences Embedding (From discussion)

1.  ProtVec (word2vec) : Continuous distributed representation of biological sequences for deep proteomics and genomics. [https://arxiv.org/abs/1503.05140](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)
2.  SeqVec (ELMo) : Modeling aspects of the language of life through transfer-learning protein sequences. [https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-3220-8](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)
3.  ESM‐1b (Transformer) : TRANSFORMER PROTEIN LANGUAGE MODELS ARE  
    UNSUPERVISED STRUCTURE LEARNERS. [https://openreview.net/pdf?id=fylclEqgvgd](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)
4.  ProtTrans (BERT) : Towards cracking the language of life’s code through self-supervised deep  
    learning and high performance computing. [https://arxiv.org/abs/2007.06225](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)
5.  UDSMProt (AWD‐LSTM) : Universal deep sequence models for protein classification. [https://academic.oup.com/bioinformatics/article/36/8/2401/5698270](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)
6.  UniRep (mLSTM) : Unified rational protein engineering with sequence-based deep representation learning. [https://www.nature.com/articles/s41592-019-0598-1](https://www.kaggle.com/competitions/cafa-5-protein-function-prediction/discussion/url)


## What is Gene Onthology (GO)

Gene Ontology (GO) is a widely used resource in bioinformatics that provides structured and standardized descriptions of genes and their associated biological functions, cellular components, and molecular processes. It serves as a controlled vocabulary to annotate and characterize genes and gene products across different organisms.

The Gene Ontology Consortium develops and maintains GO, and it consists of three main categories or branches:

| Categories or Branches | Abstruct |
|:---:|---|
|**Biological Process (BP)**|This branch describes the series of events or activities that occur within a cell or an organism, contributing to a specific biological function. <br>Examples of biological processes include cell division, metabolism, signal transduction, and immune response.|
|**Cellular Component (CC)**|This branch represents the subcellular structures, locations, and complexes where gene products are active or present.<br> Examples of cellular components include the nucleus, mitochondria, cytoskeleton, and plasma membrane.|
|**Molecular Function (MF)**|This branch describes the specific biochemical activities or properties of gene products, such as catalytic or binding activities.<br> Examples of molecular functions include enzyme activity, receptor binding, DNA binding, and transporter activity.|

The GO terms are organized in a hierarchical structure, with broader terms at the top and more specific terms at the lower levels. This hierarchical structure allows for the representation of relationships between different terms. Additionally, each term is assigned a unique identifier, allowing researchers to refer to specific terms in their analyses.

Gene Ontology analysis involves the systematic examination of gene lists or expression data to uncover functional annotations, biological themes, and relationships within the data. It helps researchers make sense of large-scale genomic or transcriptomic datasets and gain insights into the underlying biology.
