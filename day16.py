import numpy as np

valves = [ l.strip().split() for l in open('test16.txt') ]
valves = { l[1]: ( int(l[4][5:-1]), [ v.replace(',', '') for v in l[9:]]) for l in valves }

for v in valves:
    print(v, valves[v])

g = np.zeros((len(valves), len(valves)))

idx = { v:i for i,v in enumerate(valves) }


for i,v in enumerate(valves):
    g[i,i] = valves[v][0]
    for o in valves[v][1]:
        g[i, idx[o]] = 1


print(g)
