import numpy as np
import pandas as pd
import xgboost as xgb
import imblearn.over_sampling as res

# Import feature engineered training data 
data = pd.read_csv("./data/featureEngineered_data.csv")

columns_needed = ['col_0', 'col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8', 'col_9', 'col_10', 'col_11', 'col_12', 'col_13', 'col_14', 'col_15', 'col_16', 'col_17', 'col_18', 'col_19', 'col_20', 'col_21', 'col_22', 'col_23', 'col_24', 'col_25', 'col_26', 'col_27', 'col_28', 'col_29', 'dwelling_1', 'sd_1', 'mean_1', 'dwelling_2', 'sd_2', 'mean_2', 'dwelling_3', 'sd_3', 'mean_3']

# Get x and y
x_train = data[columns_needed]
y_train = data[["label"]]

# Resampling
adasyn = res.ADASYN(random_state=4262)
x_train, y_train = adasyn.fit_resample(x_train, y_train)

# XGBoost
model_xgb = xgb.XGBClassifier(
    colsample_bytree=0.7,
    learning_rate=0.05,
    max_depth=7,
    min_child_weight=5,
    missing=-999,
    nthread=4, 
    n_estimators=100,
    objective='binary:logistic',
    seed=4262,
    silent=1,
    subsample=0.8)

# Train model
model_xgb.fit(x_train, y_train, verbose=True)

# Save model as .ubj file
model_xgb.save_model('model_xgb.ubj')
