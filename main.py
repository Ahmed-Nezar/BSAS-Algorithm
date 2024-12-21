from bsas import BSAS
import numpy as np
from utils import *


data_points = [
    (2, 3),  # x8
    (5, 4),  # x6
    (9, 2),  # x11
    (2, 5),  # x1
    (1, 4),  # x5
    (6, 4),  # x2
    (5, 3),  # x3
    (2, 2),  # x4
    (3, 3),  # x7
    (8, 2),  # x10
    (2, 4),  # x9
    (10, 2),  # x12
    (11, 2),  # x13
    (10, 3),  # x14
    (9, 1),  # x15
]

data_array = np.array(data_points)

bsas_model = BSAS(max_distance=2.5, max_clusters=15, distance_metric='euclidean')

bsas_model.fit(data_array)

print("Cluster Labels: ", bsas_model.labels)

output_list = save_output_labels(bsas_model, data_array)

save_output_json(output_list, "output.json")
