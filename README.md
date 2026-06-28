# About NeuroLite

NeuroLite is an educational neural network framework designed to demonstrate the complete implementation of feedforward neural networks using only NumPy.

## Implemented Features

### Architecture

* Fully Object-Oriented Design
* Sequential Network Builder
* Dense (Fully Connected) Layer
* Unlimited Hidden Layers
* Configurable Network Architecture

### Activation Functions

* Sigmoid
* ReLU
* Tanh
* Softmax
* Linear

### Loss Functions

* Mean Squared Error (MSE)
* Mean Absolute Error (MAE)
* Binary Cross Entropy (BCE)

### Weight Initialization

* Xavier Initialization
* He Initialization

### Training Pipeline

* Forward Propagation
* Backpropagation
* Mini-batch Gradient Descent
* Configurable Learning Rate
* Configurable Batch Size
* Configurable Epochs
* Dataset Shuffling Every Epoch

### Model Utilities

* Prediction API
* Model Serialization
* Model Loading
* Network Structure Visualization

---

# Framework Statistics

| Component                     |                       Value |
| ----------------------------- | --------------------------: |
| Programming Language          |                      Python |
| Core Numerical Library        |                       NumPy |
| Layer Types                   |                   1 (Dense) |
| Activation Functions          |                           5 |
| Loss Functions                |                           3 |
| Weight Initialization Methods |                           2 |
| Optimizer                     | Mini-batch Gradient Descent |
| Hidden Layers                 |                   Unlimited |
| Model Serialization           |                           ✓ |
| Object-Oriented Architecture  |                           ✓ |

---

# NeuroLite Benchmarks

This directory contains benchmark experiments for **NeuroLite**, a lightweight neural network framework developed entirely from scratch using **NumPy**.

Unlike high-level deep learning libraries, NeuroLite was built to provide complete transparency into how neural networks work internally. Every stage of the learning pipeline—including forward propagation, backpropagation, gradient computation, weight initialization, optimization, prediction, and model serialization—was implemented from first principles without relying on machine learning frameworks such as TensorFlow or PyTorch.

The benchmark suite validates the correctness of the implementation by comparing NeuroLite against equivalent TensorFlow Keras models under identical training configurations.

---

# Benchmark Objective

The purpose of these benchmarks is to verify that NeuroLite produces learning behavior comparable to TensorFlow Keras when trained using identical architectures and hyperparameters.

Rather than comparing feature counts, the benchmarks focus on validating:

* Forward propagation correctness
* Backpropagation implementation
* Parameter update correctness
* Loss convergence
* Prediction performance
* Framework stability

---

# Benchmark Philosophy

Every benchmark follows the same evaluation methodology.

* Same dataset
* Same train/test split
* Same neural network architecture
* Same activation functions
* Same learning rate
* Same batch size
* Same number of epochs
* Same preprocessing pipeline (when required)
* Same evaluation metrics

This ensures a fair and reproducible comparison between NeuroLite and TensorFlow Keras.

---

# Benchmark Suite

| Dataset                 | Task                  | Status      |
| ----------------------- | --------------------- | ----------- |
| California Housing      | Regression            | ✅ Completed |
| Breast Cancer Wisconsin | Binary Classification | ✅ Completed |


---

# Completed Benchmarks

## 1. California Housing

### Configuration

* Task: Regression
* Network: **8 → 4 → 1**
* Activation: **ReLU → Linear**
* Loss: **Mean Squared Error**
* Learning Rate: **0.0001**
* Epochs: **100**
* Batch Size: **32**

### Results

| Metric              |    NeuroLite | TensorFlow Keras |
| ------------------- | -----------: | ---------------: |
| Final Training Loss | **1.330502** |     **1.330300** |
| Test MSE            | **1.335795** |     **1.336023** |

### Observation

NeuroLite achieved a Test MSE within **0.00023** of TensorFlow Keras under identical training conditions, demonstrating nearly identical convergence behavior.

Detailed Report

* `california_housing_benchmark_summary.md`

---

## 2. Breast Cancer Wisconsin

### Configuration

* Task: Binary Classification
* Network: **30 → 8 → 1**
* Activation: **ReLU → Sigmoid**
* Loss: **Binary Cross Entropy**
* Learning Rate: **0.001**
* Epochs: **100**
* Batch Size: **32**
* Feature Scaling: StandardScaler

### Results

| Metric              |    NeuroLite | TensorFlow Keras |
| ------------------- | -----------: | ---------------: |
| Final Training Loss | **0.361790** |     **0.417500** |
| Test BCE            | **0.345945** |     **0.402925** |
| Test Accuracy       |   **94.74%** |       **95.61%** |

### Observation

NeuroLite achieved **94.74%** classification accuracy, remaining within **0.87%** of TensorFlow Keras while using an independently implemented training pipeline.

Detailed Report

* `breast_cancer_benchmark_summary.md`

---

# Benchmark Methodology

Every benchmark follows the same experimental workflow:

1. Load the dataset.
2. Split into training and testing sets.
3. Apply preprocessing (when required).
4. Train an equivalent TensorFlow Keras model.
5. Train NeuroLite using identical hyperparameters.
6. Evaluate both models.
7. Compare convergence, prediction quality, and evaluation metrics.
8. Document the benchmark results.

---

# Conclusion

The benchmark results demonstrate that NeuroLite correctly implements the complete neural network training pipeline—from forward propagation and backpropagation to parameter optimization and prediction—using only NumPy.

Across both regression and binary classification tasks, NeuroLite achieved performance comparable to TensorFlow Keras under identical experimental settings. These benchmarks provide strong evidence for the correctness, stability, and educational value of the framework while serving as a foundation for future enhancements.
