# Fashion MNIST CNN Classifier

## Project Overview
This repository contains implementations of a Convolutional Neural Network (CNN) with six layers for classifying images in the Fashion MNIST dataset. Two versions are provided:
- **Python** (Keras)
- **R** (keras in R)

## Dataset
Fashion MNIST consists of 70,000 grayscale images of size 28×28 belonging to 10 classes (e.g., T-shirt/top, Trouser, Pullover, etc.). It is split into:
- **60,000** training images
- **10,000** test images

## Dependencies

### Python
Install via `pip`:
```bash
pip install keras numpy tensorflow tabulate
```

### R
Install and configure:
```r
install.packages("keras")
install.packages("tensorflow")
library(keras)
install_keras()
install_tensorflow()
```

## Usage

### Python
1. Clone the repo.
2. Ensure dependencies are installed.
3. Run:
   ```bash
   python main.py
   ```
4. The script will:
   - Load and preprocess the data
   - Build a 6-layer CNN
   - Train for 5 epochs
   - Evaluate on the test set
   - Output test accuracy and predictions for two sample images

### R
1. Clone the repo.
2. Ensure R dependencies are installed.
3. In an R session or script:
   ```r
   source("main.R")
   ```
4. The script will perform the same steps as the Python version.

## Model Architecture
1. **Input**: 28×28×1  
2. **Conv2D**: 32 filters, 3×3, ReLU  
3. **MaxPooling2D**: 2×2  
4. **Conv2D**: 64 filters, 3×3, ReLU  
5. **MaxPooling2D**: 2×2  
6. **Flatten**  
7. **Dense**: 10 units, Softmax  

## Training & Evaluation
- **Optimizer**: Adam  
- **Loss**: Sparse Categorical Crossentropy  
- **Metrics**: Accuracy  
- **Epochs**: 5  
- **Batch Size**: 64  
- **Validation Split**: 10%

## Predictions
The scripts predict labels for the first two images in the test set and print:
```
Image 0: true label = X, predicted = Y
Image 1: true label = A, predicted = B
```

## Author
Esther Casely Hayford 
Junior Machine Learning Researcher at Microsoft AI

