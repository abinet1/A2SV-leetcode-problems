class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = [True for i in range(0,len(l))]
        for i in range(0, len(l)):
            initial_val, final_val = min(l[i],r[i]), max(l[i],r[i])
            num = nums[initial_val: final_val+1]
            num.sort()
            for j in range(0, len(num)-1):
                if(j==0):
                    diff = num[j+1]-num[j]
                elif (diff!=num[j+1]-num[j]):
                    result[i] = False
                    break
        return result