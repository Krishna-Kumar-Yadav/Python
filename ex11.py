class Solution(object):
  
  def sumOfSquareOfDigits(self,n):
    sum = 0
    for i in str(n):
      sum = sum + int(i)**2

    return sum  
  
  def isHappy(self,n):
    import time
    result = n
    startTime = time.time()

    while time.time() - startTime < 0.0001:
      result = self.sumOfSquareOfDigits(result)
      if result == 1:
        return True
    return False
    


req = Solution()
print(req.isHappy(389997)   ) 