class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        def is_even(x):
            return x%2 == 0
        def sum_even(xs: List[int]):
            return sum(filter(is_even, xs))
        
        result = []
        init_sum = sum_even(A)
        for val, index in queries:
            pre = A[index]
            cur = pre + val
            A[index] = cur
            
            if is_even(pre) and is_even(cur):
                init_sum += cur - pre
            elif is_even(pre) and (not is_even(cur)):
                init_sum -= pre
            elif (not is_even(pre)) and is_even(cur):
                init_sum += cur
            
            result.append(init_sum)
            
        return result
            
