import copy
import itertools
from collections import defaultdict

def chunk(l, n):

    return itertools.groupby(zip(itertools.count(), l), lambda x: x[0]//n)

lines = [ x for x in open('day5.txt') ]

crates = defaultdict(list)

for i,l in enumerate(lines):
    if ']' not in l: break
    for j,x in chunk(l, 4):
        c = list(x)[1][1]
        if c == ' ': continue
        crates[1+j].append(c)

moves = []
for l in lines[i+2:]:
    _,c,_,f,_,t = l.strip().split(' ')
    moves.append((int(c),int(f),int(t)))

orig_crates = copy.deepcopy(crates)

for c,f,t in moves:
    for i in range(c):
        crates[t].insert(0,crates[f].pop(0))

print(''.join([x.pop(0) for _,x in sorted(crates.items())]))

crates = orig_crates

for c,f,t in moves:
    print(crates)
    for i in range(c):
        crates[t].insert(0, crates[f].pop(c-i-1))

print(crates)
print(''.join([x.pop(0) for _,x in sorted(crates.items())]))
