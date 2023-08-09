import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

# Load the generated dataset from the CSV file
data_frame = pd.read_csv("generated_data.csv")

# Preprocess categorical features to numerical
data_frame['Workload_Intensity_Num'] = data_frame['Workload_Intensity'].map({'Low': 0, 'Moderate': 1, 'High': 2})
data_frame['Network_Traffic_Num'] = data_frame['Network_Traffic'].str.extract('(\d+)').astype(float)

# Select the features for analysis
features = [
    'CPU_Utilization', 'Memory_Usage', 'Power_Consumption',
    'CPU_Temperature', 'Workload_Intensity_Num', 'Network_Traffic_Num'
]

# Step 1: Outlier Detection using Isolation Forest
outlier_detector = IsolationForest(contamination=0.05)
data_frame['outlier'] = outlier_detector.fit_predict(data_frame[features])

# Plot outlier graphs for each feature
for feature in features:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data_frame, x='Timestamp', y=feature, hue='outlier', palette={1: 'blue', -1: 'red'})
    plt.title(f'Outliers in {feature}')
    plt.xlabel('Timestamp')
    plt.ylabel(feature)
    plt.legend(['Inliers', 'Outliers'])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Rest of the code for finding max CPU utilization nodes and saving results
# ...








# Rest of the code for finding max CPU utilization nodes and saving results
# ...
#This code ensures that the 'Network_Traffic' column is included when applying the Isolation Forest algorithm and creating the outlier graphs.




# Rest of the code for finding max CPU utilization nodes and saving results
# ...
#In this code, the "Network_Traffic" feature is preprocessed to extract the numeric values using a regular expression. The extracted numeric values are then converted to float. This numeric version of the feature is included in the Isolation Forest outlier detection process.


# Step 2: Find Nodes with Maximum CPU Utilization at Different Time Stamps
max_cpu_nodes = data_frame[data_frame['CPU_Utilization'] == data_frame.groupby('Timestamp')['CPU_Utilization'].transform('max')]

# Step 3: Save Results to a Separate CSV File
results = pd.DataFrame(columns=['Timestamp', 'Max_CPU_Utilization_Node', 'Max_CPU_Utilization_Value'])
for timestamp, node_id, cpu_utilization in zip(max_cpu_nodes['Timestamp'], max_cpu_nodes['Node_ID'], max_cpu_nodes['CPU_Utilization']):
    results = results.append({'Timestamp': timestamp, 'Max_CPU_Utilization_Node': node_id, 'Max_CPU_Utilization_Value': cpu_utilization}, ignore_index=True)

results.to_csv("outliers_max_cpu_utilization.csv", index=False)
print("Results saved to 'outliers_max_cpu_utilization.csv'")
