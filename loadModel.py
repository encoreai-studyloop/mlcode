import pickle
import csv
import numpy as np

model = pickle.load(open("data1ML.model", 'rb'))
f = open("mlresult.csv", 'w', newline='', encoding="utf-8")
ff = csv.writer(f)
cnt = 0
for i in range(10):
    for j in range(4000):
        ff.writerow([cnt,i,j,model.predict(str(i),str(j)).est])
        cnt+=1
f.close()

clustermodel = pickle.load(open("data1Cluster.model", 'rb'))
f = open("meanstd.txt", "r")
mean = f.readline()
std = f.readline()
f.close()
mean = np.array(mean.replace("\n", "").split(",")).astype('float64')
print(mean)
std = np.array(std.split(",")).astype('float64')
#성별  나이  관심사 목표  주최경험    참여경험
testuser = np.array([[0.0,25.0,3.0,4.0,1.0,2.0]])
testuser -=mean
testuser /= std
print("predictin : ", clustermodel.predict(testuser)[0])