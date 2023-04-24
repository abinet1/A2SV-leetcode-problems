#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        index = i
        for j in range(i,len(arr)):
            if arr[index]>arr[j]:
                index = j
        return index
    
    def selectionSort(self, arr,n):
        #code here
        ar=arr
        for i in range(0,len(ar)):
            index = self.select(ar,i)
            ar[i],ar[index] = ar[index], ar[i]
        return ar

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends