cmds = [ l.strip().split() for l in open('day10.txt') ]

cycle = 0
x = 1
res = 0

screen = []
line = ""

def tick():
    global res, line
    if cycle == 20 or ((cycle-20) % 40) == 0:
        res += cycle*x

    if abs(len(line)-x)<2:
        line += '#'
    else:
        line += '.'

    if not (cycle % 40):
        screen.append(line)
        line = ''


for c in cmds:
    if len(c) == 1:
        cycle += 1
        tick()
    else:
        cycle += 1
        tick()
        cycle += 1
        tick()
        x += int(c[1])

print(res)

print('\n'.join(screen))
