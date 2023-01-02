import numpy as np
inp = [ [ 0 if c=='.' else 1 for c in l.strip()] for l in open('day23.txt') ]

start = np.array(inp)

print(start)

DIRS = [
    ( 0, np.array((-1,0)) ),
    (-1, np.array(( 1,0)) ),
    ((slice(None),0), np.array((0,-1))),
    ((slice(None),-1), np.array((0, 1))),
]

def trim(a):
    while np.all(a[0] == 0): a = a[1:]
    while np.all(a[-1] == 0): a = a[:-1]
    while np.all(a[:,0] == 0): a = a[:,1:]
    while np.all(a[:,-1] == 0): a = a[:,:-1]
    return a



def step(m):

    m = np.pad(m, ((1,1),(1,1)))

    nxs = []

    for y,x in zip(*m.nonzero()):

        sm = m[y-1:y+2, x-1:x+2]

        if len(sm.nonzero()[0]) == 1: continue

        for i,d in DIRS:
            if np.all(sm[i] == 0):
                nxs.append(((y,x), tuple((y,x)+d)))
                break

    if not nxs:
        raise Exception('no one moves!')

    nextmap = np.copy(m)
    for _,n in nxs:
        nextmap[n] += 1

    for o,nx in nxs:
        if nextmap[nx] == 1:
            nextmap[o] = 0

    nextmap[nextmap>1] = 0

    return trim(nextmap)

m = np.copy(start)
for i in range(10):
    m = step(m)
    DIRS.append(DIRS.pop(0))
    print(m)


print(m.size-len(m.nonzero()[0]))

DIRS = [
    ( 0, np.array((-1,0)) ),
    (-1, np.array(( 1,0)) ),
    ((slice(None),0), np.array((0,-1))),
    ((slice(None),-1), np.array((0, 1))),
]

m = np.copy(start)
n = 0
while True:
    try:
        m = step(m)
        DIRS.append(DIRS.pop(0))
        n += 1
    except:
        break

print(n+1)
