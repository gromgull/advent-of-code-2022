moves = [ x.strip().split(' ') for x in open('day2.txt') ]

plays = dict(X=1, Y=2, Z=3)
scores = dict(A=dict(X=3, Y=6, Z=0),
              B=dict(X=0, Y=3, Z=6),
              C=dict(X=6, Y=0, Z=3))

def score(x,y):

    return plays[y] + scores[x][y]


print(sum(score(x,y) for x,y in moves))

# X lose, Y draw, Z win
wins = dict(A=dict(X='Z', Y='X', Z='Y'),
            B=dict(X='X', Y='Y', Z='Z'),
            C=dict(X='Y', Y='Z', Z='X'))

print(sum(score(x, wins[x][y]) for x,y in moves))
