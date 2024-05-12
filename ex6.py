class Solution(object):
  def maxArea(self, height):
    i = 0
    j = len(height)-1
    volume = 0
    a = 0
    while i < j:
      if height[i] <= height[j]:
        a = height[i] * (j-i)
        i = i + 1
      else:
        a = height[j] * (j-i)
        j = j - 1

      if a > volume:
        volume = a  

    return volume      



height = [1,8,6,2,5,4,8,3,7]

req = Solution()
result = req.maxArea(height)
print(result)
