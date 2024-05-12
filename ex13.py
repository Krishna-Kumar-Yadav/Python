class Solution(object):
  def leaderNumber(self,n):
    result = []
    for i in range(len(n)):
      flag = False
      for j in range(i+1,len(n)):
        if n[i] < n[j]:
          flag = True

      if flag == False:  
        result.append(n[i])

    return result   




A = [16,17,4,3,5,2,1]

req = Solution()
print(req.leaderNumber(A))
