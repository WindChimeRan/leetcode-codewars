# 1 very bad

from itertools import takewhile, dropwhile

class Solution:
    def maxDistToClosest(self, seats: 'List[int]') -> 'int':
        is0 = lambda x: x == 0
        
        dis = []
        
        while len(seats) > 1:
            from0 = (seats[0] == 0)
            if from0:
                sub = list(takewhile(is0, seats))
                dis.append(len(sub))
                seats = list(dropwhile(is0, seats))
            else:
                sub = list(takewhile(is0, seats[1:]))
                seats = list(dropwhile(is0, seats[1:]))
                if len(seats) == 0:
                    dis.append(len(sub))
                else:
                    dis.append((len(sub)+1)//2)

        return max(dis)

# 2 still very bad

class Solution:
    def maxDistToClosest(self, seats: 'List[int]') -> 'int':
        is0 = lambda x: x == 0
        
        dis = 0
        
        while len(seats) > 1:
            from0 = (seats[0] == 0)
            if from0:
                for i, num in enumerate(seats):
                    if not is0(num):
                        break
                seats = seats[i:]
                dis = max(dis, i)
            else:
                for i, num in enumerate(seats[1:]):
                    if not is0(num):
                        dis = max(dis, (i+1)//2)
                        seats = seats[i+1:]
                        break
                else:
                    dis = max(dis, i+1)
                    seats = seats[i+2:]
        return dis

# 3 just so so, but so so
class Solution:
    def maxDistToClosest(self, seats: 'List[int]') -> 'int':
        s = ''.join(map(str, seats))
        s = s.split('1')
        lens = list(map(len, s))
        result = []
        if lens[0] != 0:
            result.append(lens[0])
        if lens[-1] != 0:
            result.append(lens[-1])
        lens = lens[1:-1]
        if len(lens) != 0:
            result.append((max(lens)+1)//2)
        return max(result)
            

            
        
