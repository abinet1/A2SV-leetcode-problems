class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        count = list(Counter(tasks).values())
        
        max_v = max(count)
        max_dub = count.count(max_v)

        return max((max_v-1)*(n+1)+max_dub,len(tasks))