class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A[A.index(min(A))] *= -1
        if K == 1:
            return sum(A)
        else:
            return self.largestSumAfterKNegations(A, K-1)
