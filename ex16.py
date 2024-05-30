class Solution(object):
  def validDic(self,dic):
    for i in dic.keys():
      try:
        if len(dic[i]) == 0:
          #dic.pop(i)
          print(i) 
        if dic[i] is None:
          print(i) 
      except:
        continue

    #print(dic["k"])   





A = {
  "a" : 2,
  "b" : "HGH",
  "c" : True,
  "d" : [],
  "e" : (),
  "f" : {},
  "g" : [1,2],
  "h" : {"ee":2},
  "i" : (4,5),
  "j" : "",
  "k" : None,

  
}

req = Solution()
req.validDic(A)