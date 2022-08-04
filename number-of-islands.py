class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if you find a land, stack 1 and make it 0
        number_of_lands = 0
        r = len(grid)
        c = len(grid[0])

        for m, row in enumerate(grid):
            for n, node in enumerate(row):
                if grid[m][n] == "1":
                    number_of_lands = number_of_lands + 1
                    # self.search_lands(m, n, grid)
                    stacked_lands = []

                    grid[m][n] = "0"
                    stacked_lands.append((m, n))

                    while stacked_lands:
                        i, j = stacked_lands.pop()
                        if j-1 >= 0 and grid[i][j-1] == "1":
                            stacked_lands.append((i, j-1))
                            grid[i][j-1] = "0"
                        if j+1 <=c-1 and grid[i][j+1] == "1":
                            stacked_lands.append((i, j+1))
                            grid[i][j+1] = "0"
                        if i-1 >= 0 and grid[i-1][j] == "1":
                            stacked_lands.append((i-1, j))
                            grid[i-1][j] = "0"
                        if i+1 <= r-1 and grid[i+1][j] == "1":
                            stacked_lands.append((i+1, j))
                            grid[i+1][j] = "0"

        return number_of_lands