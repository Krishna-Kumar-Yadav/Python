class Solution(object):
  def findMedianSortedArrays(self,num1,num2):
    sortedList = self.sort(num1,num2)
    length = len(sortedList)
    median = None
    if length % 2 == 0:  
      median = (sortedList[length // 2 - 1] + sortedList[length // 2]) / 2
    else:  
      median = sortedList[length // 2]
      
    return median


  def sort(self,num1,num2):
    num3 = []
    i = 0
    j = 0
    k = 0

    if len(num1) <= len(num2):
      while k != len(num1) + len(num2) and i != len(num1):
        if num1[i] <= num2[j]:
          num3.append(num1[i])
          i += 1
          k += 1
        else:
          num3.append(num2[j])
          j += 1
          k += 1  

      while j != len(num2):
          num3.append(num2[j])
          j += 1
          k += 1  
    else:
      while k != len(num1) + len(num2) and j != len(num2):
        if num1[i] <= num2[j]:
          num3.append(num1[i])
          i += 1
          k += 1
        else:
          num3.append(num2[j])
          j += 1
          k += 1  

      while i != len(num1):
          num3.append(num1[i])
          i += 1
          k += 1  


    return num3


  


nums1 = [1,2]
nums2 = [3,4]

req = Solution()
result = req.findMedianSortedArrays(nums1,nums2)
print(result)
