import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import KMeans

style.use("ggplot")

datas = []

file = open("house.txt")
# print file.readlines()
for line in file:
    line = line.split(' ')
    line = [x.strip() for x in line if x.strip()]
    print line
    datas.append(line)

print datas

def plotData():
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    print(centroids)
    print(labels)
    colors = ["g.", "r.", "b.", "y.", "k."]
    for i in range(0, len(datas)):
        print("Coordenada: ", datas[i], "Label: ", labels[i])
        plt.plot(datas[i][0], datas[i][1], colors[labels[i]], markersize=5)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
    plt.show()

kmeans = KMeans(n_clusters=5)

kmeans.fit(datas)
plotData();
