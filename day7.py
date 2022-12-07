
fs = {}
cwd = [fs]
mode = 'cmd'
for l in open('day7.txt'):
    l = l.strip().split()
    if l[0] == '$':
        mode = 'cmd'
        if l[1] == 'cd':
            if l[2] == '/':
                cwd = [fs]
            elif l[2] == '..':
                cwd.pop()
            else:
                cwd.append(cwd[-1][l[2]])
        elif l[1] == 'ls':
            mode = 'ls'
        else:
            raise Exception('unknown cmd %s'%l[1])
    else:
        if mode != 'ls': raise Exception('huh')
        if l[0] == 'dir':
            cwd[-1][l[1]] = {}
        else:
            cwd[-1][l[1]] = int(l[0])

def du(folder, cb, path=()):
    res = 0
    for k,v in folder.items():
        if isinstance(v, int):
            #print(k,v)
            res += v
        else:
            sd = du(v, cb, path+(k,))
            cb(path+(k,), sd)
            res += sd

    return res

def tree(folder, depth=0):
    if depth==0: print('/')
    for k,v in folder.items():
        if not isinstance(v, int):
            print('  '*depth, k)
            tree(v, depth+1)
        else:
            print('  '*depth, v, k)

tree(fs)

dirs = {}
dirs['/'] = du(fs, dirs.__setitem__ )


print(dirs)
print(sum(s for d,s in dirs.items() if s<=100000))

capacity = 70000000
free = capacity - dirs['/']
needed = 30000000 - free

print(min((v,k) for k,v in dirs.items() if v>=needed))
