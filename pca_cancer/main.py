import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from tabulate import tabulate

# === Utility Function to Print Classification Report as a Table ===
# This function prints the classification metrics in a terminal-friendly table format
# It supports easy model evaluation and presentation


def print_classification_table(y_true, y_pred, title):
    print(f"\n{title}")
    report_dict = classification_report(y_true, y_pred, output_dict=True)
    table = []
    for label, metrics in report_dict.items():
        if isinstance(metrics, dict):
            table.append(
                [
                    label,
                    f"{metrics['precision']:.2f}",
                    f"{metrics['recall']:.2f}",
                    f"{metrics['f1-score']:.2f}",
                    int(metrics["support"]),
                ]
            )
    headers = ["Class", "Precision", "Recall", "F1-Score", "Support"]
    print(tabulate(table, headers=headers, tablefmt="grid"))


# === Load Data ===
# Load the breast cancer dataset provided by sklearn
# This dataset simulates the cancer referral data that our model will analyze

data = load_breast_cancer()
X = data.data
y = data.target

# === Split ===
# Split the dataset into training and testing sets (70/30 split)
# This helps evaluate model performance on unseen data

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# === Step 3: Baseline Model (No PCA) ===
# Build a pipeline that standardizes the data and applies logistic regression
# This serves as a benchmark for evaluating the impact of PCA

baseline_pipeline = Pipeline(
    [("scaler", StandardScaler()), ("logreg", LogisticRegression(max_iter=1000))]
)

# Evaluate baseline model using cross-validation
baseline_scores = cross_val_score(
    baseline_pipeline, X_train, y_train, cv=5, scoring="accuracy"
)
print("Baseline Model (No PCA):")
print(
    f"Cross-validated Accuracy: {baseline_scores.mean():.2f} ± {baseline_scores.std():.2f}\n"
)

# Train and test the model
baseline_pipeline.fit(X_train, y_train)
y_pred_base = baseline_pipeline.predict(X_test)

# Display classification report as table
print_classification_table(
    y_test, y_pred_base, "Baseline Classification Report (No PCA)"
)

# === PCA Model with 2 Components ===
# Reduce dimensionality to 2 principal components
# This aligns with the assignment's goal of essential variable identification using PCA

pca_pipeline = Pipeline(
    [
        ("scaler", StandardScaler()),
        ("pca", PCA(n_components=2)),
        ("logreg", LogisticRegression(max_iter=1000)),
    ]
)

# Evaluate PCA model using cross-validation
pca_scores = cross_val_score(pca_pipeline, X_train, y_train, cv=5, scoring="accuracy")
print("\nPCA Model (2 Components):")
print(f"Cross-validated Accuracy: {pca_scores.mean():.2f} ± {pca_scores.std():.2f}\n")

# Train and test the PCA model
pca_pipeline.fit(X_train, y_train)
y_pred_pca = pca_pipeline.predict(X_test)

# Display classification report for PCA model
print_classification_table(
    y_test, y_pred_pca, "PCA Classification Report (2 Components)"
)

# === Confusion Matrix ===
# Confusion matrix provides detailed error analysis
# It highlights false positives and false negatives, critical in cancer diagnostics

cm = confusion_matrix(y_test, y_pred_pca)
plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=data.target_names,
    yticklabels=data.target_names,
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix (With PCA)")
plt.tight_layout()
plt.show()

# === Cumulative Explained Variance Plot ===
# Visualize how much variance is captured by each PCA component
# This helps justify the selection of only 2 components by demonstrating retained variance

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
full_pca = PCA()
X_pca_full = full_pca.fit_transform(X_scaled)

plt.figure(figsize=(8, 5))
plt.plot(np.cumsum(full_pca.explained_variance_ratio_), marker="o")
plt.title("Cumulative Explained Variance by PCA Components")
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance")
plt.grid(True)
plt.tight_layout()
plt.show()
