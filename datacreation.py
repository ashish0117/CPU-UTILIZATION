# Author: Ashish Verma
# Email Id: avermase@gmail.com

'''
Below program can generate sample dataset (in csv) for CPU utlilization with other parameters of Cloud Computing Nodes.
Parameters are
"Timestamp", "Node_ID", "Application", "CPU_Utilization", "Memory_Usage", "Workload_Intensity", "Network_Traffic",
"Storage_Utilization", "Number_of_Requests", "CPU_Temperature", "Power_Consumption", "Clock_Speed", "Cache_Size", "Number_of_Cores"
'''

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Generate random timestamps within a range
start_time = datetime(2023, 8, 9, 8, 0, 0)
end_time = datetime(2023, 8, 9, 18, 0, 0)
time_range = end_time - start_time
timestamps = [start_time + timedelta(seconds=random.randint(0, time_range.seconds)) for _ in range(1000)]

# Generate random data for the parameters
nodes = ["Node_" + str(i) for i in range(1, 6)]
applications = ["Web Server", "Database", "Analytics", "AI Inference", "File Server"]
workload_intensities = ["Low", "Moderate", "High"]
network_traffics = ["20 Mbps", "50 Mbps", "100 Mbps", "150 Mbps", "200 Mbps"]
storage_utilizations = ["40%", "60%", "70%", "80%", "90%"]

data = []

for _ in range(1000):
    node = random.choice(nodes)
    app = random.choice(applications)
    cpu_utilization = random.uniform(10, 90)
    memory_usage = random.uniform(30, 90)
    workload_intensity = random.choice(workload_intensities)
    network_traffic = random.choice(network_traffics)
    storage_utilization = random.choice(storage_utilizations)
    num_requests = random.randint(200, 2000)
    cpu_temperature = random.uniform(40, 80)
    power_consumption = random.uniform(150, 350)
    clock_speed = round(random.uniform(2.0, 3.5), 2)
    cache_size = random.choice([6, 8, 12, 16, 20])
    num_cores = random.choice([2, 4, 6, 8, 10])

    data.append([
        random.choice(timestamps),
        node, app, cpu_utilization, memory_usage, workload_intensity,
        network_traffic, storage_utilization, num_requests,
        cpu_temperature, power_consumption, clock_speed, cache_size, num_cores
    ])

columns = [
    "Timestamp", "Node_ID", "Application", "CPU_Utilization",
    "Memory_Usage", "Workload_Intensity", "Network_Traffic",
    "Storage_Utilization", "Number_of_Requests", "CPU_Temperature",
    "Power_Consumption", "Clock_Speed", "Cache_Size", "Number_of_Cores"
]

data_frame = pd.DataFrame(data, columns=columns)

data_frame.to_csv("generated_data.csv", index=False)
