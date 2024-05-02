class Solution(object):
  def isValid(self,s):
    l = []
    p = -1
    for i in range(len(s)):
         if s[i] == '(' or s[i] == '[' or s[i] == '{':
           l.append(s[i])
           p = p + 1
         elif s[i] == ')' or s[i] == ']' or s[i] == '}':
           if (l[p] == '(' and s[i] == ')') or (l[p] == '[' and s[i] == ']') or (l[p] == '{' and s[i] == '}'):
             l.remove(l[p])
             p = p - 1
           else:
             print("test")
             l.append(s[i])
             p = p + 1  

          

         print(l,p)    

    if len(l) == 0:
      return True
    else:
      return False  


req = Solution()
x = '([]))'
if req.isValid(x):
  print("valid")
else:
  print("Invalid")            