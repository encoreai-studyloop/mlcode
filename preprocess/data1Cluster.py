from sklearn.cluster import KMeans
import numpy as np
import pandas as pd


def clusteruser(f, clusternum):
    data = np.loadtxt(f, delimiter=",", dtype=np.float32, encoding="utf-8")
    kdata = data[:,1:7] #데이터 -  성별  나이  관심사 목표  주최경험    참여경험
    klabel = data[:,7:] #라벨
    kdf = pd.DataFrame(data=kdata)

    df = pd.DataFrame(data=klabel, columns=["locid","catid","days"])

    tmp = {}
    cnt=1
    arr = []

    for i in df.values:
        if tuple(i) not in tmp.keys():
            tmp[tuple(i)] = cnt
            cnt+=1
    for i in df.values:
        arr.append(tmp[tuple(i)])

    mean = kdata.mean(axis=0)
    std = kdata.std(axis=0)
    kdata -=mean
    kdata /=std
    kmeans = KMeans(n_clusters=clusternum)
    model = kmeans.fit(kdata)
    df["cluster"] = model.labels_
    df["studyid"] = np.array(arr)
    df["interest"] = data[:,0]
    return df, model, mean, std

