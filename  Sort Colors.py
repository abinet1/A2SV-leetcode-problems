class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        return self.sort(nums)


    def sort(self, arr):
        for i in range(0,len(arr)):
            for j in range(0, i):
                if arr[j]>arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]
        return arr