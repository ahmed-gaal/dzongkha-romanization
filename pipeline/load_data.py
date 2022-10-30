"""
@author: AHmed Ga'al
Data collection script
"""
import os
import gdown
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from params import Params

# Generating random seed
ran_s = Params.random_state

# Generate paths to store data extracted from remote source
Params.original.parent.mkdir(parents=True, exist_ok=True)
Params.data.mkdir(parents=True, exist_ok=True)

# Extract data from remote source
gdown.download(
    os.environ.get("DATA"),
    str(Params.original)
)

# Loading data extracted from remote source  in pandas DataFrame
df = pd.read_csv(str(Params.original))

# Set column names for the data
df.columns = ['english', 'dzongkha']

# Remove spaces in dzongkha sentences
df['dzongkha'] = df['dzongkha'].replace(" ", "")

# Split our data to train and test sets
df_train, df_test = train_test_split(
    df, test_size=0.1, shuffle=True, random_state=ran_s
)

df_train.to_csv(str(Params.data / 'train.csv'), index=None)
df_test.to_csv(str(Params.data / 'test.csv'), index=None)
