## DSA4262: Identification of RNA modifications from direct RNA-Seq data
m6A modifications is attributed to physiological processes like stem cell differentiation, viral infection and cancer progression. We aim to develop a machine learning method that identifies m6A RNA modifications that may go as far as to allow detection of cancer.

### Running our Pipeline to predict with our model
If you would like to run our Pipeline and attain predictions, we have provided step-by-step instructions on how to run our pipeline [here.](https://github.com/shodiqqul/DSA4262-geneteam/tree/main/Pipeline)

**_Continue below for more details and documentation of our work._**

#### Data Preprocessing
The mean of the reads were taken for each gene and transcription ID.

#### Feature Engineering

1. Kmerisation
To extract information while preserving sequences, we k-merised the sequence of 7 into 3-mers.

2. Hash Encoding
Due to the high cardinality nature of sequences and k-mers, we encoded the 3-mers into numeric via Hash Encoding as well as facilitating our use of XGBoost.

#### Handling Imbalanced Dataset

There was an imbalance in the dataset as observations with ```class label: 1``` is not equivalent to ```class label: 0```. We explored different methods to overcome this.
Methods tried:
- Sample weights
- Synthetic Minority Oversampling TEchnique (SMOTE) 
- ADaptive SYNthetic Technique (ADASYN)

#### Models
1. XGBoost:
- ROC AUC: **0.80**
- PR AUC (minority class): **0.44**

2. CatBoost:
With ADASYN:
- ROC AUC: **0.78**
- PR AUC: **0.33**

With Sample Weights:
- ROC AUC: **0.79**
- PR AUC: **0.36**

#### Running our XGBoost model with SG-NEx data
We looked at:
- Proportion of m6A detected
- Probability of modification for each transcript
- Comparison of probabilities of different transcripts across different cancer types


### Authors
Group GeneTeam:
- AHMAD AS-SHODIQQUL AMIN B M T
- DIONE LIM YEE SZE
- KEITH TAY XIANG RUI
- MADHU BHARATHI ELANGO
