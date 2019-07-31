class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        def check_fst(tok):
            if tok == first:
                return None, check_snd
            else:
                return None, check_fst
            
        def check_snd(tok):

            if tok == second:
                return None, check_thd
            elif tok == first:
                return None, check_snd
            else:
                return None, check_fst
            
        def check_thd(tok):

            if tok == first:
                return tok, check_snd
            else:
                return tok, check_fst
        
        result = []
        call_back = check_fst
        for tok in text.split():
            r, call_back = call_back(tok)
            if r:
                result.append(r)
        return result
    
    
# ------------------------------------------------------------------------------ #
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        result = []
        toks = text.split()
        for i, tok in enumerate(toks):
            if i<2:
                continue
            else:
                if toks[i-2] == first and toks[i-1] == second:
                    result.append(tok)
        return result
            
            
