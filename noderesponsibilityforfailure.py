import pandas as pd

# Load the generated dataset from the CSV file
data_frame = pd.read_csv("generated_data.csv")

# Select the features for monitoring and set threshold values
monitoring_features = [
    'CPU_Utilization', 'Memory_Usage', 'Power_Consumption',
    'CPU_Temperature', 'Workload_Intensity', 'Network_Traffic',
    'Number_of_Requests', 'Cache_Size'
     #'Disk_Usage', 'Response_Time'
]

# Thresholds for each feature
thresholds = {
    'CPU_Utilization': 80,
    'Memory_Usage': 90,
    'Power_Consumption': 300,
    'CPU_Temperature': 75,
    'Workload_Intensity': 'High',  # For categorical feature
    'Network_Traffic': '200 Mbps',  # For categorical feature
    'Number_of_Requests': 1500,
    'Cache_Size': 10,
    # 'Disk_Usage': 85,
    # 'Response_Time': 500
}

# Create a new DataFrame to store data for nodes liable for failure
failed_nodes_data = pd.DataFrame(columns=data_frame.columns)

# Loop through each node and check if any parameter exceeds its threshold
for node_id in data_frame['Node_ID'].unique():
    node_data = data_frame[data_frame['Node_ID'] == node_id]
    node_failed = any(node_data.apply(lambda row: any(row[feature] >= thresholds[feature] if isinstance(row[feature], (int, float)) else row[feature] == thresholds[feature] for feature in monitoring_features), axis=1))
    
    if node_failed:
        failed_nodes_data = failed_nodes_data.append(node_data, ignore_index=True)

# Save data of nodes liable for failure to a CSV file
failed_nodes_data.to_csv("failed_nodes_data.csv", index=False)

print("Data for nodes liable for failure saved to 'failed_nodes_data.csv'")



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data for nodes liable for failure from the CSV file
failed_nodes_data = pd.read_csv("failed_nodes_data.csv")

# Select the monitoring features for visualization
monitoring_features = [
    'CPU_Utilization', 'Memory_Usage', 'Power_Consumption',
    'CPU_Temperature', 'Workload_Intensity', 'Network_Traffic',
    'Number_of_Requests', 'Cache_Size'
    #, 'Disk_Usage', 'Response_Time'
]

# Plotting the data for each monitoring feature
for feature in monitoring_features:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=failed_nodes_data, x='Node_ID', y=feature)
    plt.title(f'{feature} for Failed Nodes')
    plt.xlabel('Node')
    plt.ylabel(feature)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
