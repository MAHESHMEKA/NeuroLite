# Breast Cancer Wisconsin Benchmark

## Objective

Evaluate the performance of the custom NumPy-based Neural Network Framework by comparing it against TensorFlow Keras using an identical neural network architecture and training configuration on a binary classification task.

---

## Benchmark Configuration

| Parameter | Value |
|-----------|-------|
| Dataset | Breast Cancer Wisconsin |
| Task | Binary Classification |
| Input Features | 30 |
| Output Units | 1 |
| Hidden Layers | 1 |
| Hidden Neurons | 8 |
| Hidden Activation | ReLU |
| Output Activation | Sigmoid |
| Loss Function | Binary Cross Entropy (BCE) |
| Optimizer | Mini-batch Gradient Descent (Framework) / SGD (Keras) |
| Learning Rate | 0.001 |
| Epochs | 100 |
| Batch Size | 32 |
| Train/Test Split | 80% / 20% |
| Feature Scaling | StandardScaler |

---

## Model Architecture

```
Input (30)
      │
      ▼
Dense(8, ReLU)
      │
      ▼
Dense(1, Sigmoid)
```

---

# Benchmark Results

| Metric | Neural Network Framework | TensorFlow Keras |
|---------|-------------------------:|-----------------:|
| Final Training Loss | **0.361790** | **0.417500** |
| Test Binary Cross Entropy | **0.345945** | **0.402925** |
| Test Accuracy | **94.74%** | **95.61%** |
| Training Time | **0.1342 s*** | **4.9044 s*** |

> *Training time includes framework-specific initialization and execution overhead. Multiple benchmark runs should be performed before drawing conclusions regarding execution speed.*

---

## Performance Comparison

### Binary Cross Entropy

```
Framework : 0.345945
Keras     : 0.402925

Difference = 0.056980
```

---

### Classification Accuracy

```
Framework : 94.74%
Keras     : 95.61%

Difference = 0.87%
```

---

## Observations

- Both models were trained using the same neural network architecture.
- Both implementations used the same learning rate, batch size, number of epochs, and train/test split.
- Input features were standardized using StandardScaler before training.
- The custom framework demonstrated stable convergence throughout training.
- The framework achieved **94.74%** classification accuracy, only **0.87%** lower than TensorFlow Keras under identical benchmark settings.
- The benchmark validates the correctness of the forward propagation, backpropagation, Binary Cross Entropy implementation, parameter updates, and overall training pipeline of the custom neural network framework.

---

## Conclusion

The custom NumPy-based Neural Network Framework achieved performance comparable to TensorFlow Keras on the Breast Cancer Wisconsin dataset. With only a **0.87%** difference in classification accuracy while using an independently implemented training pipeline, the benchmark demonstrates the correctness and effectiveness of the framework for binary classification tasks.