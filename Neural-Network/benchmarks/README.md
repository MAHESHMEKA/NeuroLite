# Neural Network Framework Benchmarks

This directory contains benchmark experiments conducted to validate the correctness, stability, and predictive performance of the custom **NumPy-based Neural Network Framework** by comparing it with equivalent **TensorFlow Keras** implementations.

Rather than measuring raw speed, these benchmarks focus on verifying that the framework learns correctly and converges to performance comparable with an industry-standard deep learning library under identical training conditions.

---

# Objective

The primary objectives of these benchmarks are to:

* Validate the correctness of forward propagation.
* Verify the implementation of backpropagation.
* Evaluate weight update behavior during training.
* Compare convergence against TensorFlow Keras.
* Demonstrate the framework's ability to solve both regression and classification problems.
* Provide reproducible experimental results for future improvements.

---

# Benchmark Principles

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

Using identical configurations ensures that any observed differences originate from the framework implementation rather than experimental settings.

---

# Benchmark Suite

| Dataset                 | Machine Learning Task | Status      |
| ----------------------- | --------------------- | ----------- |
| California Housing      | Regression            | ✅ Completed |
| Breast Cancer Wisconsin | Binary Classification | ✅ Completed |

---

# Completed Benchmarks

## California Housing

A regression benchmark performed using the California Housing dataset.

### Configuration

* Input Features: **8**
* Hidden Layers: **1**
* Hidden Neurons: **4**
* Network Architecture: **8 → 4 → 1**
* Activation Functions: **ReLU → Linear**
* Loss Function: **Mean Squared Error (MSE)**
* Learning Rate: **0.0001**
* Epochs: **100**
* Batch Size: **32**

### Results

| Metric              | Custom Framework | TensorFlow Keras |
| ------------------- | ---------------: | ---------------: |
| Final Training Loss |     **1.330502** |     **1.330300** |
| Test MSE            |     **1.335795** |     **1.336023** |

### Summary

The custom framework achieved a Test Mean Squared Error within **0.00023** of TensorFlow Keras, demonstrating nearly identical convergence and predictive performance under identical training configurations.

Detailed Report:

* `california_housing_benchmark_summary.md`

---

## Breast Cancer Wisconsin

A binary classification benchmark performed using the Breast Cancer Wisconsin dataset.

### Configuration

* Input Features: **30**
* Hidden Layers: **1**
* Hidden Neurons: **8**
* Network Architecture: **30 → 8 → 1**
* Activation Functions: **ReLU → Sigmoid**
* Loss Function: **Binary Cross Entropy**
* Learning Rate: **0.001**
* Epochs: **100**
* Batch Size: **32**
* Feature Scaling: **StandardScaler**

### Results

| Metric                    | Custom Framework | TensorFlow Keras |
| ------------------------- | ---------------: | ---------------: |
| Final Training Loss       |     **0.361790** |     **0.417500** |
| Test Binary Cross Entropy |     **0.345945** |     **0.402925** |
| Classification Accuracy   |       **94.74%** |       **95.61%** |

### Summary

The framework achieved **94.74%** classification accuracy, remaining within **0.87%** of TensorFlow Keras while using a completely independent implementation of forward propagation, backpropagation, and parameter updates.

Detailed Report:

* `breast_cancer_benchmark_summary.md`

---

# Benchmark Methodology

Each benchmark follows the same experimental workflow:

1. Load the dataset.
2. Split into training and testing sets.
3. Apply preprocessing when required.
4. Train the TensorFlow Keras reference model.
5. Train the custom Neural Network Framework using identical hyperparameters.
6. Evaluate both models on the testing set.
7. Compare convergence, loss, and predictive performance.
8. Document the results.

---

# Evaluation Metrics

### Regression

* Mean Squared Error (MSE)
* Final Training Loss

### Binary Classification

* Binary Cross Entropy (BCE)
* Classification Accuracy
* Final Training Loss

---

# Benchmark Environment

All benchmarks were executed using the same software environment.

| Component            | Value            |
| -------------------- | ---------------- |
| Programming Language | Python           |
| Numerical Library    | NumPy            |
| Reference Framework  | TensorFlow Keras |
| Operating System     | Windows          |

---

# Conclusion

The completed benchmarks demonstrate that the custom NumPy-based Neural Network Framework correctly implements the essential components of neural network training, including forward propagation, backpropagation, parameter optimization, and prediction.

Across both regression and binary classification tasks, the framework achieved performance comparable to TensorFlow Keras while remaining lightweight, transparent, and designed specifically for educational understanding and algorithmic exploration.

These benchmarks will continue to evolve as additional features, optimizers, and layer types are incorporated into the framework.
