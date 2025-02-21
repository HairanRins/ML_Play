import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

data = pd.read_csv('../data/boston_housing.csv')

# Séparer les caractéristiques (X) et la variable cible (y)
X = data.drop('PRICE', axis=1)
y = data['PRICE']

# Diviser les données en ensembles d'entraînement et de test (80% entraînement, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisation des caractéristiques
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Sauvegarder les données prétraitées
np.save('../data/X_train_scaled.npy', X_train_scaled)
np.save('../data/X_test_scaled.npy', X_test_scaled)
np.save('../data/y_train.npy', y_train.values)
np.save('../data/y_test.npy', y_test.values)