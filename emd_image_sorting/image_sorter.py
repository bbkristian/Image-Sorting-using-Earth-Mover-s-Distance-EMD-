import numpy as np
import networkx as nx

# Convert text file to numpy array
def f(filename):
    l = list()
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            l.append(list(line)[:-1])
    if filename == "P13.txt":
        return np.array(l[:-1], dtype=int)
    return np.array(l, dtype=int)   

# Distance in indexes between nodes
def dist_node(c_1,c_2):
    if c_1 > c_2:
        return 80 - c_1 + c_2
    return c_2 - c_1


# Calculate min cost flow   
def flow(file1,file2):
    # Convert text files into numpy array and normalize to 1
    f1 = f(file1)/sum(sum(f(file1)))
    f2 = f(file2)/sum(sum(f(file2)))
    G = nx.DiGraph()
    G.add_node("s", demand = -1.0) # Source
    G.add_node("t", demand = +1.0) # Sink
    G.add_edge("s", "t", capacity = 1e-15, weight = 0) # Add edge to compensate for float error

    l1 = [] # List of nodes with capacity non-zero in image 1
    l2 = [] # List of nodes with capacity non-zero in image 2

    # Generate nodes for two images for nodes with non-zero capacity
    for i in range(f1.shape[0]):
        for j in range(f1.shape[1]):
            if f1[i][j] != 0:
                G.add_node(f"f1({i},{j})")
                l1.append([f"f1({i},{j})",f1[i][j], j]) # Append [node, capacity, column]
            if f2[i][j] != 0:
                G.add_node(f"f2({i},{j})")
                l2.append([f"f2({i},{j})",f2[i][j], j]) # Append [node, capacity, column]
    
    # Generates edges between source and nodes of first graph
    for node in l1:
        G.add_edge("s", node[0], capacity = node[1])

    # Generates edges between nodes of the second graph and sink
    for node in l2:
        G.add_edge(node[0], "t", capacity = node[1])
    
    # Generates inbetween nodes
    for node1 in l1:
        for node2 in l2:
            G.add_edge(node1[0], node2[0], weight = dist_node(node1[2], node2[2]), capacity = min(node1[1], node2[1]))
    return nx.min_cost_flow(G), l1, l2


# This function should return the EMD distances between file1 and file2.
# EMD distance depends on your choice of distance between pixels and
# this will be taken into account during grading.
def comp_dist(file1, file2):
    distance = 0
    d , l1, l2 = flow(file1,file2)
    for node1 in l1:
        for node2 in l2:
            distance += d[node1[0]][node2[0]]*dist_node(node1[2],node2[2])
    return float(distance)

def sort_files():
    files = ['P1.txt', 'P2.txt', 'P3.txt', 'P4.txt', 'P5.txt', 'P6.txt', 'P7.txt', 'P8.txt', 'P9.txt', 'P10.txt', 'P11.txt', 'P12.txt', 'P13.txt', 'P14.txt', 'P15.txt']
    sorted_files = []
    current = "P1.txt"
    while files:
        files.remove(current)
        sorted_files.append(current)
        m = float('inf')
        n = 0
        for file in files:
            if (comp_dist(current, file)) < m:
                m = comp_dist(current, file)
                n = file
        current = n
    return sorted_files
