class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        print(6/-132)
        result = []
        for i in range(0,len(tokens)):
            if tokens[i]=='+':
                print("+",result[len(result)-2],result[len(result)-1])
                res = result[len(result)-2]+result[len(result)-1]
                result.pop()
                result.pop()
                result.append(res)
            elif tokens[i]=='-':
                print("-",result[len(result)-2],result[len(result)-1])
                res = result[len(result)-2]-result[len(result)-1]
                result.pop()
                result.pop()
                result.append(res)
            elif tokens[i]=='*':
                print("*",result[len(result)-2],result[len(result)-1])
                res = result[len(result)-2]*result[len(result)-1]
                result.pop()
                result.pop()
                result.append(res)
            elif tokens[i]=='/':
                print("/",result[len(result)-2],result[len(result)-1])
                res = int(result[len(result)-2]/result[len(result)-1])
                result.pop()
                result.pop()
                result.append(res)
            else:
                result.append(int(tokens[i]))
        return result[0]