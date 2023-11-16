import pandas as pd
import numpy as np
a = [1.,7,2]
# Creating an empty series
ser = pd.Series(dtype=float)
print(ser)


data = np.array(['g','e','e','k','s'])
ser = pd.Series(data)
print(ser)

df = pd.DataFrame()
print()
print(df)


df = pd.DataFrame(data=a)
print(df)
print()

m = {'col1': (1,2), 'col2': (3,4), 'col3': [4,5]}
df = pd.DataFrame(data=m)
print(df)
print()


import numpy as np

deep_layer = 100


W1 =np.random.uniform(-0.5, 0.5, (len(X[0]) * deep_layer)) # \n",
W1 = np.reshape(W1, (deep_layer,len(X[0]))) #  150 x 768\n",
b1 = np.random.uniform(0, 0, deep_layer) # 0 0\n",
b1 = np.reshape(b1,(deep_layer,1)) # 150 x 1\n",
W2 = np.random.uniform(-0.5, 0.5, 10 * deep_layer) # 10 x 150\n",
W2 = np.reshape(W2, (10,deep_layer))\n",
b2 = np.random.uniform(0, 0, (10*1))\n",
b2 = np.reshape(b2, (10, 1)) #10 X 1\n",


def sigmoid():
    pass

def sigmoid_derivative():
    pass

def nll_loss():
    pass
def softmax():
    pass

def train(X, y):
    for i in range(10):
        temp_X = np.reshape(X[i], (len(X[0]), 1))

        z1 = np.dot(W1, temp_X) + b1  # 150 X 768 * 768 X 1 = 150 X 1\n",

        h1 = sigmoid(z1)

        Z2 = np.dot(W2, h1) + b2  # 10 X 150   150 X 1 = 10 x 1 \n",

        y_hat = softmax(Z2)

        y_true = np.zeros(shape=[10, 1])

        y_true[int(y[i]), 0]=1

        loss =  nll_loss(y_hat, y_true)

        avg_epoch_loss = avg_epoch_loss + loss

        dZ2 = (y_hat - y_true) #dl/dz2\n",

        dW2 = np.dot(h1,dZ2.T).T

        db2 = dZ2
        dh1 = np.dot(dZ2.T, W2) # (1 X 10) *(10 X 150) = 1 X 150.   dL/dZ2 * dZ2/dh\n",

        dz1 =dh1 * sigmoid_derivative(z1.T)  # dL/dZ2 * dZ2/dh1 * dh1/dz1 = 150 X 1 * 150 X 1\\\n",

        dW1 = (np.dot(temp_X, dz1)).T   # (150 X 1)*(1 X 768)  =150 X 768     dL/dZ2 * dZ2/dh1 * dh1/dz1 * dz1/dw1\n",
        db1 = dz1.T



