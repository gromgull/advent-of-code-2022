import numpy as np
from queue import PriorityQueue

m = [ [ ord(c)-97 if c not in 'SE' else c for c in l.strip() ] for l in open('day12.txt') ]

for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == 'S':
            start = (i,j)
            m[i][j] = 0
        if m[i][j] == 'E':
            end = (i,j)
            m[i][j] = 25

m = np.array(m)

print(m)

edge = PriorityQueue()
edge.put((0, start))
visited = set()

w,h = m.shape

while not edge.empty():

    d, (x,y) = edge.get()
    if (x,y) in visited: continue
    visited.add((x,y))
    if (x,y) == end:
        break
    nexts = [ (x-1, y), (x+1, y), (x, y-1), (x, y+1) ]

    for (nx,ny) in nexts:
        if nx < 0 or nx >= w or ny < 0 or ny >= h: continue
        if (nx,ny) in visited: continue
        if m[nx, ny] > m[x,y]+1: continue

        edge.put((d+1, (nx, ny)))

print(d)


edge = PriorityQueue()
edge.put((0, end))
visited = {}

w,h = m.shape

while not edge.empty():

    d, (x,y) = edge.get()
    if (x,y) in visited: continue
    visited[(x,y)] = d
    nexts = [ (x-1, y), (x+1, y), (x, y-1), (x, y+1) ]

    for (nx,ny) in nexts:
        if nx < 0 or nx >= w or ny < 0 or ny >= h: continue
        if (nx,ny) in visited: continue
        if m[nx, ny] < m[x,y]-1: continue

        edge.put((d+1, (nx, ny)))

print(min(visited[n] for n in zip(*(m==0).nonzero()) if n in visited))
