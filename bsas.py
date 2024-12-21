import numpy as np

class BSAS:
    def __init__(self, max_distance, max_clusters, distance_metric='euclidean'):
        self.max_distance = max_distance
        self.max_clusters = max_clusters
        self.cluster = 0
        self.clusters = {}
        self.distance_metric = distance_metric
    
    def fit(self, X):
        self.centroids = [np.array(X[0])]
        self.labels = [self.cluster]
        self.clusters[self.labels[0]] = [np.array(X[0])]
        for i in range(1, len(X)):
            
            distances = [self._distance(np.array(X[i]), centroid) for centroid in self.centroids]
            if min(distances) > self.max_distance and self.cluster < self.max_clusters:
                self.cluster += 1
                self.centroids.append(np.array(X[i]))
                self.labels.append(self.cluster)
                self.clusters[self.cluster] = [np.array(X[i])]
            else:
                self.labels.append(distances.index(min(distances)))
                self.clusters[self.labels[-1]].append(np.array(X[i]))
                self.centroids[self.labels[-1]] = np.mean(np.array(self.clusters[self.labels[-1]]), axis=0)

    def _distance(self, x, y):
        if self.distance_metric == 'euclidean':
            distance = np.linalg.norm(x - y)
        elif self.distance_metric == 'manhattan':
            distance = np.sum(np.abs(x - y))
        else:
            raise ValueError("Invalid distance metric")    
        return distance