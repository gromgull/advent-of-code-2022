import itertools

packs = [ l.strip() for l in open('day3.txt') ]
packs = [ (l[:len(l)//2],l[len(l)//2:]) for l in packs ]

def prio(c):
    if c.islower(): return ord(c)-96
    if c.isupper(): return ord(c)-38

print(sum(prio(list(set(x).intersection(y))[0]) for x,y in packs))

def chunk(l, n):

    return itertools.groupby(zip(itertools.count(), l), lambda x: x[0]//3)

def badge(l):
    _,x = next(l)
    res = set(x[0]+x[1])
    for _,x in l:
        res.intersection_update(x[0]+x[1])
    return list(res)[0]

print(sum(prio(badge(x)) for _,x in chunk(packs, 3)))
