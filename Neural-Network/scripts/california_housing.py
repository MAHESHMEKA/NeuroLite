from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense 
from sklearn.datasets import fetch_california_housing
from tensorflow.keras.optimizers import SGD
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse

x,y=fetch_california_housing(return_X_y=True)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

model=Sequential([
    Dense(4,activation="relu",input_shape=(8,)),
    Dense(1)
])

model.compile(
    optimizer=SGD(learning_rate=0.0001),
    loss="mse"
)

start1=time.time()
model.fit(x_train,y_train,epochs=100,batch_size=32)
end1=time.time()

from src import Network
model1=Network(x.shape)
model1.add_layer(4,activation="relu")
model1.add_layer(1)

model1.compile(loss="mse",learning_rate=0.0001,epochs=100,batch_size=32)
start2=time.time()
model1.train(x_train,y_train)
end2=time.time()

pred=model.predict(x_test)
performance=mse(y_test,pred)

pred1=model1.predict(x_test)
performance1=mse(y_test,pred1)

print("Keras training time : " ,end1-start1)
print("Newtwork training time : ",end2-start2)

print("Keras test mse : ",performance)
print("Network test mse : ",performance1)

