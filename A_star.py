# algorithm A*
# G is weighted graph (V(G)=n and E(G)=m) given as list.
# G[i] is list of tuples (j,k) denoting e=(i,j) with cost k
# h is heuristic function given as list H = [h(0), h(1),...,h(n)]
# a is first node of path
# b is last node of path

import heapq

def A_star(graph, a, b, H):
    nodes = []
    path = []
    for i in range(len(graph)):
        path.append(0)
    path[a] = a
    cost = []

    for i in range(len(graph)):
        if i == a:
            nodes.append((0,a))
            cost.append(0)
        else:
            nodes.append((2**16, i)) #distance = infinity
            cost.append(2**16)
    heapq.heapify(nodes)
    while len(nodes)>0:
        (t,v) = heapq.heappop(nodes)
        for (i,j) in G[v]: # (i,j) = (node, cost)
            if cost[i] > t + j + H[i]:
                cost[i] = t + j + H[i]
                heapq.heappush(nodes, (t+j+H[i], i))
                path[i] = v
    c = b
    best_path = [c]
    while c != a:
        best_path.append(path[c])
        c = path[c]
    best_path = best_path[::-1]

    return best_path
G = [[(1,3),(4,3)],[],[(0,1),(1,2)],[(2,4),(0,7)],[(3,2)]]
H = [1,6,15,3,4]
b = 1
a = 4
print(A_star(G,a,b,H))
