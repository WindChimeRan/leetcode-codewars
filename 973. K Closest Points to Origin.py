class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def euclidean(point: List[int]) -> int:
            return sum(map(lambda x: x**2, point))
        
        dis = sorted(points, key=euclidean)
        return dis[:K]
        
