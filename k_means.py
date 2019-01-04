# k-menas clustering
# D je množica točk
# k je število klastrov, ki jih želimo.

import numpy as np
import random
import math

def dist (p0x, p0y, p1x, p1y):
    return math.sqrt((p0x-p1x)**2 + (p0y - p1y)**2)

def my_mean(M):
    x = 0
    y = 0
    n = len(M)
    for i in range(n):
        x+=M[i][0]
        y+=M[i][1]
    return([x/n, y/n])


def k_means(D, k):
    n = len(D) # število točk, ki so dane.
    C = [] # centri, ki jih iščemo.
    i = 0
    izbrane = [] # na začetku naključno izberemo k danih točk.
    premik = [] # ko bo premik 0, se bo zanka ustavila.
    nic = [] # nicelni vektor s katerim primerjamo.
    while i < k: # izberemo k paroma različnih točk iz D
        j = random.randint(0,n-1)
        if j not in izbrane:
            izbrane.append(j)
            premik.append(1)
            nic.append(0)
            C.append(D[j])
            i += 1
    while premik != nic:
        G = [] # seznam kamor bomo shranjevali k seznamov z vozlišči,
                # ki so najbljižje izbrani točki.
        for i in range(k):
            G.append([])
        for i in range(len(D)): #klasificiramo točke v skupine
            oddaljenost = []
            for j in range(k):
                d = dist(D[i][0], D[i][1], C[j][0], C[j][1])
                oddaljenost.append(d)
            w = oddaljenost.index(min(oddaljenost)) # s, ki je najbližje
            G[w].append(D[i])
        for i in range(k):
            nov = my_mean(G[i])
            premik[i] = dist(nov[0], nov[1], C[i][0], C[i][1])
            C[i]= nov
    return (C)

m = 10
D = []
for i in range(m):
    l = random.uniform(3, 6)
    k = random.uniform(4, 5)
    D.append([l,k])
for i in range(m):
    l = random.uniform(-5, -3)
    k = random.uniform(-1, -4)
    D.append([l, k])
for i in range(m):
    l = random.uniform(0, 2)
    k = random.uniform(-1, 3)
    D.append([l, k])
print(k_means(D,3))