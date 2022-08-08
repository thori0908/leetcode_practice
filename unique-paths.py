class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths_map = [[None]*n for _ in range(m)]

        for i in range(0, m):
            row = [1]
            for j in range(0, n):
                if i == 0 or j == 0:
                    paths_map[i][j] = 1
                else:
                    paths_map[i][j] = paths_map[i-1][j] + paths_map[i][j-1]
        return paths_map[m-1][n-1]


        # m+nCm or m+nCn
        # 21C10 or 21C11
        # 21C10 = 20C10 + 20C9
        # (3,2) = (2,2) + (3,1)

        # move down m-1 times
        # move right n-1 times
        # move down or right m+n times
        # ith(0~m+n-2) paths 
        # paths_i = paths_i-1 down + paths_i-1 right
        # [r, r, d]
        # [r, d, r]
        # [d, r, r]

        # 5C1 = 5
        # 5C1 = 5
        # 2C1 = 2
        # 5C2 = 4C2 + 4C1
        # 6C2 = 5C2 + 5C1


