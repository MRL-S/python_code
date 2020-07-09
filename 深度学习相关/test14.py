import matplotlib.pyplot as plt
import numpy as np
# plt.rcParams["font.sans-serif"] = "SimHei"
# plt.rcParams["axes.unicode_minus"] = False

# n = 1024
# x = np.random.normal(0,1,n)
# y = np.random.normal(0,1,n)

# plt.scatter(x,y,color="blue",marker='*')

# plt.title("标准正态分布",fontsize=20)
# plt.text(2.5,2.5,"均 值：0\n标准差：1")

# plt.xlim(-4,4)
# plt.ylim(-4,4)

# plt.xlabel('横坐标x',fontsize=14)
# plt.ylabel('纵坐标y',fontsize=14)

# plt.show()
import tensorflow as tf
import pandas as pd
plt.rcParams["font.sans-serif"] = 'SimHei'
plt.rcParams["axes.unicode_minus"] = False
# boston_housing = tf.keras.datasets.boston_housing

# (train_x,train_y),(_,_) = boston_housing.load_data(test_split=0)
# titles = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B-1000','LSTAT','MEDV']
# plt.figure(figsize=(12,12))
# for i in range(13):
#     plt.subplot(4,4,(i+1))
#     plt.scatter(train_x[:,i],train_y)
#     plt.xlabel(titles[i])
#     plt.ylabel("Price($1000's)")
#     plt.title(str(i)+"."+titles[i]+'- Price')
# plt.tight_layout(rect=[0,0,1,0.9])
# plt.show()
# print(train_x[0:5])
COLUMN_NAMES = ['SepalLength','SepalWidth','PetaLength','PetalWidth','Species']
TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
train_path = tf.keras.utils.get_file("iris_training.csv",TRAIN_URL)
df_iris = pd.read_csv(train_path,header=0,names=COLUMN_NAMES)
iris = np.array(df_iris)
fig = plt.figure('Iris Data',figsize=(15,15))
plt.suptitle("Anderson's Iris Data Set\n(Bule->Setosa | Red->versicolor | Green->Virginica)")

for i in range(4):
    for j in range(4):
        plt.subplot(4,4,4*i+(j+1))
        if (i==j):
            plt.text(0.3,0.4,COLUMN_NAMES[i],fontsize=15)
        else:
            plt.scatter(iris[:,j],iris[:,i],c=iris[:,4],cmap="brg")
        if (i==0):
            plt.title(COLUMN_NAMES[j])
        if (j==0):
            plt.ylabel(COLUMN_NAMES[i])
plt.show()