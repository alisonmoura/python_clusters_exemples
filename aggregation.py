import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import KMeans

style.use("ggplot")

datas = []

file = open("aggregation.txt")
for line in file:
    line = line.split('\t')
    line[2] = line[2].replace("\r\n","")
    datas.append(line)

def plotData():
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    print(centroids)
    print(labels)
    colors = ["g.", "r.", "b.", "y.", "k."]
    for i in range(0, len(datas)):
        print("Coordenada: ", datas[i], "Label: ", labels[i])
        plt.plot(datas[i][0], datas[i][1], colors[labels[i]], markersize=10)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
    plt.show()

kmeans = KMeans(n_clusters=3)

kmeans.fit(datas)
plotData();