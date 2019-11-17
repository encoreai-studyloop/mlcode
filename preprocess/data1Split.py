import csv
import data1Cluster
import numpy as np
import pickle
import os

input_file = "data/data1_generate.csv"
output_file1 = "data/data1_user.csv"
output_file2 = "data/data1_study.csv"
clustermodel = None
user = open(output_file1, 'w', newline='', encoding="utf-8")
study = open(output_file2, 'w', newline='', encoding="utf-8")
df, clustermodel, mean, std = data1Cluster.clusteruser(input_file, 10)
filename = 'data1Cluster.model'
pickle.dump(clustermodel, open(filename, 'wb'))
meanstd = open('meanstd.txt', 'w')
meanstd.write(str(mean.tolist())[1:-1].replace(" ",""))
meanstd.write("\n")
meanstd.write(str(std.tolist())[1:-1].replace(" ",""))
meanstd.close()

clustermodel = pickle.load(open("data1Cluster.model", 'rb'))
#성별  나이  관심사 목표  주최경험    참여경험
testuser = np.array([[0.0,25.0,3.0,4.0,1.0,2.0]])
testuser -=mean
testuser /= std
print("predictin : ", clustermodel.predict(testuser))
#print(df)
userlist = {}
studylist = {}
for i in df.values:
    if (int(i[3]), int(i[4])) not in userlist.keys():
        userlist[(int(i[3]), int(i[4]))] = i[5]
    else:
        userlist[(int(i[3]), int(i[4]))] = float(userlist[(int(i[3]), int(i[4]))])+float(i[5])
    if int(i[4]) not in studylist.keys():
        studylist[int(i[4])] = [int(i) for i in i[:3]]

fuser = csv.writer(user)
fstudy = csv.writer(study)
fusercol = ["userclusterid", "studyid", "interest"]
fstudycol = ["studyid", "studloc", "studycat", "studyday"]
#fuser.writerow(fusercol)
#fstudy.writerow(fstudycol)
for i in userlist.keys():
    fuser.writerow(i+tuple(np.array([userlist[i]])))
for i in studylist.keys():
    fstudy.writerow(tuple(np.array([i]))+tuple(studylist[i]))

user.close()
study.close()


