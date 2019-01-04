# alogirtem A*
# G naj bo obtežen usmerjen graf (z n vozlišči in m povezavami)
# podan kot seznam n seznamov:
    # za vsako vozlišče i podamo seznam parov (j, k), kjer je
    # i vozlišče v katerem se poezava začne
    # j vozlišče v katerem se povezava konča
    # k utež na povezavi med i in j.
# h je heveristična funkcija, ki deluje na vozliščih. Podana je v obliki
# seznama H = [h(0), h(1), h(2), ...h(n)]
# a je številka vozlišča, v katerem začnemo iskanje optimalne poti
# b je številka vozlišča v katerem želimo končati pot.

import heapq

def A_star(G, a, b, H):
    seznam = []
    pot = []
    for i in range(len(G)):
        pot.append(0)
    pot[a] = a
    cena_poti = []

    for i in range(len(G)):
        if i == a:
            seznam.append((0,a))
            cena_poti.append(0)
        else:
            seznam.append((2**16, i)) #razdalije nastavimo na 'neskončno'.
            cena_poti.append(2**16)
    # print(seznam)
    # print(cena_poti)
    heapq.heapify(seznam) # naredimo kopico.
    while len(seznam)>0:
        (t,v) = heapq.heappop(seznam) # najcenejše vozlišče in njegova cena
        for (i,j) in G[v]: # i je vozlišče, j je utež na povezavi do vozlišča
            # print(H[i])
            if cena_poti[i] > t + j + H[i]:
                cena_poti[i] = t + j + H[i]
                heapq.heappush(seznam, (t+j+H[i], i))
                pot[i] = v
    c = b
    iskana_pot = [c]
    while c != a:
        iskana_pot.append(pot[c])
        c = pot[c]
    iskana_pot[::-1]

    return iskana_pot
G = [[(1,3),(4,3)],[],[(0,1),(1,2)],[(2,4),(0,7)],[(3,2)]]
H = [1,6,15,3,4]
b = 1
a = 4
print(A_star(G,a,b,H))
