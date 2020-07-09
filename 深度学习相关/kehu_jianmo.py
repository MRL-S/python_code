

#----------------------------------------------------------------------------------------------
#                                               导入库
#----------------------------------------------------------------------------------------------

# 导入Numpy库
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 导入Keras库和包
import keras
from keras.models import Sequential
from keras.layers import Dense

# 将数据集分为训练集和测试集
from sklearn.model_selection import train_test_split

# 特征缩放 （正态分布）从－1到1 
from sklearn.preprocessing import StandardScaler

# 制作混淆矩阵
from sklearn.metrics import confusion_matrix,accuracy_score


#----------------------------------------------------------------------------------------------
#                                               数据预处理
#----------------------------------------------------------------------------------------------
# 导入数据集
dataset = pd.read_csv('BankCustomers.csv')
X = dataset.iloc[:, 3:13] # 全表 
y = dataset.iloc[:, 13]   # 输出值

print('打印表预览')
print(X.head())
print('')
print('客户数量是：')
print(len(y))
print('')

# 将分类特征转换为虚拟变量
states=pd.get_dummies(X['Geography'],drop_first=True)
gender=pd.get_dummies(X['Gender'],drop_first=True)

# 连接其余的虚拟变量列
X=pd.concat([X,states,gender],axis=1)

# 删除列，因为不再需要

X=X.drop(['Geography','Gender'],axis=1)


#dataset.iloc[:, 3:13].values
print(states.head())
 



# 将数据集分为训练集和测试集
# X = 全表
# y = 输出值
feature_train, feature_test, label_train, label_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# 特征缩放 （正态分布）从－1到1 
sc = StandardScaler()
feature_train = sc.fit_transform(feature_train)
feature_test = sc.transform(feature_test)

#----------------------------------------------------------------------------------------------
#                                    定义和训练神经网络
#----------------------------------------------------------------------------------------------

# 初始化人工神经网络
classifier = Sequential()

# 添加输入层和第一个隐藏层
classifier.add(Dense(activation="relu", input_dim=11, units=6, kernel_initializer="uniform"))

# 添加第二个隐藏层
classifier.add(Dense(activation="relu", units=6, kernel_initializer="uniform"))

# 添加输出层
classifier.add(Dense(activation="sigmoid", units=1, kernel_initializer="uniform"))

# 编译神经网络
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# 将ANN拟合到训练集
# 如果你电脑有点慢， 缩小nb_epoch
classifier.fit(feature_train, label_train, batch_size = 10)

#----------------------------------------------------------------------------------------------
#                                    准确性和混淆矩阵
#----------------------------------------------------------------------------------------------

# 预测测试集结果
label_pred = classifier.predict(feature_test)
label_pred = (label_pred > 0.5) # FALSE/TRUE depending on above or below 50%


cm = confusion_matrix(label_test, label_pred)  
accuracy=accuracy_score(label_test,label_pred)

print('打印模型摘要')
print(classifier.summary())
print('')

# 准确性和混淆矩阵

print('印刷混淆矩阵和准确性')
print(cm)
print(accuracy)

