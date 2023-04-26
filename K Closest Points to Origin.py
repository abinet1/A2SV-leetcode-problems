import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points_heap = []
        for i in (points):
            points_heap.append([i[0]**2+i[1]**2, i[0],i[1]])
        
        heapq.heapify(points_heap)

        res = []
        while k>0:
            dis, x, y = heapq.heappop(points_heap)
            res.append([x,y])
            k-=1
        return res