# Importer les bibliothèques nécessaires
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le dataset Boston Housing depuis un fichier CSV local
data = pd.read_csv('../data/boston_housing.csv')

# Statistiques descriptives
print(data.describe())

# Corrélation entre les variables
correlation_matrix = data.corr()

# Sauvegarder la matrice de corrélation
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matrice de Corrélation')
plt.savefig('../results/correlation_matrix.png', dpi=300)
plt.show()