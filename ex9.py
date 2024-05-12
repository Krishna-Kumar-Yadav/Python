""" import csv

def calculate(filepath):
  column = 7
  total = 0
  i = 0
  with open(filepath,'r') as file:
    csvFile = csv.reader(file)
    for row in csvFile:
      if i > 0:
        total = total + int(row[column])
      else:
        i = i + 1

    print(total)      



calculate('StudentOutstandingReport.csv')

 """

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a = ''
        flag = False
        for i in range(len(word)):
            if word[i] == ch and flag == False:
                a = word[i::-1]
                flag = True
                
            elif flag == False:
                a = word  

            if flag:
                a = a + word[i+1::1]
                break              

        return a  

req = Solution()
req.reversePrefix("xxxxxxx","c")                