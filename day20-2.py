from __future__ import annotations
from dataclasses import dataclass


lst = [int(l.strip()) for l in open('day20.txt')]
lst = [ 811589153*i for i in lst ]

@dataclass
class Item:
    val : int
    prev : Item = None
    next : Item = None

lst = [ Item(v) for v in lst ]

for i in range(1, len(lst)-1):
    lst[i].prev = lst[i-1]
    lst[i].next = lst[i+1]

lst[0].prev = lst[-1]
lst[0].next = lst[1]
lst[-1].prev = lst[-2]
lst[-1].next = lst[0]

for i in lst:
    if i.val == 0: zero = i

def show(s):
    n = s
    while True:
        yield n.val
        n = n.next
        if n == s: break

for i in range(10):

    for n in lst:

        for j in range(abs(n.val)%(len(lst)-1)):

            pre = n.prev
            nxt = n.next

            if n.val>0:

                nxtnxt = n.next.next

                pre.next = nxt
                nxt.prev = pre

                n.prev = nxt
                nxt.next = n

                n.next = nxtnxt
                nxtnxt.prev = n

            else:

                prepre = n.prev.prev

                nxt.prev = pre
                pre.next = nxt

                n.prev = prepre
                prepre.next = n

                n.next = pre
                pre.prev = n



print(list(show(zero)))


vals = []
for i in [1000,2000,3000]:
    n = zero
    for j in range(i):
        n = n.next
    print(n.val)
    vals.append(n.val)

print(sum(vals))
