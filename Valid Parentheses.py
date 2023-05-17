class Solution:

    def oposite(self, t1, t2):
        if(t2=="(" and t1==')'):
            return True
        if(t2=="{" and t1=='}'):
            return True
        if(t2=="[" and t1==']'):
            return True
        return False

    def isValid(self, s: str) -> bool:
        a=[]
        if len(s)%2!=0:
            return False

        else:

            for i in s:
                if i in "({[":
                    a.append(i)
                elif len(a)>0 and self.oposite(i,a[len(a)-1]):
                    a.pop()
                else:
                    return False
                    
        if len(a)==0:
            return True
        else:
            return False