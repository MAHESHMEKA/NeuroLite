from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import SGD

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import numpy as np
import time

def binary_cross_entropy(y_true, y_pred):
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)

    return -np.mean(
        y_true * np.log(y_pred) +
        (1 - y_true) * np.log(1 - y_pred)
    )

x, y = load_breast_cancer(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

keras_model = Sequential([
    Input(shape=(30,)),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid")
])

keras_model.compile(
    optimizer=SGD(learning_rate=0.001),
    loss="binary_crossentropy"
)

start1 = time.time()

keras_model.fit(
    x_train,
    y_train,
    epochs=100,
    batch_size=32,
    verbose=1
)

end1 = time.time()

keras_pred_prob = keras_model.predict(x_test, verbose=0).flatten()

keras_pred = (keras_pred_prob >= 0.5).astype(int)

keras_accuracy = accuracy_score(
    y_test,
    keras_pred
)

keras_loss = binary_cross_entropy(
    y_test,
    keras_pred_prob
)

from src import Network

model = Network(x.shape)

model.add_layer(8, activation="relu")
model.add_layer(1, activation="sigmoid")

model.compile(
    loss="binary_cross_entropy",
    learning_rate=0.001,
    epochs=100,
    batch_size=32
)

start2 = time.time()

model.train(
    x_train,
    y_train
)

end2 = time.time()

framework_pred_prob = model.predict(x_test).flatten()

framework_pred_prob = np.clip(
    framework_pred_prob,
    1e-15,
    1 - 1e-15
)

framework_pred = (
    framework_pred_prob >= 0.5
).astype(int)

framework_accuracy = accuracy_score(
    y_test,
    framework_pred
)

framework_loss = binary_cross_entropy(
    y_test,
    framework_pred_prob
)


print(f"Keras Training Time      : {end1-start1:.4f} s")
print(f"Framework Training Time  : {end2-start2:.4f} s")

print()

print(f"Keras BCE Loss           : {keras_loss:.6f}")
print(f"Framework BCE Loss       : {framework_loss:.6f}")

print()

print(f"Keras Accuracy           : {keras_accuracy*100:.2f}%")
print(f"Framework Accuracy       : {framework_accuracy*100:.2f}%")