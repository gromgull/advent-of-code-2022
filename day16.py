from queue import PriorityQueue
import numpy as np
from itertools import permutations

valves = [ l.strip().split() for l in open('day16.txt') ]
valves = { l[1]: ( int(l[4][5:-1]), [ v.replace(',', '') for v in l[9:]]) for l in valves }

for v in valves:
    print(v, valves[v])

g = np.zeros((len(valves), len(valves)),dtype=int)

idx = { v:i for i,v in enumerate(valves) }


for i,v in enumerate(valves):
    g[i,i] = valves[v][0]
    for o in valves[v][1]:
        g[i, idx[o]] = 1


print(g)


def shortest(start):
    edge = PriorityQueue()
    edge.put((0, start))
    visited = np.full(g.shape[0], -1)

    while not edge.empty():

        d, n = edge.get()
        if visited[n] != -1: continue
        visited[n] = d

        nexts = g[n].nonzero()[0]

        for nn in nexts:
            if nn == n: continue
            if visited[nn] != -1: continue

            edge.put((d+1, nn))

    return visited


paths = np.zeros(g.shape, dtype=int)

for i in range(paths.shape[0]):
    paths[i] = shortest(i)



flows = g.diagonal()
flow_valves = list(flows.nonzero()[0])
print(len(flow_valves))

# hah!
# n = 0
# for x in permutations(list(g.diagonal().nonzero()[0])):
#     n += 1
# print(n)

def score(order):

    n = 0
    flow = 0
    time = 30
    for o in order:
        if time<0: break
        flow += (time - paths[n,o] - 1)*flows[o]
        time -= paths[n,o]+1
        n = o

    print(order, flow)
    return flow



def find_best(options, best=0, sol=[], time=30):

    if not options: return sol, score(sol)

    max_score = score(sol) + time*flows[ [ v for v in flow_valves if v not in sol ]].sum()
    if max_score<best:
        return None, None

    b = 0
    res = None
    for v in options:
        if v in sol: continue

        r, s = find_best(options - {v}, best, sol+[v], time-paths[sol[-1] if sol else 0,v]-1)
        if r is None: continue
        if s>b:
            b = s
            res = r

    return res, b

print(find_best(frozenset(flow_valves)))
