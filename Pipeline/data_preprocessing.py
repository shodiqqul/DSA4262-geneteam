import sys
import json
import pathlib
import numpy as np
import pandas as pd

# Get input filepaths
data_info_path = sys.argv[1]
data_json_path = sys.argv[2]

# Convert data.info to .csv
p = pathlib.Path(data_info_path)
p.rename(p.with_suffix('.csv'))

# Import data.csv
new_path = p.parent / (p.name + '.csv')

# Import training_data.json
new = []
for line in open(data_json_path, 'r'):
  new += [line[:-1]]

# Feature dataframe with average of reads
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

# Merge data.csv with training_data.json
merged_data = pd.merge(data_csv, feature, on = ["transcript_id", "transcript_position"])
merged_data.to_csv("./data/merged_data.csv")
