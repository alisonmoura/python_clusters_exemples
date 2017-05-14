import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import KMeans

style.use("ggplot")

X = np.array(
    [
        [1, 2],
        [5, 8],
        [1.5, 1.8],
        [8, 8],
        [1, 0.6],
        [9, 11]
    ]
)

def plotData():
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    print(centroids)
    print(labels)
    colors = ["g.", "r."]
    for i in range(len(X)):
        print("Coordenada: ", X[i], "Label: ", labels[i])
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker="x", s=150, linewidths=5, zorder=10)
    plt.show()

kmeans = KMeans(n_clusters=2)

kmeans.fit(X)
plotData();

kmeans.fit(X)
plotData();

kmeans.fit(X)
plotData();