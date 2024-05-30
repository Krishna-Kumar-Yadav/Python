class Solution(object):
  def dic(self):
    d = {
      '2' : 'a',
      '22' : 'b',
      '222' : 'c',
      '3' : 'd',
      '33' : 'e',
      '333' : 'f',
      '4' : 'g',
      '44' : 'h',
      '444' : 'i',
      '5' : 'j',
      '55' : 'k',
      '555' : 'l',
      '6' : 'm',
      '66' : 'n',
      '666' : 'o',
      '7' : 'p',
      '77' : 'q',
      '777' : 'r',
      '7777' : 's',
      '8' : 't',
      '88' : 'u',
      '888' : 'v',
      '9' : 'w',
      '99' : 'x',
      '999' : 'y',
      '9999' : 'z'

    }

    return d   

  def phone(self,n):
    d = self.dic()
    j = 0
    i = 0
    try:
      A = [n[0]]
      while i != len(n)-1:
        if len(A[j]) < 3 and n[i] == n[i+1]:
          A[j] += n[i+1]
        else:
          A.append(n[i+1])
          j += 1 
        i += 1 
        
      result = ""
      for i in A:
        result += d[i]

      print(result) 
    except:
      print("Only key between 2-9")

"""def phone(self,n):
    d = self.dic()
    flag = True
    i = 0
    a = ""
    result = ""
    while flag:
      try:
        if n[i] != n[i+1]:
          a = n[0:i+1:1]
          result += d[a]
          n = n.replace(n[0:i+1:1],"")
          i = -1  
        i += 1 
      except :
        flag = False  
    result += d[n[0]]    
    print(result) """     




         
        



req = Solution()
x = input("Enter the number : ")
req.phone(x)    