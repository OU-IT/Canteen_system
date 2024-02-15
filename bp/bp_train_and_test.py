import pandas as pd  
from keras.models import Sequential  
from keras.layers import Dense  
from sklearn.model_selection import train_test_split  
import pickle 
  
# 读取txt文件  
data = pd.read_csv('user.txt', sep=' ', header=None, names=['user_id', 'item1', 'item2', 'item3', 'item4'], on_bad_lines='error')

  
# 数据预处理：将选择次数转换为概率  
data['item1'] /= data['item1'].sum()  
data['item2'] /= data['item2'].sum()  
data['item3'] /= data['item3'].sum()  
data['item4'] /= data['item4'].sum()  
  
# 划分特征和目标  
X = data[['user_id', 'item1', 'item2', 'item3', 'item4']]  
y = data[['item1', 'item2', 'item3', 'item4']]  
  
# 划分训练集和测试集  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)  
  
# 定义神经网络模型  
model = Sequential()  
model.add(Dense(5, input_shape=(5,), activation='relu'))  # 输入层，5个神经元对应5个特征  
model.add(Dense(1000, activation='relu'))  # 隐藏层，10个神经元  
model.add(Dense(1000, activation='relu'))  # 隐藏层，10个神经元  
model.add(Dense(4, activation='softmax'))  # 输出层，4个神经元对应4个商品的概率  
  
# 编译模型  
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])  
  
# 训练模型  
model.fit(X_train, y_train, batch_size=20, epochs=10)  
  
#保存模型
with open('my_model.pkl', 'wb') as f:  
    pickle.dump(model, f)  

# 评估模型性能  
loss, accuracy = model.evaluate(X_test, y_test)  
print(X_test)
print(y_test)
print('Test loss:', loss)  
print('Test accuracy:', accuracy)