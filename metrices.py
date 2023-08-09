'''
Metrics that are more relevant for evaluating unsupervised anomaly detection techniques include:

1. Silhouette Score: Measures how similar an object is to its own cluster (cohesion) compared to other clusters (separation). A higher silhouette score indicates better separation and cohesive clusters.
2. Davies-Bouldin Index: Measures the average similarity between each cluster and its most similar cluster. Lower values indicate better clustering.

These are used for KMeans, Hierarchical and for DBSCAN
'''



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.decomposition import PCA

# Load the generated dataset from the CSV file
data_frame = pd.read_csv("generated_data.csv")

# Select the features for analysis
features = ['CPU_Utilization', 'Memory_Usage', 'Power_Consumption', 'CPU_Temperature', 'Workload_Intensity', 'Network_Traffic']

# Preprocess categorical feature to numerical
data_frame['Workload_Intensity_Num'] = data_frame['Workload_Intensity'].map({'Low': 0, 'Moderate': 1, 'High': 2})

# Preprocess 'Network_Traffic' to extract numeric values
data_frame['Network_Traffic_Num'] = data_frame['Network_Traffic'].str.extract('(\d+)').astype(float)

# Remove the original categorical features
data_frame = data_frame.drop(columns=['Workload_Intensity', 'Network_Traffic'])

# Select the features for analysis
features = ['CPU_Utilization', 'Memory_Usage', 'Power_Consumption', 'CPU_Temperature', 'Network_Traffic_Num']

# Standardize features
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_frame[features])

# Perform dimensionality reduction using PCA for visualization
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

# Initialize clustering algorithms
kmeans = KMeans(n_clusters=3)
hierarchical = AgglomerativeClustering(n_clusters=3)
dbscan = DBSCAN(eps=0.5, min_samples=5)

# Fit and predict clusters
data_frame['KMeans_Cluster'] = kmeans.fit_predict(data_scaled)
data_frame['Hierarchical_Cluster'] = hierarchical.fit_predict(data_scaled)
data_frame['DBSCAN_Cluster'] = dbscan.fit_predict(data_scaled)

# Calculate silhouette score and Davies-Bouldin index
silhouette_kmeans = silhouette_score(data_scaled, data_frame['KMeans_Cluster'])
silhouette_hierarchical = silhouette_score(data_scaled, data_frame['Hierarchical_Cluster'])
silhouette_dbscan = silhouette_score(data_scaled, data_frame['DBSCAN_Cluster'])
davies_bouldin_kmeans = davies_bouldin_score(data_scaled, data_frame['KMeans_Cluster'])
davies_bouldin_hierarchical = davies_bouldin_score(data_scaled, data_frame['Hierarchical_Cluster'])
davies_bouldin_dbscan = davies_bouldin_score(data_scaled, data_frame['DBSCAN_Cluster'])

# Visualize clusters using PCA
plt.figure(figsize=(12, 6))
sns.scatterplot(x=data_pca[:, 0], y=data_pca[:, 1], hue=data_frame['KMeans_Cluster'], palette='viridis')
plt.title('KMeans Clustering')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x=data_pca[:, 0], y=data_pca[:, 1], hue=data_frame['Hierarchical_Cluster'], palette='viridis')
plt.title('Hierarchical Clustering')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x=data_pca[:, 0], y=data_pca[:, 1], hue=data_frame['DBSCAN_Cluster'], palette='viridis')
plt.title('DBSCAN Clustering')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()

print("Silhouette Scores:")
print("KMeans:", silhouette_kmeans)
print("Hierarchical:", silhouette_hierarchical)
print("DBSCAN:", silhouette_dbscan)
print("\nDavies-Bouldin Index:")
print("KMeans:", davies_bouldin_kmeans)
print("Hierarchical:", davies_bouldin_hierarchical)
print("DBSCAN:", davies_bouldin_dbscan)
