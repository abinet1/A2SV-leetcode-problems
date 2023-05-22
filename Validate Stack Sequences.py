class Solution(object):
    def validateStackSequences(self, pushed, popped):
        res = []

        while(len(pushed)>0):
            
            pushed_num = pushed.pop(0)

            res.append(pushed_num)
    
            while(len(res)>0 and len(popped)>0):
                if res[len(res)-1]==popped[0]:
                    res.pop()
                    popped.pop(0)
                else: 
                    break
            
        if len(pushed)==0 and len(popped)==0 and len(res)==0:
            return True
        else:
            return False