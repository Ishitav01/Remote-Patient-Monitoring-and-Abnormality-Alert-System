import matplotlib.pyplot as plt

# Data for Latency vs. Accuracy Graph
# Each point represents a hypothetical model or configuration in your project
models = ['YOLOv8 + CNN', 'OpenPose', 'HRNet', 'PoseNet', 'DeepLabCut']
latencies = [180, 350, 300, 90, 400]  # Latency in milliseconds
accuracies = [90.37, 88, 92, 75, 87]  # Accuracy in percentage

# Plotting the Latency vs. Accuracy graph
plt.figure(figsize=(10, 6))
plt.scatter(latencies, accuracies, color='blue', s=100, label='Model Performance')

# Annotate each point with the model name
for i, model in enumerate(models):
    plt.text(latencies[i] + 5, accuracies[i] - 1, model, fontsize=10)

# Adding graph labels and title
plt.title('Graph: Latency vs. Accuracy', fontsize=14)
plt.xlabel('Latency (ms)', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
plt.grid(linestyle='--', alpha=0.7)
plt.xlim(0, 450)
plt.ylim(70, 95)
plt.legend(loc='lower left')

# Save the graph as a high-resolution image
plt.savefig("Graph_Latency_vs_Accuracy.png", dpi=300)  # Save in high resolution for publication
plt.show()
