class Solution:
    def convert(self, s: str):
        return s[::-1]
    
    def check(self, s: str):
        # print("the start of def: ",s)
        index=0
        # print(s)
        while(index<len(s)):
            # print(s)
            # print(index)
            if(s[index]=='('):    
                s=s[:index]+'*'+s[index+1:]
                temp = self.check(s[index:])
                s = s[0:index] + temp + s[index+len(temp):]
                # ct = temp[1]
            elif (s[index]==')'):
                temp = s[0:index+1]
                temp=temp.replace('(','*')
                temp=temp.replace(')','*')
                # print(temp)
                return self.convert(temp)
            index+=1
        return s
            
    def reverseParentheses(self, s: str) -> str:
        # ct = s.count('(')
        result = self.check(s)
        result=result.replace('*','')
        # print(result)
        return result