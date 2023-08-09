import pandas as pd
from sklearn.ensemble import IsolationForest

# Load the generated dataset from the CSV file
data_frame = pd.read_csv("generated_data.csv")

# Select the features for outlier detection
features = [
    'CPU_Utilization', 'Memory_Usage', 'Number_of_Requests',
    'CPU_Temperature', 'Power_Consumption', 'Clock_Speed', 'Cache_Size', 'Number_of_Cores'
]

# Initialize the Isolation Forest model
outlier_detector = IsolationForest(contamination=0.05, random_state=42)

# Fit the model to the features
outlier_detector.fit(data_frame[features])

# Predict outliers using -1 for outliers and 1 for inliers
data_frame['outlier'] = outlier_detector.predict(data_frame[features])

# Display the rows identified as outliers
outliers = data_frame[data_frame['outlier'] == -1]
print("Detected Outliers:")
print(outliers)

# Plot the outliers
import matplotlib.pyplot as plt

for feature in features:
    plt.figure(figsize=(10, 6))
    plt.scatter(data_frame.index, data_frame[feature], c=data_frame['outlier'], cmap='viridis')
    plt.xlabel('Index')
    plt.ylabel(feature)
    plt.title(f'{feature} Outliers')
    plt.colorbar()
    plt.show()
