## Overview

This project uses **Principal Component Analysis (PCA)** to identify essential variables in the Anderson Cancer Center dataset. The aim is to reduce dimensionality and highlight the most impactful features in cancer diagnosis, in support of data-driven decision-making at the Anderson Cancer Center. An optional logistic regression model is implemented to evaluate the predictive power retained after dimensionality reduction.

---

## Objectives

- **Identify essential variables** through PCA.
- **Reduce dimensionality** of the dataset to 2 principal components.
- **Visualize** how well the two components separate diagnostic outcomes.
- **(Optional)** Train a logistic regression model to assess classification performance using the reduced features.
- **Present results** in a clean, tabulated format for interpretability and decision-making.

---

## Dataset
From this documentation [https://pypi.org/project/sklearn/]() this package is deprecated

The project uses the `Breast Cancer Wisconsin Diagnostic` dataset from `scikit-learn`. This dataset includes:

- **569 samples**
- **30 numerical features** related to cell nuclei characteristics
- **2 target classes**: Malignant (0) and Benign (1)

---

## Methods

### 1. **Preprocessing**
- Features are standardized using `StandardScaler` to ensure PCA isn't biased by feature scale.

### 2. **PCA Implementation**
- Full PCA is performed to analyze how much variance each component captures.
- A cumulative variance plot is used to guide component selection.

### 3. **Dimensionality Reduction**
- PCA is applied with `n_components=2` to reduce the dataset for visualization and modeling.

### 4. **Visualization**
- A 2D scatterplot shows how well the reduced data separates malignant from benign cases.

### 5. **Logistic Regression (Bonus)**
- A simple logistic regression model is trained on the 2D PCA-reduced data.
- Accuracy and classification metrics are reported to evaluate model performance.

### 6. **Formatted Output**
- A clean classification report is printed using the `tabulate` library for easy reading in terminal environments.

---

## Installation

### Required Packages

Install all required packages via pip:

```bash
pip install numpy matplotlib seaborn scikit-learn tabulate
