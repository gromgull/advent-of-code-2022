inp = open('day6.txt').read()

n = 14
lastn = []

for i in range(len(inp)):
    lastn.append(inp[i])
    if len(lastn)>n: lastn.pop(0)
    print(i, lastn)
    if len(set(lastn))==n: break

print(i+1)
