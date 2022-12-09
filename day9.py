moves = [ l.split() for l in open('day9.txt') ]
moves = [ (d, int(c)) for d,c in moves ]

visited = {}

head = 0j
tail = 0j

DIR = dict(
    U=1j,
    D=-1j,
    L=-1+0j,
    R=1+0j,
)

def sign(s):
    if s<0: return -1
    if s>0: return 1
    return 0

for d, c in moves:
    for i in range(c):
        # print(d, head, tail, head-tail)
        head += DIR[d]

        diff = (head-tail)
        if abs(diff)>1.5:
            tail += sign(diff.real) + sign(diff.imag)*1j
        visited[tail] = True

print(len(visited))

n = 10
snake = [0j]*n
visited = {}

for d, c in moves:
    for i in range(c):
        # print(d, head, tail, head-tail)
        snake[0] += DIR[d]

        for i in range(1,n):

            diff = (snake[i-1]-snake[i])
            if abs(diff)>1.5:
                snake[i] += sign(diff.real) + sign(diff.imag)*1j
        visited[snake[-1]] = True

print(len(visited))
