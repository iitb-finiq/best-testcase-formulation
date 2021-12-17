# Best Testcase Formulation

## Problem Overview
Currently, to test the Payoff Variation for various Autocall prodecures, either the entire dataset is tested or the best testcases to test are intiutively chosen. However, this might lead to inconsistencies and be a time consuming process. The task was to computationally formulated a method to select the best testcases that could represent the entire dataset. One could extrapolate the result of testing this best chosen dataset for the complete procedure. 

## Solution Overview
To mathematically formulate the problem, we encoded the features corresponding to a Autocall procedure (ex: strike shift, autocall frequency) in a class `Object`. We then defined the model distribution of the procedure. Ex: strike shift should have 80% Tdy and 20% Fwd. 

Initially, we began with a randomly selected set of testcases and applied genetic algorithm to come up with best representitive set of testcases. The objective function was to minimise the KL Divergence between the model distribution defined aboved and empricial distribution of the set selected.

## File System
- `genetic_algorithm.py`: this file has the genetic algorithm which finds the optimal best testcases to represent the entire dataset. The objective function used by the algorithm is the KL divergence between the model distribution and the formulated distribution.

- `object.py`: contains the class `Object` corresponding to the features and the model distribution of the **Standard Autocall** dataset. KL Divergence is also defined along with the class in this file.

- `data_transform.py`: used to read the complete dataset (from excel) and transform into the input format for the object. The inputs are then coverted into the `Object` class and stored in the list `S`.

- `plot.py`: is used to set parameters for calling the genetic algorithm. It also plots the variation of the KL divergence with respect to the basket size of best population.

## Running the Code
To run & test the code, you just need to run `plot.py`, it computes the best testcases for different population size and plots a variation of the KL Divergence with respect to the basket size. These parameters can be controlled to tune algorithm and produce better results:

- `n_iter`: define the total iterations
- `n_obj`: define the basket size
- `n_pop`: define the population size
- `r_cross`: crossover rate
- `r_mut`: mutation rate

## Usage 
To use the code for generating best testcases samples, following things need to be changed:

- `Object` class: Modify the class to encode features corresponding to the prodcedure type (Ex: new features need to be added for Fixed Couppon AC). 
- Model distribution `q(x)` should have different probability corresponding to new features.

## Reference
- Genetic Algorithm: https://en.wikipedia.org/wiki/Genetic_algorithm 
- KL Divergence: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence 