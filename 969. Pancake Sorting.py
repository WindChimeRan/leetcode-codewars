# 1
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        
        def flip(A: List[int], k: int) -> None:
            A[:k] = list(reversed(A[:k]))
            return 
        
        result = []
        def psort(A: List[int]):
            if A == sorted(A):
                return
            else:
                idx = A.index(max(A)) + 1
                flip(A, idx)
                flip(A, len(A))
                result.append(idx)
                result.append(len(A))
                psort(A[:-1])
        psort(A)
        return result
            
                
