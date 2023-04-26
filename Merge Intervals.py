class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            # print((result[len(result)-1][1]>=intervals[i][0]) and (result[len(result)-1][1]<intervals[i][1]))
            if (result[len(result)-1][1]>=intervals[i][0]) and (result[len(result)-1][1]<intervals[i][1]):
                result[len(result)-1][1]=intervals[i][1]
            elif (result[len(result)-1][1]<intervals[i][0]):
                result.append(intervals[i])
        
        return result