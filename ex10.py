class Solution(object):
  def binaryToInteger(self,a):
    result = 0
    i = 1
    j = -1
    while j != -len(a)-1:
      result = result + int(a[j]) *i
      i = 2**-j
      j = j-1

    return result
  
  def integerToBinary(self,a):
    result = ''
    while a > 0:
      result = str(a%2) +result
      a = a//2

    return result  

  def binaryAddition(self,a,b):
    resultInt = int(self.binaryToInteger(a)) + int(self.binaryToInteger(b))
    print(resultInt)
    return self.integerToBinary(resultInt)



    

req = Solution()
result = req.binaryAddition('1000011', '11101')  
print(result)   

#'1011100'