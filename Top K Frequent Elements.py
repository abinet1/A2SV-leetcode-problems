class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = 1+count.get(i,0)

        for key, value in count.items():
            result[value].append(key)

        res = []
        for i in range(len(result)-1,0,-1):
            for j in result[i]:
                res.append(j)
                if len(res)==k:
                    return res