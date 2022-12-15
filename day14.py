import numpy as np


def r(start, stop):
    return np.arange(min(start,stop), max(start, stop)+1)

def ar(start, stop):
    x1,y1 = start
    x2,y2 = stop

    res = [ (x1, y) for y in r(y1,y2) ] if x1 == x2 else [ (x, y1) for x in r(x1,x2) ]
    return [ r[0] for r in res ], [ r[1] for r in res ]

def down(s): return (s[0], s[1]+1)
def left_down(s): return (s[0]-1, s[1]+1)
def right_down(s): return (s[0]+1, s[1]+1)

def prnt(w):
    print('\n'.join([ ''.join([ ['.', '#', 'o'][c] for c in l ]) for l in w ]))

floor = True

walls = [ [list(map(int, c.split(','))) for c in l.strip().split(' -> ')] for l in open('day14.txt') ]

wxmin = min(min(c[0] for c in w) for w in walls)-1
wxmax = max(max(c[0] for c in w) for w in walls)+2
wymin = min(min(c[1] for c in w) for w in walls)-1
wymax = max(max(c[1] for c in w) for w in walls)+2

wxmin -= wymax
wxmax += wymax

print(wxmin, wxmax, wymin, wymax)

world = np.zeros((wxmax-wxmin,wymax+1), dtype=int)

walls = [ [(cx-wxmin, cy) for cx,cy in w] for w in walls]

for w in walls:
    for i in range(1, len(w)):
        world[ar(w[i-1],w[i])] = 1

if floor:
    world[:,-1] = 1

prnt(world.T)

n = 0
while True:
    s = (500-wxmin, 0)
    oob = False
    while True:
        try:
            if not world[down(s)]:
                s = down(s)
            elif not world[left_down(s)]:
                s = left_down(s)
            elif not world[right_down(s)]:
                s = right_down(s)
            else:
                world[s] = 2
                break
        except IndexError:
            oob = True
            break
    #prnt(world.T)
    if oob: break
    n += 1
    if floor and s == (500-wxmin, 0): break

prnt(world.T)
print(n)
