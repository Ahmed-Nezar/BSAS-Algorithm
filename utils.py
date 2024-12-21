import numpy as np
import json
import os


def save_output_labels(bsas_model, data_array):
    output_list = []
    for labels in np.unique(bsas_model.labels):
        output_dict = {}
        output_dict["Cluster"] = int(labels + 1) 
        output_dict['Members'] = data_array[np.where(bsas_model.labels == labels)].tolist()
        output_dict['Mean'] = np.mean(data_array[np.where(bsas_model.labels == labels)], axis=0).tolist()
        output_list.append(output_dict)
    return output_list


def save_output_json(output_list, output_file):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(base_dir, output_file)
    with open(output_file, 'w') as f:
        json.dump(output_list, f, indent=2)
    
    print(f"\033[92mOutput saved to {output_file}\033[0m")