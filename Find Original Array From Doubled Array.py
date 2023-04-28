import heapq


class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """

        heapq.heapify(changed)
        result = []
        response = []



        if len(changed)%2==0:
            while len(changed)>0:
                num = heapq.heappop(changed)
                if len(result)==0:
                    result.append(num)
                elif result[0]*2==num:
                    response.append(result[0])
                    result.pop(0)
                else:
                    result.append(num)

                    
            if (len(result)==0):
                return response
            else:
                return []
        else:
            return []