# BSAS-Algorithm

Implementing the Basic Sequential Algorithmic Scheme (BSAS) from scratch.

## Directory Structure

```
BSAS-Algorithm/
├── main.py       # Entry point for running the BSAS algorithm
├── tests.py      # Unit tests for the BSAS implementation
├── bsas.py       # Core BSAS algorithm implementation
├── utils.py      # Utility functions for saving and processing data
├── output.json   # Example output of clustering results
└── README.md     # Documentation for the project
```

## Files Overview

### 1. `main.py`
This file demonstrates how to use the `BSAS` class to cluster a set of data points. Key steps include:

- Loading data points.
- Initializing the `BSAS` model with parameters like maximum distance, maximum clusters, and distance metric.
- Fitting the model to data points.
- Saving the cluster labels and output results to a JSON file.

### 2. `tests.py`
Contains unit tests to validate the functionality of the `BSAS` implementation. It compares the clustering results of the custom `BSAS` class with a reference implementation (`pyclustering.cluster.bsas`).

### 3. `bsas.py`
Defines the `BSAS` class, which implements the Basic Sequential Algorithmic Scheme. Key features:

- Configurable distance metric (`euclidean` or `manhattan`).
- Dynamic updating of centroids and clusters based on input data points.
- Handles clustering constraints like maximum clusters and distance thresholds.

### 4. `utils.py`
Provides utility functions for:

- Saving clustering results (labels, members, and means) as a JSON file.
- Computing and organizing cluster data for easy interpretation.

### 5. `output.json`
An example output file containing clustering results, including cluster members and their means.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd BSAS-Algorithm
   ```

2. Install required dependencies:
   ```bash
   pip install numpy
   ```

3. Run the main script:
   ```bash
   python main.py
   ```
   The clustering results will be saved to `output.json`.

4. Run the tests:
   ```bash
   python tests.py
   ```
   The tests will validate the correctness of the implementation.

## Example Output

An example of clustering results saved in `output.json`:

```json
[
  {
    "Cluster": 1,
    "Members": [
      [2, 3],
      [2, 5],
      [1, 4],
      [2, 2],
      [3, 3],
      [2, 4]
    ],
    "Mean": [
      2.0,
      3.5
    ]
  },
  {
    "Cluster": 2,
    "Members": [
      [5, 4],
      [6, 4],
      [5, 3]
    ],
    "Mean": [
      5.333333333333333,
      3.6666666666666665
    ]
  }
]
```

## Key Features

- **Customizable Parameters**: Supports adjusting maximum distance, maximum clusters, and distance metric.
- **Real-Time Centroid Updates**: Dynamically recalculates cluster centroids as new points are added.
- **Efficient Clustering**: Implements the BSAS algorithm efficiently with minimal dependencies.

## Dependencies

- Python 3.6+
- `numpy`

## Contributing

Feel free to contribute by submitting issues or pull requests. Please follow the project structure and maintain clean, readable code.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

