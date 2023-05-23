class Solution:
    def move_left(self, heght,left,right):
        result = min(heght[left],heght[right])*(right-left)
        return result, left
    def move_right(self, heght, left, right):
        result = min(heght[left],heght[right])*(right-left)
        return result, right
    def maxArea(self, height) -> int:
        leftindex=0
        rightindex=len(height)-1
        result = min(height[leftindex],height[rightindex])*(rightindex-leftindex)
        while leftindex < rightindex:
            if height[leftindex] <= height[rightindex]:
                new_result, leftindex = self.move_left(height,leftindex+1,rightindex)
                result = max(result, new_result)
            elif height[leftindex] >= height[rightindex]:
                new_result, rightindex = self.move_right(height,leftindex,rightindex-1)
                result = max(result, new_result)
        return result