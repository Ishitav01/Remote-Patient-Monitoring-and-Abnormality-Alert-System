import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Sample confusion matrix data
true_labels = ['Standing', 'Bending', 'Falling', 'Standing', 'Bending', 'Falling']
predicted_labels = ['Standing', 'Bending', 'Falling', 'Standing', 'Bending', 'Standing']

# Generate confusion matrix
conf_matrix = confusion_matrix(true_labels, predicted_labels, labels=['Standing', 'Bending', 'Falling'])

# Plotting Confusion Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Standing', 'Bending', 'Falling'], yticklabels=['Standing', 'Bending', 'Falling'])
plt.title('Confusion Matrix for Pose Classification')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()
