pairs = [ x.strip().split(',') for x in open('day4.txt') ]

def parse(s): return [ int(x) for x in s.split('-') ]

pairs = [ (parse(x), parse(y)) for x,y in pairs ]

def contains(a,b,x,y):
    return (a>=x and b<=y) or (x>=a and y<=b)

print(len([1 for x,y in pairs if contains(*x,*y)]))

def overlap(a,b,x,y):
    return (a>=x and a<=y) or (b>=x and b<=y) or (x>=a and x<=b) or (y>=a and y<=b)

print(len([1 for x,y in pairs if overlap(*x,*y)]))
