from bsas import BSAS
from pyclustering.cluster.bsas import bsas
from pyclustering.utils.metric import distance_metric, type_metric

def get_ground_truth(data_points, clusters):
    ground_truth_labels = []
    for i in range(len(data_points)):
        for j in range(len(clusters)):
            if i in clusters[j]:
                ground_truth_labels.append(j)
                break
    return ground_truth_labels



# Test 1
data_points = [
    (2, 5),  
    (6, 4),  
    (5, 3),  
    (2, 2),  
    (1, 4),  
    (5, 4),  
    (3, 3),  
    (2, 3),  
    (2, 4),  
    (8, 2),  
    (9, 2),  
    (10, 2), 
    (11, 2), 
    (10, 3), 
    (9, 1)   
]

bsas_model = BSAS(max_distance=1.5, max_clusters=3, distance_metric='euclidean')
bsas_model.fit(data_points)

metric = distance_metric(type_metric.EUCLIDEAN)
bsas_instance = bsas(data_points, 3, 1.5, metric)
bsas_instance.process()
clusters = bsas_instance.get_clusters()
representatives = bsas_instance.get_representatives()

ground_truth_labels = get_ground_truth(data_points, clusters)

if bsas_model.labels == ground_truth_labels:
    print(f"\033[92mTest 1 passed\033[0m")
    
else:
    print(f"\033[91mTest 1 failed\033[0m")


# Test 2
bsas_model = BSAS(max_distance=0.5, max_clusters=8, distance_metric='euclidean')
bsas_model.fit(data_points)

metric = distance_metric(type_metric.EUCLIDEAN)
bsas_instance = bsas(data_points, 8, 0.5, metric)
bsas_instance.process()
clusters = bsas_instance.get_clusters()

ground_truth_labels = get_ground_truth(data_points, clusters)

if bsas_model.labels == ground_truth_labels:
    print(f"\033[92mTest 3 passed\033[0m")

else:
    print(f"\033[91mTest 3 failed\033[0m")


# Test 3
bsas_model = BSAS(max_distance=0.5, max_clusters=8, distance_metric='manhattan')
bsas_model.fit(data_points)

metric = distance_metric(type_metric.MANHATTAN)
bsas_instance = bsas(data_points, 8, 0.5, metric)
bsas_instance.process()
clusters = bsas_instance.get_clusters()

ground_truth_labels = get_ground_truth(data_points, clusters)

if bsas_model.labels == ground_truth_labels:
    print(f"\033[92mTest 3 passed\033[0m")

else:
    print(f"\033[91mTest 3 failed\033[0m")

