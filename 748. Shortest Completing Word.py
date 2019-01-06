# 1
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        plate = sorted(map(str.lower, filter(lambda x: str.isalpha(x), licensePlate)))
        
        result = None
        length = 1001
        
        for w in words:
            inword = sorted(filter(lambda x: x in plate, w))
            state = []
            for p in plate:
                if p in inword:
                    state.append(True)
                    inword.remove(p)
                else:
                    state.append(False)
            if all(state):
                if len(w) < length:
                    result = w
                    length = len(w)
        return result
