sensors = [ line.strip().split(' ') for line in open('day15.txt') ]
sensors = [ (int(l[2][2:-1]), int(l[3][2:-1]), int(l[8][2:-1]), int(l[9][2:])) for l in sensors ]

beacons = set((s[2], s[3]) for s in sensors)
sensors = [ (s[0], s[1], abs(s[0]-s[2])+abs(s[1]-s[3])) for s in sensors ]

minx = min( x-d for x,y,d in sensors )
maxx = max( x+d for x,y,d in sensors )


n = 0
ty = 2000000 # 10
for tx in range(minx, maxx+1):
    if (tx,ty) in beacons: continue
    for x,y,d in sensors:
        if abs(tx-x)+abs(ty-y) <= d:
            #print(tx, ty, abs(tx-x)+abs(ty-y), d)
            n += 1
            break

print(n)
