import itertools
import operator as op
from tqdm import tqdm

def chunk(l, n):

    return itertools.groupby(zip(itertools.count(), l), lambda x: x[0]//n)

OPS = {
    '+': op.add,
    '*': op.mul,
}

class Monkey:

    def __init__(self, s):
        self.id = int(s[0].split()[1][:-1])
        self.items = [int(i) for i in s[1].split(':')[1].split(',')]
        ops = s[2].split()[-2:]
        self.op = OPS[ops[0]]
        self.op_arg = int(ops[1]) if ops[1]!='old' else None
        self.test = int(s[3].split()[-1])
        self.if_true = int(s[4].split()[-1])
        self.if_false = int(s[5].split()[-1])
        self.inspects = 0

    def turn(self):
        for i in self.items:
            self.inspects += 1
            i = self.op(i, i if self.op_arg is None else self.op_arg)
            # i //= 3

            if (i % self.test) == 0:
                i //= self.test
                monkeys[self.if_true].items.append(i)
            else:
                monkeys[self.if_false].items.append(i)

        self.items = []

    def __repr__(self):
        return f'Monkey({self.id}, {self.inspects}, {self.items})'


monkeys = [ Monkey([s[1] for s in c]) for _,c in chunk([ l.strip() for l in open('test11.txt') ], 7) ]
monkeys = { m.id: m for m in monkeys }

for r in tqdm(range(1000)):
    for m in monkeys.values():
        #import ipdb; ipdb.set_trace()
        m.turn()
        if not r % 100:
            print(monkeys)

best = sorted([(m.inspects, m) for m in monkeys.values()])[-2:]
print(best[0][0]*best[1][0])

print(monkeys)
