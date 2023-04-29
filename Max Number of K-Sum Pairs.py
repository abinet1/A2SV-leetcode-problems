class Solution(object):
    def check(self, num_one, num_two, k):
        return num_one + num_two == k

    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        need = {}
        count = 0
        for i in nums:
            if i<=k:
                if (i in need)and(need[i]>0):
                    # print("if :",need, i, need[i], count)
                    count = count + 1
                    need[i] = need[i] - 1
                elif ((k-i) in need):
                    # print("elif :",need, i, count)
                    need[k-i] = need[k-i]+1
                else:
                    # print("else :",need, i, count)
                    need[k-i] = 1
            
        # print(count)
        return count

