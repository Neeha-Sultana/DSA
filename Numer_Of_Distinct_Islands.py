from collections import deque
class Solution:
    def dfs(self, row, col, vis, grid, vec, row0, col0):
        # Mark the cell as visited
        vis[row][col] = 1
       
        # Coordinates - base coordinates
        vec.append((row - row0, col - col0))
        
        n = len(grid)
        m = len(grid[0])
        
        # Delta row and delta column
        delrow = [-1, 0, 1, 0]
        delcol = [0, -1, 0, 1]
        
        # Traverse all 4 neighbours
        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]
            
            # Check for valid unvisited land neighbour coordinates
            if (0 <= nrow < n and 0 <= ncol < m and
                not vis[nrow][ncol] and grid[nrow][ncol] == 1):
                self.dfs(nrow, ncol, vis, grid, vec, row0, col0)

    def countDistinctIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        vis = [[0] * m for _ in range(n)]
        st = set()
        
        # Traverse the grid
        for i in range(n):
            for j in range(m):
                # If not visited and is a land cell
                if not vis[i][j] and grid[i][j] == 1:
                    vec = []
                    self.dfs(i, j, vis, grid, vec, i, j)
                    # Store in set
                    st.add(tuple(vec))
        
        return len(st)

if __name__ == "__main__":
    grid = [
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]
    ]
            
    obj = Solution()
    print(obj.countDistinctIslands(grid))
