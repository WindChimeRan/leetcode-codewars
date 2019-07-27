class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        saved = set() 
        substr = []
        begin = 0
        for i, c in enumerate(s):
            substr.append(c)
            if c not in saved:
                saved.add(c)
            else:
                while True:
                    head = substr.pop(0) 
                    if head == c: 
                        break
                    else:
                        saved.remove(head)
                        
            result = max(result, len(substr))
                
        return result
