class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        win_len = 1
        right_pointer = 0
        left_pointer = 0
        max_len = 1
        nums.sort()         
        total = nums[right_pointer]   

        while(right_pointer<len(nums) and len(nums)-left_pointer>max_len ):
            if(nums[right_pointer]*win_len <= k + total):
                
                right_pointer =right_pointer + 1
                max_len = max(win_len, max_len)
                win_len = win_len+1
                if right_pointer<len(nums):
                    total = total + nums[right_pointer] 
            
            elif(nums[right_pointer]*win_len > k + total):
                total = total - nums[left_pointer]
                win_len -= 1 
                left_pointer =left_pointer+ 1
        return max_len;

