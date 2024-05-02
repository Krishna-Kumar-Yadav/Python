class Solution(object):
    def reverse(self, x):
          string = str(x)
          if string[0] == '-':
              result = string[-1:-len(string):-1]    
              finalResult = '-' + result
          else:
              finalResult = string[::-1]   

          if int(finalResult) < -2**31 or int(finalResult) > 2**31-1:
            return 0
          else:
            return int(finalResult)


def main():
    req = Solution()
    result = req.reverse(1534236469)  
    print(result)


main()                
        