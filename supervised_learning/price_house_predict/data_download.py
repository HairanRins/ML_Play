import pandas as pd
import numpy as np

# URL du dataset
data_url = "http://lib.stat.cmu.edu/datasets/boston"

# Lire les données brutes
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# Créer un DataFrame Pandas
column_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
boston = pd.DataFrame(data, columns=column_names)
boston['PRICE'] = target

# Sauvegarder le dataset en CSV (facultatif)
boston.to_csv('./data/boston_housing.csv', index=False)