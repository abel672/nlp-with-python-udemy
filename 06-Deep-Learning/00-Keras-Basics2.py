# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np


# %%
from sklearn.datasets import load_iris


# %%
iris = load_iris()


# %%
type(iris)


# %%
print(iris.DESCR)


# %%
X = iris.data


# %%
X # numpy array with four measurments (sepal length, sepal width, petal length, petal width)


# %%
y = iris.target


# %%
y # classes


# %%
# this is how keras will setup the classes from 'y'
# class 0 --> [1,0,0]
# class 1 --> [0,1,0]
# class 2 --> [0,0,1]


# %%
from keras.utils import to_categorical


# %%
y = to_categorical(y)


# %%
y.shape


# %%
# step 1: Train the data that you have with sklearn
from sklearn.model_selection import train_test_split


# %%
# X = 4 measurments, y = 3 classes models
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# %%
# y_test


# %%
from sklearn.preprocessing import MinMaxScaler


# %%
# how MinMaxScaler works
np.array([5,10,15,20])/20 # [min, x, y, max]/max = (ranges between 0 to 1)


# %%
scaler_object = MinMaxScaler()


# %%
scaler_object.fit(X_train)


# %%
scaled_X_train = scaler_object.transform(X_train)


# %%
scaled_X_test = scaler_object.transform(X_test)


# %%
# all the values are now between 0 and 1 (helps neural networkw to evade large symbiosis growing)
# scaled_X_train


# %%
# setp 2: Build a network with keras
from keras.models import Sequential # Model to use. In this case sequencial, to add a sequence of layers
from keras.layers import Dense # layers to use, in this case, Dense layers


# %%
model = Sequential()
model.add(Dense(8,input_dim=4,activation='relu'))
model.add(Dense(8,input_dim=4,activation='relu'))
model.add(Dense(3,activation='softmax')) # [0.2,0.3,0.5]
# compile the model
model.compile(
    loss='categorical_crossentropy', # what are we performing? in this case categorical data
    optimizer='adam',
    metrics=['accuracy'] # what are we trainig? what are we gonig to report back?. In this case, accuracy.
)


# %%
model.summary()


# %%
model.fit(scaled_X_train, y_train, epochs=150, verbose=2) # train our model with our scale data


# %%



