import sys
import json
import numpy as np
import pandas as pd
import xgboost as xgb
import category_encoders.hashing as ce

def data_preprocessing(filename): 
  data_csv = pd.read_csv("./data/data.csv")

  new = []
  for line in open(filename, 'r'):
    new += [line[:-1]]

  feature = []
  for x in new:
    x = json.loads(x)
    transcriptid = list(x.keys())[0]
    nested = x[transcriptid]
    position = list(nested.keys())[0]
    nested = nested[position]
    sequence = list(nested.keys())[0]
    nested = nested[sequence]
    nested = list(zip(*nested))
    features = [np.mean(x) for x in nested]
    features = [transcriptid, position, sequence] + features
    feature += [features]

  feature = pd.DataFrame(feature, columns = ["transcript_id", "transcript_position", "Sequence", "dwelling_1", "sd_1", "mean_1", "dwelling_2", "sd_2", "mean_2", "dwelling_3", "sd_3", "mean_3"])
  feature['transcript_position'] = feature['transcript_position'].astype('int')
  test_data = pd.merge(data_csv, feature, on = ["transcript_id", "transcript_position"])
  return(test_data)

def feature_engineering(test_data):
  """ Kmerisation """
  def get_kmers(read, k):
    lst_kmers = []
    num_kmers = len(read) - k + 1
    for i in range(num_kmers):
        kmer = read[i:i+k]
        lst_kmers.append(kmer)
    return lst_kmers
  
  def slice_kmers(lst):
    kmers_cols = [[] for i in range(len(lst[0]))]
    for i in range(len(lst)):
      for j in range(len(lst[0])):
        kmers_cols[j].append(lst[i][j])
    return kmers_cols

  def kmers_to_df(cols, col_names, df):
    for i in range(len(cols)):
      df[col_names[i]] = cols[i]
  
    df = df.drop("Sequence", axis=1)
    return df

  kmers_cols_names = ["k_1", "k_2", "k_3", "k_4", "k_5"] # varies according to value of k, manually update

  data_kmers_all = []
  for seq in test_data["Sequence"]:
    data_kmers = get_kmers(seq, 3)
    data_kmers_all.append(data_kmers)

  data_kmers_cols = slice_kmers(data_kmers_all)
  data_kmerised = kmers_to_df(data_kmers_cols, kmers_cols_names, test_data)

  """ Hash Encoding """
  he = ce.HashingEncoder(cols=kmers_cols_names, n_components=30)
  he.fit(data_kmerised)
  data_kmerised_encoded = he.transform(data_kmerised)
  return(data_kmerised_encoded)

def main(data_kmerised_encoded):
  """ Load Model """
  filename = 'model_xgb.ubj'
  model_xgb = xgb.XGBClassifier()
  model_xgb.load_model(filename)

  """ Run Model """
  columns_needed = ['col_0', 'col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8', 'col_9', 'col_10', 'col_11', 'col_12', 'col_13', 'col_14', 'col_15', 'col_16', 'col_17', 'col_18', 'col_19', 'col_20', 'col_21', 'col_22', 'col_23', 'col_24', 'col_25', 'col_26', 'col_27', 'col_28', 'col_29', 'dwelling_1', 'sd_1', 'mean_1', 'dwelling_2', 'sd_2', 'mean_2', 'dwelling_3', 'sd_3', 'mean_3']
  x_train = data_kmerised_encoded[columns_needed]

  y_pred_proba = model_xgb.predict_proba(x_train)

  results = pd.DataFrame()
  results["transcript_id"] = data_kmerised_encoded["transcript_id"]
  results["transcript_position"] = data_kmerised_encoded["transcript_position"]
  results["score"] = pd.DataFrame(y_pred_proba[:,1], columns=['score'])
  return(results)

if __name__ == '__main__':
  test_data_filename = sys.argv[1]
  test_data = data_preprocessing(test_data_filename)
  test_data_featureEngineered = feature_engineering(test_data)
  results = main(test_data_featureEngineered)
  results.to_csv("./results/results.csv", index=False)
  print("Done!")