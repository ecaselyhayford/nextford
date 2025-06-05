# Import required libraries
# These packages are essential for data manipulation, visualization, modeling, and formatting output
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from tabulate import tabulate

# === PCA Implementation ===

# Load a real-world cancer dataset from sklearn
# This mimics the referral and diagnostic data at Anderson Cancer Center
data = load_breast_cancer()
X = data.data  # Features (30 clinical variables)
y = data.target  # Labels (0 = malignant, 1 = benign)
feature_names = data.feature_names  # Names of variables

# Standardize the features to have mean = 0 and variance = 1
# PCA is sensitive to scale, so this is an essential preprocessing step
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to the full dataset to observe which variables (components) explain most variance
# This helps identify "essential variables" that donor funding decisions might rely on
pca_full = PCA()
X_pca_full = pca_full.fit_transform(X_scaled)

# Plot the cumulative variance explained by the components
# This visual helps show how many components are needed to capture most of the information
plt.figure(figsize=(8, 5))
plt.plot(np.cumsum(pca_full.explained_variance_ratio_), marker="o")
plt.title("Explained Variance by PCA Components")
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance")
plt.grid(True)
plt.tight_layout()
plt.show()

# === Dimensionality Reduction to 2 PCA Components ===

# Reduce the dataset to just 2 principal components
# This allows for 2D PCA and allows for visualization
pca_2 = PCA(n_components=2)
X_pca_2 = pca_2.fit_transform(X_scaled)

# Plot the 2 principal components, colored by class (malignant/benign)
# This helps stakeholders visualize how the two components separate patient outcomes
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca_2[:, 0], y=X_pca_2[:, 1], hue=y, palette="coolwarm", alpha=0.7)
plt.title("2D PCA of Breast Cancer Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.tight_layout()
plt.show()

# === Logistic Regression for Prediction ===

# Split the PCA-reduced data into training and test sets
# This allows us to train a model and evaluate how well 2 components can predict outcomes
X_train, X_test, y_train, y_test = train_test_split(
    X_pca_2, y, test_size=0.3, random_state=42
)

# Train a logistic regression classifier using only the 2 PCA components
# This tests whether dimensionality reduction retains enough signal for accurate classification
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# === Report Results in a nice Format: didn't like default terminal output ===

# Print classification accuracy: how often the model predicts the correct diagnosis
print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.2f}")

# Generate precision, recall, and F1-score per class
# These metrics provide insight into model reliability — crucial for clinical decision-making
report = classification_report(y_test, y_pred, output_dict=True)

# Format the report as a terminal-friendly table using 'tabulate'
# This ensures results are clearly readable for team presentation or reporting
table = []
for label, metrics in report.items():
    if isinstance(metrics, dict):  # Skip summary-level keys like "accuracy"
        row = [
            label,
            f"{metrics['precision']:.2f}",
            f"{metrics['recall']:.2f}",
            f"{metrics['f1-score']:.2f}",
            f"{int(metrics['support'])}",
        ]
        table.append(row)

# Define the column headers for the results table
headers = ["Class", "Precision", "Recall", "F1-Score", "Support"]

# Print the formatted classification report table
print("\nClassification Report:")
print(tabulate(table, headers=headers, tablefmt="grid"))
