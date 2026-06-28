# California Housing Benchmark

## Objective

Evaluate the performance of the custom NumPy-based Neural Network Framework against TensorFlow Keras using an identical neural network architecture and training configuration.

---

## Dataset

- **Dataset:** California Housing
- **Source:** scikit-learn (`fetch_california_housing`)
- **Task:** Regression
- **Input Features:** 8
- **Output:** Median House Value

---

## Model Configuration

| Parameter | Value |
|-----------|-------|
| Network Architecture | 8 → 4 (ReLU) → 1 (Linear) |
| Hidden Layers | 1 |
| Activation Function | ReLU |
| Loss Function | Mean Squared Error (MSE) |
| Optimizer | Mini-batch Gradient Descent (Framework) / SGD (Keras) |
| Learning Rate | 0.0001 |
| Batch Size | 32 |
| Epochs | 100 |

---

# Benchmark Results

| Metric | Neural Network Framework | TensorFlow Keras |
|---------|-------------------------:|-----------------:|
| Final Training Loss | **1.33050** | **1.33030** |
| Test Mean Squared Error (MSE) | **1.33579** | **1.33602** |
| Training Time* | **2.23 s** | **41.77 s** |

---

## Observations

- Both implementations converged to nearly identical training losses.
- The custom framework achieved a test MSE within **0.00023** of TensorFlow Keras.
- The benchmark demonstrates that the implemented forward propagation, backpropagation, gradient computation, and parameter updates produce results comparable to an established deep learning framework under the tested configuration.
- Training time measurements are preliminary and should not be interpreted as a definitive performance comparison without multiple benchmark runs and averaging.

---

## Experimental Setup

Both implementations used:

- Same dataset
- Same train/test split
- Same network architecture
- Same learning rate
- Same batch size
- Same number of epochs
- Mean Squared Error (MSE) as the loss function

This benchmark aims to validate the correctness of the custom implementation rather than outperform TensorFlow Keras.

---

## Conclusion

The NumPy-based Neural Network Framework successfully reproduces the learning behavior of an equivalent TensorFlow Keras model on the California Housing regression dataset.

The minimal difference in final training loss and test MSE indicates that the framework correctly implements:

- Dense Layers
- Forward Propagation
- Backpropagation
- Mini-batch Gradient Descent
- Weight Initialization
- Model Prediction

Future benchmarks will include additional datasets such as XOR, Iris, Breast Cancer Wisconsin, and MNIST to further evaluate the framework across binary classification, multiclass classification, and regression tasks.

---

\* Training time depends on the software framework, runtime initialization, hardware, and execution environment. Timing results should be interpreted cautiously and validated over multiple runs.