import numpy as np

trees = np.array([[int(c) for c in l.strip()] for l in open('day8.txt')])

visible = np.zeros(trees.shape, dtype=bool)

visible[0] = 1
visible[-1] = 1
visible[:, 0] = 1
visible[:, -1] = 1

mx = trees[0]
for i in range(1,trees.shape[0]):
    visible[i] |= trees[i]>mx
    mx = np.maximum(trees[i], mx)

mx = trees[:,0]
for i in range(1,trees.shape[1]):
    visible[:,i] |= trees[:,i]>mx
    mx = np.maximum(trees[:,i], mx)

mx = trees[-1]
for i in range(trees.shape[0]-2,0,-1):
    visible[i] |= trees[i]>mx
    mx = np.maximum(trees[i], mx)

mx = trees[:,-1]
for i in range(trees.shape[1]-2,0,-1):
    visible[:,i] |= trees[:,i]>mx
    mx = np.maximum(trees[:,i], mx)

print(trees)
print(visible.astype(int))

print(len(visible.nonzero()[0]))


counts = np.zeros(trees.shape, dtype=int)

for i in range(0,trees.shape[0]):
    for j in range(0, trees.shape[1]):

        c = 0
        for a in range(i+1, trees.shape[0]):
            c += 1
            if trees[a,j] >= trees[i,j]: break

        counts[i,j] = c

        c = 0
        for a in range(j+1, trees.shape[1]):
            c += 1
            if trees[i,a] >= trees[i,j]: break

        counts[i,j] *= c

        c = 0
        for a in range(i-1, -1, -1):
            c += 1
            if trees[a,j] >= trees[i,j]: break

        counts[i,j] *= c

        c = 0
        for a in range(j-1, -1, -1):
            c += 1
            if trees[i,a] >= trees[i,j]: break

        counts[i,j] *= c


print(counts)
print(counts.max())
