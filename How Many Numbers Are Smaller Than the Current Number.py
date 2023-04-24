class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0 for i in range(0, len(nums))]
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    result[i] += 1
                elif nums[j]>nums[i]:
                    result[j] += 1
        return result