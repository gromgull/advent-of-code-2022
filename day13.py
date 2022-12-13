import itertools
import functools
def chunk(l, n):
    return itertools.groupby(zip(itertools.count(), l), lambda x: x[0]//n)

def cmp(x,y):

    if x is None and y is None:
        return 0
    elif x is None and y is not None:
        return -1
    elif x is not None and y is None:
        return 1
    elif isinstance(x,int) and isinstance(y, int):
        return (x > y) - (x < y)
    elif isinstance(x, list) or isinstance(y, list):
        if not isinstance(x, list): x = [x]
        if not isinstance(y, list): y = [y]
        for a,b in itertools.zip_longest(x,y):
            if c := cmp(a,b):
                return c




pairs = [ [eval(i[1]) for i in list(p)[:2]] for _,p in chunk(open('day13.txt'), 3)]
cmps = [ cmp(x,y) for x,y in pairs ]
print(sum(i+1 for i,c in enumerate(cmps) if c < 0))

lst = [ x for s in pairs for x in s ]
lst += [ [[2]], [[6]] ]

lst = sorted(lst, key=functools.cmp_to_key(cmp))

print((lst.index([[2]])+1)*(lst.index([[6]])+1))
