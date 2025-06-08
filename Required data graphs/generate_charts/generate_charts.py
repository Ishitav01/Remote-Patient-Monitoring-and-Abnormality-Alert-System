import matplotlib.pyplot as plt

# --- Graph 1: Latency Analysis by Component ---

# Data for Latency Analysis
components = ['YOLO Keypoint Detection', 'CNN Pose Classification', 'Alert Generation']
latencies = [60, 20, 100]  # Latency values in milliseconds

# Plotting the bar graph for latency analysis
plt.figure(figsize=(10, 6))
plt.bar(components, latencies, color=['blue', 'green', 'red'])
plt.title('Graph 1: Latency Analysis by Component')
plt.xlabel('System Components')
plt.ylabel('Average Latency (ms)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the figure as a high-resolution image (300 DPI)
plt.savefig("Graph_1_Latency_Analysis_by_Component.png", dpi=300)
plt.show()


# --- Graph 2: Health Suggestions Frequency ---

# Data for Health Suggestions Frequency
time_intervals = ['Morning', 'Afternoon', 'Evening', 'Night']
suggestion_counts = [15, 25, 30, 10]  # Example frequency of suggestions

# Plotting the bar graph for health suggestions frequency
plt.figure(figsize=(10, 6))
plt.bar(time_intervals, suggestion_counts, color=['skyblue', 'orange', 'green', 'purple'])
plt.title('Graph 2: Health Suggestions Frequency')
plt.xlabel('Time of Day')
plt.ylabel('Number of Suggestions')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the figure as a high-resolution image (300 DPI)
plt.savefig("Graph_2_Health_Suggestions_Frequency.png", dpi=300)
plt.show()
