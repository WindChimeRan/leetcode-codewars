class Solution:
    def isAlienSorted(self, words: 'List[str]', order: 'str') -> 'bool':
        tab = {k: v for v, k in enumerate(order)}
        def trans(word):
            return tuple(map(lambda x: tab[x], word))
        init = trans(words[0])
        for w in words:
            cur = trans(w)
            if cur < init:
                return False
            else:
                init = cur
        return True
        
