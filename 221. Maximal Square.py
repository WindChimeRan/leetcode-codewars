import copy
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # check edge case
        
        if not matrix:
            return 0
        
        R = len(matrix)
        C = len(matrix[0])

        dp = [[int(c) for c in r] for r in matrix]
        for r in range(1, R):
            for c in range(1, C):
                if dp[r][c] == 1:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    print(dp[r][c])

        return max(map(max,dp)) ** 2
