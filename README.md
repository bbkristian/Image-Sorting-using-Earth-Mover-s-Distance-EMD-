# Image-Sorting-using-Earth-Mover-s-Distance-EMD

This project includes Python code that sorts a set of images based on their EMD distances.

### What is Earth Mover's Distance (EMD)?

Earth Mover's Distance (EMD), also known as the Wasserstein metric, is a measure of the similarity between two probability distributions over a given region. In the context of image comparison, EMD is a way to calculate the difference between two images based on the distribution of their pixel intensities.

EMD can be thought of as the minimum amount of work required to transform one distribution into the other, where work is measured as the product of the amount of mass moved and the distance it is moved. Mathematically, it is defined as the minimum cost of transporting mass from one distribution to another.

### Minimum Cost Flow Problem

The EMD problem can be formulated as a minimum cost flow problem in a bipartite graph. A bipartite graph is a graph that consists of two disjoint sets of vertices, with edges connecting vertices from one set to the other. In this case, each set of vertices represents the pixel intensities of one of the two images being compared.

Each edge in the bipartite graph has a cost associated with it, which represents the distance between the two pixels connected by the edge. The goal is to find the flow of mass between the vertices that minimizes the total cost while satisfying the constraints on the amount of mass that can be transported.

We want to find a flow $F = [f_{i,j}]$ with $f_{i,j}$ being the flow between $p_i$ and $q_j$ that minimizes the overall cost.

$\underset{F}{\min}$ $\sum \sum f_{i,j}d_{i,j}$ , with $d_{i,j}$ being the distance between $p_i$ and $q_j$.


### Code Overview

The provided code performs the following tasks:

1. Converts text files containing image data into NumPy arrays.
2. Normalizes the distribution of pixels in every image.
3. Calculates the EMD distance between pairs of images using NetworkX to solve the minimum cost flow problem.
4. Sorts the images based on their EMD distances.

You can find the full code for this project in the repository under the `emd_image_sorting` folder.
