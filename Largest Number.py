class Solution(object):
    def sort(self, nums):
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if int(str(nums[j])+str(nums[j-1]))> int(str(nums[j-1])+str(nums[j])):
                    nums[j], nums[j-1] = nums[j-1], nums[j] 
        return nums
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        result = self.sort(nums)
        res=""
        only_zero = True if result[0] == 0 else False
        for i in result:
            res=res+str(i)
        if only_zero:
            return "0"
        return res