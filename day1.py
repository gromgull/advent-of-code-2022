lines = [ x.strip() for x in open('day1.txt') ]
lines = [ int(x) if x else None for x in lines ]
elves = []
elf = []
while lines:
    if x := lines.pop():
        elf.append(x)
    else:
        elves.append(elf)
        elf = []

sums = [sum(e) for e in elves]
print(max(sums))

print(sum(sorted(sums)[-3:]))
