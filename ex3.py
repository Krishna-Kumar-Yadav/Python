class Solution(object):
  def romanToInt(self,s):
    romanIntValue = {
      "I" : 1,
      "V" : 5,
      "X" : 10,
      "L" : 50,
      "C" : 100,
      "D" : 500,
      "M" : 1000
    }
    rInt = romanIntValue[s[-1]]
    for i in range(-2,-len(s)-1,-1):
      if romanIntValue[s[i+1]] <= romanIntValue[s[i]]:
        rInt += romanIntValue[s[i]]
      else:
        rInt -= romanIntValue[s[i]]

    print(rInt)    



req = Solution()
req.romanToInt("MCMXCIV")
