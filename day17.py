import numpy as np
from itertools import cycle

winds = open('day17.txt').read().strip()

winds = [ 1 if w == '>' else -1 for w in winds ]

blocks = set()

pieces = [
    [ (0,0), (1,0), (2,0), (3,0) ],
    [ (1,0), (0,1), (1,1), (2,1), (1,2) ],
    [ (0,0), (1,0), (2,0), (2,1), (2,2) ],
    [ (0,0), (0,1), (0,2), (0,3) ],
    [ (0,0), (0,1), (1,0), (1,1) ],
    ]

widths = [ 1+max(x for x,y in p ) for p in pieces ]
heights = [ 1+max(y for x,y in p ) for p in pieces ]

print(widths, heights)

def blocked(piece, xd, yd):

    return any((x+xd, y+yd) in blocks or x+xd>6 or x+xd<0 or y+yd<0 for x,y in piece)

def rest(piece, xp, yp):
    for x,y in piece:
        blocks.add((x+xp, y+yp))

def display(top):

    for y in range(top,-1,-1):
        print(''.join('#' if (x,y) in blocks else '.' for x in range(7)))

top = 0
wind = cycle(winds)

DEBUG = False

for i, (p, w, h) in enumerate(zip(cycle(pieces), cycle(widths), cycle(heights))):

    if i>=2022: break

    y = top+3
    x = 2

    while True:
        d = next(wind)

        print(x,y)
        if not blocked(p, x+d, y):
            x += d
            if DEBUG: print('x', d)

        if not blocked(p, x, y-1):
            if DEBUG: print('down')
            y -= 1
        else:
            rest(p, x, y)
            if DEBUG: print('rest')
            top = max(y for x,y in blocks)+1
            break

    if DEBUG: display(top)


print(top)
