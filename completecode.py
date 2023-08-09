import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the dataset
data_frame = pd.read_csv("generated_data.csv")

# Display first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(data_frame.head())

# Display information about data types and non-null values
print("\nInformation about data types and non-null values:")
print(data_frame.info())

# Summary statistics for numerical columns
print("\nSummary statistics for numerical columns:")
print(data_frame.describe())

# Check unique values in categorical columns
print("\nUnique values in 'Node_ID':", data_frame['Node_ID'].unique())

# Visualize the distribution of 'CPU_Utilization'
plt.figure(figsize=(8, 6))
sns.histplot(data_frame['CPU_Utilization'], bins=20, kde=True)
plt.title("Distribution of CPU Utilization")
plt.xlabel("CPU Utilization")
plt.ylabel("Frequency")
plt.show()

# Visualize relationships between features using pairplot
numerical_features = ['CPU_Utilization', 'Memory_Usage', 'Power_Consumption', 'CPU_Temperature',"Storage_Utilization","Number_of_Requests"]
plt.figure(figsize=(10, 8))
sns.pairplot(data_frame[numerical_features])
plt.suptitle("Pairwise Relationships between Numerical Features")
plt.show()

# Check for missing values
missing_values = data_frame.isnull().sum()
print("\nMissing values count:")
print(missing_values)

# Visualize box plots for numerical features to identify outliers
plt.figure(figsize=(12, 8))
sns.boxplot(data=data_frame[numerical_features])
plt.title("Box Plots of Numerical Features")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.show()

# Check for duplicated rows
duplicated_rows = data_frame.duplicated()
print("\nNumber of duplicated rows:", duplicated_rows.sum())

# Perform dimensionality reduction using PCA for visualization
features = ['CPU_Utilization', 'Memory_Usage', 'Power_Consumption', 'CPU_Temperature','Storage_Utilization','Number_of_Requests']
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_frame[features])
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

# Visualize data in reduced dimensions using scatter plot
plt.figure(figsize=(10, 8))
sns.scatterplot(x=data_pca[:, 0], y=data_pca[:, 1])
plt.title("PCA Scatter Plot")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.show()
