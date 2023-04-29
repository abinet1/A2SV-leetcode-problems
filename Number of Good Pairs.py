import heapq

class Solution(object):

    def permut(self, n):
        return (n*(n+1))/2

    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        heapq.heapify(nums)
        prive = heapq.heappop(nums)
        count = 0 
        count_sum = 0
        while(len(nums)>0):
            num = heapq.heappop(nums)
            if prive == num:
                count = count + 1
            elif prive != num:
                prive = num
                count_sum = count_sum + self.permut(count)
                count = 0

        if(count>0):
            count_sum = count_sum + self.permut(count)
        
        return count_sum

