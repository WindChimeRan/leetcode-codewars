class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, key=lambda x: -x)
        for i in range(len(A)-2):
            a, b, c = A[i], A[i+1], A[i+2]
            if b + c > a:
                return a+b+c
        return 0
            
                
