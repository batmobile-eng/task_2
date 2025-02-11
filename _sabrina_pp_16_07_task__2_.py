# -*- coding: utf-8 -*-
"""_sabrina_pp_16-07_TASK _2 .ipynb



Original file is located at
    https://colab.research.google.com/drive/1s2pidbzxLP2bTz4X4u0VNEMD8h0LSv3h

Task: Basic Resource Allocation for Small Construction Projects
Objective
Create a Python-based system that tracks the allocation of resources (materials and labor) for small-scale
construction projects. The system will help track resources required for tasks, monitor usage, and ensure
that no resource is over or under-utilized.

Tasks


4. Visualization
o Create bar charts to visualize how much of each resource is being used by each task.
o Display a pie chart showing the distribution of resources across different tasks.

##1.Data Import
o Import resource allocation data from a CSV file.
o Ensure all required fields are filled.
"""

import csv

# Define the header row
header = ['ID', 'Project_ID', 'Task_ID', 'Resource_Type', 'Resource_Name', 'Amount_Required', 'Amount_Used', 'Start_Date', 'End_Date']

# Create and write to the CSV file
with open('resource_allocation.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

print("CSV file 'resource_allocation.csv' created with header.")

"""/content/drive/MyDrive/Python _iict/task_2_Sabrina_Afrin_Resource_Allocation_for_Small_Construction_Projects.csv"""

import csv

# Dataset file path
dataset_file_path = '/content/drive/MyDrive/Python _iict/task_2_Sabrina_Afrin_Resource_Allocation_for_Small_Construction_Projects.csv'

# CSV file path
csv_file_path = 'resource_allocation.csv'

# Read data from the dataset file
with open(dataset_file_path, 'r') as dataset_file:
    reader = csv.reader(dataset_file)
    # Skip the header row in the dataset file if it has one
    next(reader, None)
    dataset_data = list(reader)

# Append data to the CSV file
with open(csv_file_path, 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(dataset_data)

print(f"Data from '{dataset_file_path}' imported into '{csv_file_path}'.")

"""##2.Track Resource Usage
o Monitor how much of each resource is required and how much has been used.
o Track which task is using which resource.
"""

import csv

def track_resource_usage(csv_file_path):
    """
    Tracks resource usage from a CSV file.

    Args:
    csv_file_path (str): The path to the CSV file containing resource allocation data.

    Returns:
    dict: A dictionary containing resource usage information.
    """

    resource_usage = {}

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            task_id = row['Task_ID']
            resource_name = row['Resource_Name']
            amount_required = int(row['Amount_Required'])  # Convert to integer
            amount_used = int(row['Amount_Used'])  # Convert to integer

            # Update resource usage for the task
            if task_id not in resource_usage:
                resource_usage[task_id] = {}
            resource_usage[task_id][resource_name] = {
                'required': amount_required,
                'used': amount_used
            }

    return resource_usage

# Example usage
csv_file_path = 'resource_allocation.csv'  # Replace with your CSV file path
resource_usage_data = track_resource_usage(csv_file_path)

# Print the resource usage information
for task_id, resources in resource_usage_data.items():
    print(f"Task ID: {task_id}")
    for resource_name, usage in resources.items():
        print(f"  Resource: {resource_name}, Required: {usage['required']}, Used: {usage['used']}")

"""##3. Efficiency Monitoring
o Compare the required amount of resource vs. the actual usage.
o Identify tasks that might be under or over-utilizing resources.
"""

import csv

def track_resource_usage(csv_file_path):
    """
    Tracks resource usage from a CSV file.

    Args:
    csv_file_path (str): The path to the CSV file containing resource allocation data.

    Returns:
    dict: A dictionary containing resource usage information.
    """

    resource_usage = {}

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            task_id = row['Task_ID']
            resource_name = row['Resource_Name']
            amount_required = int(row['Amount_Required'])  # Convert to integer
            amount_used = int(row['Amount_Used'])  # Convert to integer

            # Update resource usage for the task
            if task_id not in resource_usage:
                resource_usage[task_id] = {}
            resource_usage[task_id][resource_name] = {
                'required': amount_required,
                'used': amount_used
            }

    return resource_usage


def monitor_efficiency(resource_usage_data):
    """
    Monitors resource efficiency and identifies under/over utilization.

    Args:
    resource_usage_data (dict): Resource usage data from track_resource_usage.
    """

    for task_id, resources in resource_usage_data.items():
        print(f"Task ID: {task_id}")
        for resource_name, usage in resources.items():
            required = usage['required']
            used = usage['used']

            if used < required * 0.8:  # Threshold for under-utilization (80%)
                print(f"  Resource: {resource_name} - Under-utilized (Used: {used}, Required: {required})")
            elif used > required * 1.2:  # Threshold for over-utilization (120%)
                print(f"  Resource: {resource_name} - Over-utilized (Used: {used}, Required: {required})")
            else:
                print(f"  Resource: {resource_name} - Efficiently utilized (Used: {used}, Required: {required})")

# Example usage
csv_file_path = 'resource_allocation.csv'  # Replace with your CSV file path
resource_usage_data = track_resource_usage(csv_file_path)
monitor_efficiency(resource_usage_data)

"""##4.Visualization
o Create bar charts to visualize how much of each resource is being used by each task.
o Display a pie chart showing the distribution of resources across different tasks.
"""

import csv
import matplotlib.pyplot as plt

# ... (previous code for track_resource_usage and monitor_efficiency) ...

def visualize_resource_usage(resource_usage_data):
    """
    Visualizes resource usage using bar charts and pie charts.

    Args:
    resource_usage_data (dict): Resource usage data from track_resource_usage.
    """

    # Get all unique resources across all tasks
    all_resources = set()
    for task_resources in resource_usage_data.values():
        all_resources.update(task_resources.keys())
    all_resources = list(all_resources)

    # Bar chart for resource usage by task
    tasks = list(resource_usage_data.keys())
    resource_usage_values = []
    for task in tasks:
        task_resource_usage = []
        for resource in all_resources:
            # Use get() to handle missing resources, defaulting to 0
            used_amount = resource_usage_data.get(task, {}).get(resource, {}).get('used', 0)
            task_resource_usage.append(used_amount)
        resource_usage_values.append(task_resource_usage)

    plt.figure(figsize=(10, 6))
    bottom = [0] * len(tasks)  # Initialize bottom for stacked bars
    for i, resource in enumerate(all_resources):
        plt.bar(tasks, [row[i] for row in resource_usage_values], bottom=bottom, label=resource)
        bottom = [bottom[j] + resource_usage_values[j][i] for j in range(len(bottom))]

    plt.xlabel("Task ID")
    plt.ylabel("Resource Usage")
    plt.title("Resource Usage by Task")
    plt.legend()
    plt.show()

    # Pie chart for resource distribution across tasks
    total_resource_usage = {resource: sum(resource_usage_data.get(task, {}).get(resource, {}).get('used', 0) for task in tasks) for resource in all_resources}
    resource_labels = list(total_resource_usage.keys())
    resource_values = list(total_resource_usage.values())

    plt.figure(figsize=(8, 8))
    plt.pie(resource_values, labels=resource_labels, autopct='%1.1f%%', startangle=90)
    plt.title("Resource Distribution Across Tasks")
    plt.show()

# Example usage
csv_file_path = 'resource_allocation.csv'  # Replace with your CSV file path
resource_usage_data = track_resource_usage(csv_file_path)
visualize_resource_usage(resource_usage_data)
