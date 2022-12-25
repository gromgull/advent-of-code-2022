import sys
sys.setrecursionlimit(15000)


cubes = { tuple(map(int, l.strip().split(','))) for l in open('day18.txt') }

done = set()

def move(c,i,d):
    new = list(c)
    new[i] += d
    return tuple(new)

def count(c):

    if c in done: return 0
    done.add(c)

    res = 0
    for i in range(3):
        for d in [-1,1]:
            m = move(c,i,d)
            if m in cubes:
                res += count(m)
            else:
                res += 1


    return res

print(len(cubes))
print(sum(count(c) for c in cubes))
print(len(done))

# part 2

bounds = [ max(c[i] for c in cubes) for i in range(3) ]
print(bounds)

outside = set()

def in_bounds(c):
    return not any(c[i]<-1 or c[i]>bounds[i]+1 for i in range(3))

def fill(c):

    if c in outside: return 0
    outside.add(c)

    for i in range(3):
        for d in [-1,1]:
            m = move(c,i,d)
            if not in_bounds(m): continue
            if m not in cubes:
                fill(m)

if (0,0,0) in cubes: raise Exception('0,0,0 in cubes')
fill((0,0,0))

done = set()

def count2(c):

    if c in done: return 0
    done.add(c)

    res = 0
    for i in range(3):
        for d in [-1,1]:
            m = move(c,i,d)
            if m in cubes:
                res += count2(m)
            elif m in outside:
                res += 1



    return res

print(sum(count2(c) for c in cubes))
