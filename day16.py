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

valves = list(valves)

aa = valves.index('AA')

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

cache = {}

def find_best(options, here=aa, time=30):

    if not options: return [], 0

    key = (options, here, time)

    #if key in cache: return cache[key][0], cache[key][1]

    b = 0
    res = []
    for v in options:
        new_time = time-paths[here,v]-1
        if new_time <= 0: continue

        r, s = find_best(options - {v}, v, new_time)

        s += new_time*flows[v]
        r = [v] + r

        if s > b:
            b = s
            res = r

    cache[key] = res, b

    return res, b

solution, score = find_best(frozenset(flow_valves))

print(solution)


print('possible:')
for v in flow_valves: print(valves[v], flows[v])

print('solution:')
time = 30
here = aa
for step in solution:
    time -= paths[here, step] + 1
    here = step
    print(time, valves[step], flows[step])

print(score)

#print(cache)
