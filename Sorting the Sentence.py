class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """

        sentence = s.split(' ')

        a = ["" for i in range(0,len(sentence))]

        for i in sentence:
            a[int(i[-1])-1]=i[0:len(i)-1]

        res = ""
        for i in range(0,len(a)):
            res += a[i]
            if(i!=len(a)-1):
                res += " "

        return res
