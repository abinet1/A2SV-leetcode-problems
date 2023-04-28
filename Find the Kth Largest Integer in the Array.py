import heapq

class Solution(object):

    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        k = len(nums)-k
        # print("k: ",k," len of nums: ", len(nums))

        nums=[int(i) for i in nums]
        heapq.heapify(nums)
        
        while k>=0:
            res = heapq.heappop(nums)
            k-=1

            # print(res)
        return str(res)