class Solution(object):
  def check(self,a,b):
      k = a
      count = 0
      for i in range(len(a)-1):
         if a[i] != "*" and a[i+1] == "*":
            k = k.replace(a[i],'')
            k = k.replace(a[i+1],'')
 

      for i in k:
         for j in b:
            if i == j:
              count += 1
  
         if count > 1:
            return False
         else:
            count = 0

      return True             

      



A = "a*b*cd"
B = "aabcdbb"

req = Solution()
print(req.check(A,B))
