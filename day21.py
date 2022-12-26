import operator as op
monkeys = { l[:4]: l[6:-1] for l in open('day21.txt') }

monkeys = { k: v.split(' ') if ' ' in v else int(v) for k,v in monkeys.items() }

OPS = {
    '+': op.add,
    '*': op.mul,
    '/': op.truediv,
    '-': op.sub
}

def solve(m):

    v = monkeys[m]
    if isinstance(v, int): return v

    a,o,b = v
    return OPS[o](solve(a), solve(b))

print(solve('root'))

import sympy

def solve2(m):

    if m == 'humn':
        return sympy.var('humn')

    v = monkeys[m]
    if isinstance(v, int): return v

    a,o,b = v
    return OPS[o](solve2(a), solve2(b))

a,_,b = monkeys['root']


av = solve2(a)
bv = solve2(b)

print(av)
print(bv)

# solve expression on paper :D

# a = 242030880169441.0 - 703*humn/15
# b = 82091308111060.0

# 15 * (b-242030880169441) / 703
