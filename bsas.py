import numpy as np

class BSAS:
    def __init__(self, min_distance, max_clusters):
        self.min_distance = min_distance
        self.max_clusters = max_clusters
        self.cluster = 0
        self.clusters = {}
    
    def fit(self, X):
        self.centroids = [X[0]]
        self.labels = [self.cluster]
        self.clusters[self.labels[0]] = [X[0]]
        for i in range(1, len(X)):
            
            distances = [self._distance(X[i], centroid) for centroid in self.centroids]
            if min(distances) > self.min_distance and self.cluster < self.max_clusters:
                self.cluster += 1
                self.centroids.append(X[i])
                self.labels.append(self.cluster)
            else:
                self.labels.append(distances.index(min(distances)))
                if self.labels[-1] in self.clusters:
                    self.clusters[self.labels[-1]].append(X[i])
                    self.centroids[self.labels[-1]] = np.mean(self.clusters[self.labels[-1]], axis=0)
                else:
                    self.clusters[self.labels[-1]] = [X[i]]
                    self.centroids[self.labels[-1]] = X[i]

    def _distance(self, x, y):
        return np.linalg.norm(x - y)