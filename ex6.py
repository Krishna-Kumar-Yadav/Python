class Solution(object):
  def maxArea(self, height):
    volume = 0
    a = 0
    b = 0
    c = 0
    for i in range(len(height)):
      for j in range(i+1,len(height)):
        if height[i] <= height[j]:
          a = height[i]
        else:
          a = height[j]
        b = (j-i) * a

        if c <= b:
          c = b
      if volume <= c:
        volume = c    
    return volume


height = [1,8,6,2,5,4,8,3,7]

req = Solution()
result = req.maxArea(height)
print(result)
