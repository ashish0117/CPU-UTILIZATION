import pandas as pd
import matplotlib.pyplot as plt

# Load the data for nodes liable for failure from the CSV file
failed_nodes_data = pd.read_csv("failed_nodes_data.csv")

# Select the monitoring features for analysis
monitoring_features = [
    'CPU_Utilization', 'Memory_Usage', 'Power_Consumption',
    'CPU_Temperature', 'Workload_Intensity', 'Network_Traffic',
    'Number_of_Requests', 'Cache_Size'
    #, 'Disk_Usage', 'Response_Time'
]

# Standardize the monitoring features by calculating z-scores
z_scores = (failed_nodes_data[monitoring_features] - failed_nodes_data[monitoring_features].mean()) / failed_nodes_data[monitoring_features].std()

# Calculate an overall score for each node based on z-scores
failed_nodes_data['Overall_Score'] = z_scores.sum(axis=1)

# Rank nodes based on the overall score
ranked_nodes = failed_nodes_data.sort_values(by='Overall_Score', ascending=False)

# Plot the overall scores for the nodes
plt.figure(figsize=(10, 6))
plt.bar(ranked_nodes['Node_ID'], ranked_nodes['Overall_Score'])
plt.xlabel('Node')
plt.ylabel('Overall Score')
plt.title('Overall Scores for Nodes Liable for Failure')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()