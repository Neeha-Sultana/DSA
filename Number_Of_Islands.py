from collections import deque
def dfs(i,j,grid,n,m):
	# Check if its out of bound
	if i<0 or i>=n or j<0 or j>=m or grid[i][j] == 0:
		return
	# Mark as visited
	grid[i][j] = 0

	# Iterate for all possible directions
	for x in range(-1, 2):  
		for y in range(-1, 2):  
			nRow, nCol = i + x, j + y
			dfs(nRow,nCol,grid,n,m)
def bfs(i, j, grid, n, m):
    grid[i][j] = 0
    queue = deque([(i, j)])
    while queue:
        row, col = queue.popleft()
        for x in range(-1, 2):  
            for y in range(-1, 2):  
                nRow, nCol = row + x, col + y
		# Check if coordinates is out of bound
                if nRow < 0 or nRow >= n or nCol < 0 or nCol >= m or grid[nRow][nCol] == 0:
                    continue		
		# Mark as visited and append to queue
                grid[nRow][nCol] = 0
                queue.append((nRow, nCol))

def findIslands(mat, n, m):
	cnt = 0
	for i in range(n):
		for j in range(m):
			if mat[i][j]==1:
				dfs(i,j,mat,n,m)
				#bfs(i,j,mat,n,m)
				cnt+=1
	return cnt

mat = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1]
]
n = len(mat)
m = len(mat[0])

# Call the function to find islands
island_count = findIslands(mat, n, m)
print("Number of islands:", island_count)
