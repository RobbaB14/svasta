# k-menas clustering

# X... (n*d) matrix
# k... number of clusters

import numpy as np
import random


def k_means(X, k):
    n = len(X) # number of given points
    d = len(X[0]) # dimension
    centres = np.zeros((k,d))
    i = 0
    chosen_lines = [] # we choose k points (k lines in X)
    move = np.ones((1,k)) # vector of distance between last end new C
    zero = np.zeros((1,k))
    while i < k: # We choose k points from X and put them in C
        j = random.randint(0,n-1)
        if j not in chosen_lines:
            chosen_lines.append(j)
            centres[i]=(X[j])
            i += 1

    while np.linalg.norm(move-zero) != 0:
        partition = [] # current partition
        for i in range(k):
            partition.append([])
        for i in range(len(X)):
            distance = []
            for j in range(k):
                distance.append(np.linalg.norm(X[i]-centres[j]))
            nearest_c = distance.index(min(distance))
            partition[nearest_c].append(X[i])
        for i in range(k):
            new_s = np.mean(partition[i], axis=0)
            move[0][i] = np.linalg.norm(new_s-centres[i])
            centres[i]= new_s
    return (centres)

# example of input:
m = 4
d = 4
Y_1 = 2*np.random.rand(m,d)+[-2,-2,0,0]
X = Y_1
Y_2 = np.random.rand(m,d)+ [0,0,1,1]
X = np.r_[X,Y_2]
Y_3 = np.random.rand(m,d) + [0,3,3,0]
X = np.r_[X,Y_3]
print(k_means(X,3))