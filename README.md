# Resource Allocation for Small Construction Projects

## Introduction

This project aims to develop a Python-based system for tracking resource allocation in small-scale construction projects. It helps monitor resource usage, ensures efficient allocation, and provides visualizations for better insights.

## Features

* **Data Import:** Imports resource allocation data from a CSV file.
* **Resource Tracking:** Monitors resource requirements and actual usage for each task.
* **Efficiency Monitoring:** Identifies tasks that might be under or over-utilizing resources.
* **Visualization:**
    * Bar charts to visualize resource usage by each task.
      ![Image](https://github.com/user-attachments/assets/9ab90310-bd58-4dcf-b2c3-686d224cbf85)

    * Pie chart to show the distribution of resources across tasks.
     ![Image](https://github.com/user-attachments/assets/97d78dc6-438a-4ecf-a5ac-259ca1b8e43e)

## Usage

1. **Data Preparation:** Create a CSV file named `resource_allocation.csv` with the following header:
   `ID, Project_ID, Task_ID, Resource_Type, Resource_Name, Amount_Required, Amount_Used, Start_Date, End_Date`
2. **Import Data:** Run the data import section to populate the `resource_allocation.csv` file.
3. **Track Resource Usage:** Execute the `track_resource_usage` function to analyze resource usage patterns.
4. **Monitor Efficiency:** Use the `monitor_efficiency` function to identify potential under or over-utilization of resources.
5. **Visualization:** Call the `visualize_resource_usage` function to generate bar charts and pie charts for visual insights.

## Benefits

* **Improved Resource Management:** Provides a centralized system for tracking resource allocation.
* **Enhanced Efficiency:** Helps identify and address resource under or over-utilization.
* **Better Project Planning:** Facilitates informed decision-making for future projects.
* **Reduced Costs:** Optimizes resource usage to minimize wastage and unnecessary expenses.

## Conclusion

This resource allocation system provides a valuable tool for managing resources in small construction projects. By effectively tracking usage and identifying potential inefficiencies, it contributes to better project planning and execution.

## Future Enhancements

* Integrate with project management software for seamless data exchange.
* Implement real-time data updates for dynamic monitoring.
* Develop predictive models to forecast resource needs.
* Add a user interface for easier interaction and data input.
