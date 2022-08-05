from collections import deque

row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]

def isSafe(mat, x, y, processed):
    return (x >= 0 and x < len(processed)) and (y >= 0 and y < len(processed)) and mat[x][y] == 1 and not processed[x][y] 

def BFS(mat, processed, i, j):
    q = deque()
    q.append((i, j))

    processed[i][j] = True

    while q:
        x, y = q.popleft()

        for k in range(len(row)):
            if isSafe(mat, x + row[k], y + col[k], processed):
                processed[x + row[k]][y + col[k]] = True
                q.append((x + row[k], y + col[k]))



def countIslands(mat):
    if not mat or not len(mat):
        return 0
    
    M, N = (len(mat), len(mat[0]))
    processed = [[False for x in range(N)] for y in range(M)]

    islands = 0
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 1 and not processed[i][j]:
                BFS(mat, processed, i, j)
                islands += 1
    return islands

if __name__ == '__main__':
 
    mat = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    ]
 
    print('The total number of islands is', countIslands(mat))