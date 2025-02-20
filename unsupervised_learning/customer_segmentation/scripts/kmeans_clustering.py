import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score 
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('../data/Mall_Customers.csv')

# Préparation des données 
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Méthode du coude pour déterminer le nombre optimal de clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1,11), wcss, marker='o')
plt.title('Méthode du Coude')
plt.xlabel('Nombre de Clusters')
plt.ylabel('WCSS')
plt.savefig('../results/elbow_method.png')  # Sauvegarder le graphique
plt.show()

# Appliquer K-Means avec k = 5 (d'après la méthode du coude)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
clusters_kmeans = kmeans.fit_predict(X_scaled)

# Calculer le score de silhouette
silhouette_avg_kmeans = silhouette_score(X_scaled, clusters_kmeans)
print(f"Score de Silhouette (K-Means): {silhouette_avg_kmeans:.2f}")   

# Visualisation des clusters K-Means 
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters_kmeans, cmap='viridis', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', label='Centroids')
plt.title('Clustering K-Means')
plt.legend()
plt.savefig('../results/kmeans_clusters.png')  
plt.show()

# Score de Silhouette (K-Means): 0.55 