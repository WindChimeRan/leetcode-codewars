class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        matrix = [[10086000 if nn != n else 0 for nn in range(N+1)] for n in range(N+1)]
        for t in times:
            i, o, w = t
            matrix[i][o] = w
        for k in range(N + 1):
            for i in range(N + 1):
                for j in range(N + 1):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        result = max(matrix[K][i] for i in range(1, N+1))
        result = result if result != 10086000 else -1
        return result
