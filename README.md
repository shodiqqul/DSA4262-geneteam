
## DSA4262: Identification of RNA modifications from direct RNA-Seq data
![alt text](https://github.com/shodiqqul/DSA4262-geneteam/blob/85cca09e97f829192a3368d8539528f3041bcd5d/images/DSA4262%20Presentation.png)

m6A modifications is attributed to physiological processes like stem cell differentiation, viral infection and cancer progression. 
We aim to develop a machine learning method that identifies m6A RNA modifications that may go as far as to allow detection of cancer.

### Running our Pipeline to predict with our model
If you would like to run our Pipeline and attain predictions, we have provided step-by-step instructions on how to run our pipeline [here.](https://github.com/shodiqqul/DSA4262-geneteam/tree/main/Pipeline)

**_Continue below for more details and documentation of our work._**

---
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

| XGBoost |Value |
| ---------|:-------------:|
| ROC AUC                 | 0.80 | 
| PR AUC (minority class) | 0.44 | 

| CatBoost with ADASYN |Value |
| ---------|:-------------:|
| ROC AUC                 | 0.78 | 
| PR AUC (minority class) | 0.33 | 

| CatBoost with Sample Weights |Value |
| ---------|:-------------:|
| ROC AUC                 | 0.79 | 
| PR AUC (minority class) | 0.36 | 

We proceeded with an XGBoost model.

#### Running our XGBoost model with SG-NEx data
We looked at:
- Proportion of m6A detected
- Probability of modification for each transcript
- Comparison of probabilities of different transcripts across different cancer types

To view our interactive Tableau dashboard, click [here!](https://public.tableau.com/app/profile/gene.team/viz/shared/78BZKPMTP)

---
### Authors
Group GeneTeam:
- AHMAD AS-SHODIQQUL AMIN B M T
- DIONE LIM YEE SZE
- KEITH TAY XIANG RUI
- MADHU BHARATHI ELANGO


A special thanks to Professor Jonathan Göke, Christopher Hendra and Yuk Kei Wan

---
### References

[1]: Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.

[2]: Hashing. Hashing - Category Encoders 2.5.1.post0 documentation. (n.d.). Retrieved October 26, 2022, from https://contrib.scikit-learn.org/category_encoders/hashing.html

[3]: Akalin, A. (2020, September 30). Computational genomics with R. 5.10 How to deal with class imbalance. Retrieved October 26, 2022, from https://compgenomr.github.io/book/how-to-deal-with-class-imbalance.html

[4]: Jain, A. (2022, June 15). XGBOOST parameters: XGBoost parameter tuning. Analytics Vidhya. Retrieved November 3, 2022, from https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/
