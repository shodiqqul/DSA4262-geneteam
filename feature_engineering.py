import numpy as np
import pandas as pd
import category_encoders.hashing as ce

# Import merged data
data = pd.read_csv("./data/merged_data.csv")

# Kmerisation
def get_kmers(read, k):
    lst_kmers = []
    # Calculate how many kmers of length k there are
    num_kmers = len(read) - k + 1
    # Loop over the kmer start positions
    for i in range(num_kmers):
        # Slice the string to get the kmer
        kmer = read[i:i+k]
        lst_kmers.append(kmer)
    return lst_kmers
  
def slice_kmers(lst):
  # Create list of lists
  kmers_cols = [[] for i in range(len(lst[0]))]
  # Slice j-th kmer from i-th row and put them together
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      kmers_cols[j].append(lst[i][j])
  return kmers_cols

def kmers_to_df(cols, col_names, df):
  # Add new kmers columns to dataframe
  for i in range(len(cols)):
    df[col_names[i]] = cols[i]
  
  # Drop Sequence column
  df = df.drop("Sequence", axis=1)
  return df

kmers_cols_names = ["k_1", "k_2", "k_3", "k_4", "k_5"] # varies according to value of k, manually update

data_kmers_all = []
for seq in data["Sequence"]:
    data_kmers = get_kmers(seq, 3)
    data_kmers_all.append(data_kmers)

data_kmers_cols = slice_kmers(data_kmers_all)
data_kmerised = kmers_to_df(data_kmers_cols, kmers_cols_names, data)

# Hash Encoding
if __name__ == '__main__':
    he = ce.HashingEncoder(cols=kmers_cols_names, n_components=30)
    he.fit(data_kmerised)
    data_kmerised_encoded = he.transform(data_kmerised)
  
    data_kmerised_encoded.to_csv("./data/featureEngineered_data.csv")
