class Solution(object):
    
    def prep(self, nums, bounder):
        result = []
        for i in range(0,bounder):
            result.append(nums[i])
            if nums[len(nums)-(i+1)] and i!=len(nums)-(i+1):
                result.append(nums[len(nums)-(i+1)])  
            # print(result)
        return result
        
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()

        result = []
        
        # print(nums)
        if len(nums)%2==0:
            result = self.prep(nums, len(nums)/2)
        else: 
            result = self.prep(nums, len(nums)/2+1)
            
            
        return result