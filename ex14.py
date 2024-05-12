class Solution(object):
    def removeDuplicates(self, nums):
      result = []
      compare = nums[0]
      result.append(compare)
      for i in range(len(nums)):
         if compare != nums[i]:
            compare = nums[i]
            result.append(compare)


      return len(result) 
      print(result)     
         




A = [0,0,1,1,1,2,2,3,3,4]

req = Solution()
req.removeDuplicates(A)
        

