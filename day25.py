DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '-': -1,
    '=': -2,
}

SNAFU = '=-012'

fives = [ 5**n for n in range(1,20) ]

def to_int(s):

    res = 0
    p = 1
    for c in reversed(s):
        res += DIGITS[c]*p
        p *= 5

    return res

def from_int(n):

    res = ''

    for i,f in enumerate(fives):

        r = n % f
        print(n, f, r)
        res += SNAFU[r]
        n -= r


    return res[::-1].lstrip('0')

numbers = [ s.strip() for s in open('test25.txt') ]


for s in numbers:
    print(s, to_int(s), from_int(to_int(s)))

print(sum(to_int(s) for s in numbers))

#print(from_int(3))
