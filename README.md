## DSA4262: Identification of RNA modifications from direct RNA-Seq data

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

To view our interactive Tableu dashboard, click [here!](https://public.tableau.com/app/profile/gene.team/viz/shared/78BZKPMTP)

---
### Authors
Group GeneTeam:
- AHMAD AS-SHODIQQUL AMIN B M T
- DIONE LIM YEE SZE
- KEITH TAY XIANG RUI
- MADHU BHARATHI ELANGO

---
### References

[1]:  Zhang, W., Qian, Y., & Jia, G. (2021, August). The detection and functions of RNA modification M6a based on M6a writers and Erasers. The Journal of biological chemistry. Retrieved October 26, 2022, from https://doi.org/10.1016%2Fj.jbc.2021.100973

[2]: Gao, R., Ye, M., Liu, B., Wei, M., Ma, D., & Dong, K. (1AD, January 1). M6A modification: A double-edged sword in tumor development. Frontiers. Retrieved October 26, 2022, from https://doi.org/10.3389/fonc.2021.679367

[3]: Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.

[4]: Zou, Q., Xing, P., Wei, L., & Liu, B. (2019, February). Gene2vec: Gene subsequence embedding for prediction of mammalian n6-methyladenosine sites from mrna. RNA (New York, N.Y.). Retrieved October 26, 2022, from https://doi.org/10.1261%2Frna.069112.118

[5]: Hashing. Hashing - Category Encoders 2.5.1.post0 documentation. (n.d.). Retrieved October 26, 2022, from https://contrib.scikit-learn.org/category_encoders/hashing.html

[6]: Bonidia. (n.d.). Bonidia/Mathfeature: Feature extraction package for biological sequences. GitHub. Retrieved November 3, 2022, from https://github.com/Bonidia/MathFeature

[7]: Akalin, A. (2020, September 30). Computational genomics with R. 5.10 How to deal with class imbalance. Retrieved October 26, 2022, from https://compgenomr.github.io/book/how-to-deal-with-class-imbalance.html

[8]: Mishra, A. (2019). Machine learning in the AWS cloud: Add intelligence to applications with Amazon Sagemaker and Amazon Rekognition. Amazon. Retrieved October 26, 2022, from https://docs.aws.amazon.com/sagemaker/latest/dg/catboost-tuning.html

[9]: Jain, A. (2022, June 15). XGBOOST parameters: XGBoost parameter tuning. Analytics Vidhya. Retrieved November 3, 2022, from https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/
