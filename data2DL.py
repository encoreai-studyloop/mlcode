import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras import models, layers
import numpy as np
import pickle

data = np.loadtxt("data/data2_generate.csv", delimiter=",", dtype=np.float32)
x_data = data[:,:-1]
y_data = data[:,-1]

kdata = data[:,:-1] #데이터
klabel = data[:,-1] #라벨
print(kdata.shape)
print(klabel.shape)
train_data, test_data, train_label, test_label = train_test_split(kdata, klabel, stratify=klabel)

#정규화
mean = train_data.mean(axis=0)
std = train_data.std(axis=0)
mean1 = test_data.mean(axis=0)
std1 = test_data.std(axis=0)
train_data -=mean
train_data /=std
test_data -= mean1
test_data /=std1

pickle.dump(mean, open("mean.dl", 'wb'))
pickle.dump(std, open("std.dl", "wb"))
print(pickle.load(open("mean.dl", 'rb')))

#model = models.Sequential()
#model.add(layers.Dense(64, activation="relu", input_shape=(train_data.shape[1], ))) # 12개
#model.add(layers.Dense(64, activation="relu"))
#model.add(layers.Dense(1))
#model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
#여기서 예측 가능
#print(train_label)
#model.fit(train_data, train_label, epochs=1000)
#filename = 'data2DL.model'
#pickle.dump(model, open(filename, 'wb'))

#print(model.predict(test_data))
#print(test_label)
#print(model.evaluate(train_data, train_label))
# k = 4
# n_samples = len(train_data)//k
# scores = []
# for i in range(k):
#     v_data = train_data[i*n_samples:(i+1)*n_samples]
#     v_label = train_label[i*n_samples:(i+1)*n_samples]
#
#     f_data = np.concatenate([train_data[:i*n_samples], train_data[(i+1)*n_samples:]], axis=0)
#     f_label = np.concatenate([train_label[:i*n_samples], train_label[(i+1)*n_samples:]], axis=0)
#     model.fit(f_data, f_label, epochs=2, batch_size=1, verbose=1)
#     mse, mae = model.evaluate(v_data, v_label)
#     scores.append(mae)
#
# print(scores)
# print(np.mean(scores))