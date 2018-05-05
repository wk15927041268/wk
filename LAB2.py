import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import datasets
iris = datasets.load_iris()
data = iris.data
def DENCLUE(data, eps=0.3, min_samples=10):
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(data)
    coreSampleMask = np.zeros_like(db.labels_, dtype = bool)
    coreSampleMask[db.core_sample_indices_] = True
    clusterLabels = iris.target
    uniqueClusterLabels = set(clusterLabels)
    colors = ['red', 'green', 'blue', 'black', 'gray', '#ff00ff', '#ffff00']
    markers = ['v', '^', 'o', '*', 'x', 'h', 'd']
    for i, cluster in enumerate(uniqueClusterLabels):
        clusterIndex = (clusterLabels == cluster)
        coreSamples = data[clusterIndex & coreSampleMask]
        plt.scatter(coreSamples[:, 0] + coreSamples[:, 1], coreSamples[:, 2] + coreSamples[:, 3],c=colors[i],  marker=markers[i], s=80)
        noiseSamples = data[clusterIndex & ~coreSampleMask]
        plt.scatter(noiseSamples[:, 0] + noiseSamples[:, 1],noiseSamples[:, 2] + noiseSamples[:, 3], c=colors[i], marker=markers[i], s=26)
    plt.show()
DENCLUE(data, 10, 10)
