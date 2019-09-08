class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
            def check(target, refer):
                # only check the target vector, according to refer
                assert len(target) == len(refer)
                # edge case: len <= 1
                eq_target0 = target[0]
                eq_refer0 = refer[0]
                cnt_target = 0 # fst token is the current one
                cnt_refer = 1 # fst token is to rotate
                for i in range(1, len(target)):
                    if target[i] == eq_target0:
                        cnt_target += 0
                    elif refer[i] == eq_target0:
                        cnt_target += 1

                    if target[i] == eq_refer0:
                        cnt_refer += 0
                    elif refer[i] == eq_refer0:
                        cnt_refer += 1
                    if eq_target0 not in (target[i], refer[i]):
                        cnt_target = float('inf')
                    if eq_refer0 not in (target[i], refer[i]):
                        cnt_refer = float('inf')

                return cnt_refer, cnt_target
            search_a = check(A, B)
            search_b = check(B, A)
            result = min(search_a + search_b)
            return result if result != float('inf') else -1
