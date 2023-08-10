# CPU-UTILIZATION

1. datacreation.py:
This file is helpful to generate sample dataset (in csv) for CPU utlilization with other parameters of Cloud Computing Nodes.
Parameters are
"Timestamp", "Node_ID", "Application", "CPU_Utilization", "Memory_Usage", "Workload_Intensity", "Network_Traffic",
"Storage_Utilization", "Number_of_Requests", "CPU_Temperature", "Power_Consumption", "Clock_Speed", "Cache_Size", "Number_of_Cores"
Output will be file named generated_csv.csv

2. noderesponsibilityforfailure.py

This program select some features ('CPU_Utilization', 'Memory_Usage', 'Power_Consumption','CPU_Temperature', 'Workload_Intensity', 'Network_Traffic',
'Number_of_Requests', 'Cache_Size') with some threshold values ('CPU_Utilization': 80, 'Memory_Usage': 90, 'Power_Consumption': 300,
'CPU_Temperature': 75, 'Workload_Intensity': 'High',  # For categorical feature,  'Network_Traffic': '200 Mbps',  # For categorical feature
'Number_of_Requests': 1500, 'Cache_Size': 10,) and save nodes data which are liable for failure in csv file named failed_nodes_data.csv. It also plot the data for each monitoring feature.
   
3. failednodechecking.py
This program Standardize the monitoring features by calculating z-scores, calculate overall score for each node based on z-score, and rank them.

 
4. metrices.py
This program use Metrics that are more relevant for evaluating unsupervised anomaly detection techniques which include:

a. Silhouette Score: Measures how similar an object is to its own cluster (cohesion) compared to other clusters (separation). A higher silhouette score indicates better separation and cohesive clusters.
b. Davies-Bouldin Index: Measures the average similarity between each cluster and its most similar cluster. Lower values indicate better clustering.

These are used for KMeans, Hierarchical and for DBSCAN

5.  isolationforest.py
This program uses isolation forest for detecting outliers

6.  allsteps.py
This program is extension of isolation forest and saving outliers responsible for max cpu utilization is same named csv file.

7.  completecode.py
it is the basic program for visulalizing the data with dimensiionality reduction


  
  
