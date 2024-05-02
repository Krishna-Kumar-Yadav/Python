class Solution:
    def longestValidParentheses(self, s: str) -> int:
        a = []
        p = -1
        for i in range(len(s)):
            print(a)
            if s[i] == ')' and  s[i-1] == '(':
                a.remove(s[p])
                p = p - 1
            else:
                a.append(s[i])
                p = p + 1    


        return a       


    
            

req = Solution()
x = "()(())"
print(req.longestValidParentheses(x) )           