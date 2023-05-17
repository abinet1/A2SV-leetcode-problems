class Solution:

    def carFleet(self, target, position, speed) -> int:
        arr=[]
        for i in range(0,len(position)):
            arr.append([position[i],speed[i]])

        arr.sort()

        stack = []

        for i in range(len(arr)-1,-1,-1):
            if len(stack) == 0:
                stack.append(arr[i])
            elif arr[i][1]<=stack[len(stack)-1][1]:
                stack.append(arr[i])
            elif arr[i][1]>stack[len(stack)-1][1]:
                t = (target-arr[i][0])/arr[i][1]
                tt = (target-stack[len(stack)-1][0])/stack[len(stack)-1][1]
                if t>tt:
                    stack.append(arr[i])
                
        return len(stack)