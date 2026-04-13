# ACAS Xu Benchmark

The Unmanned Aerial Vehicle Collision Avoidance System X (ACAS Xu) consists of 45 deep neural networks that used to determine the best course of action for an unmanned aircraft in proximity with another aircraft, to avoid collisions. Each neural network takes in five inputs: the distance between the aircrafts, the relative angle of each aircraft, and the speed of each aircraft. The output is another array of five integers giving a score to five different actions: weak left turn, strong left turn, weak right turn, strong right turn, or clear out of conflict. The action with the lowest score is the recommended action.

Each network has 6 hidden layers with 50 nodes each, forming a modest 300 nodes. However, on an unmanned aircraft with limited computing power it is of interest to reduce the size of such neural networks to make fast calculations while retaining accuracy. This can be achieved using various node pruning techniques such as weight pruning, node pruning, and quantization.

To ensure accuracy is retained, equivalence verification is used. Once the pruned network has been reconstructed to be isomorphic with the original, each network is given the same input tensor and the distance of the outputs is measured. If the distance is smaller or equal to the selected epsilon - the networks are equal. If the distance is greater than the selected epsilon then they are not equivalent.

This process has been named VeriPrune and is demonstrated in this VNN-LIB 2.0 benchmark. The input constraints are set to any possible input and if there is any possible input such that the output distance is greater than the epsilon then the specification is unsatisfied.

These benchmarks were compiled using networks and specifications from [Samuel Teuber](https://teuber.dev/).