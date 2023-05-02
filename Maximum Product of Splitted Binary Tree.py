import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_list=[]
        count =0
        priv = arr[0]
        heapq.heapify(arr)
        leng = len(arr)
        while(len(arr)):
            i = heapq.heappop(arr)
            if i==priv:
                count=count+1
            else:
                count_list.append(count)
                priv = i
                count = 1
        print(count_list)
        
        if count!=0:
            count_list.append(count)
            count = 0

        count_list.sort()
        sum_=0

        index = len(count_list)-1
        
        while(sum_<leng//2):
            res = count_list[index]
            sum_=sum_ + res
        
            if(sum_>=int(leng/2)):
                return len(count_list)-(index)
            index=index-1

        return sum_