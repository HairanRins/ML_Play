import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score 
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('../data/Mall_Customers.csv') 

X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters_dbscan = dbscan.fit_predict(X_scaled)

# Calculer le score de silhouette (si applicable)
if len(set(clusters_dbscan))  > 1:  # Vérifier si plus d'un cluster a été trouvé
    silhouette_avg_dbscan = silhouette_score(X_scaled, clusters_dbscan)
    print(f"Score de Silhouette (DBSCAN): {silhouette_avg_dbscan:.2f}")
else:
    print("DBSCAN n'a pas pu trouver plusieurs clusters.")

plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters_dbscan, cmap='viridis', s=50)
plt.title('Clustering DBSCAN')
plt.savefig('../results/dbscan_clusters.png')  
plt.show()

# Score de Silhouette (DBSCAN): 0.35 