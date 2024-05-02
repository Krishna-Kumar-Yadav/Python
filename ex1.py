# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        firstNumber = ''
        secondNumber = ''
        resultList = []

        for i in range(-1,-len(l1)-1,-1):
            firstNumber += str(l1[i])

        for j in range(-1,-len(l2)-1,-1):
            secondNumber += str(l1[j])

        print(firstNumber)
        print(secondNumber)
        sum = int(firstNumber) + int(secondNumber)   
  
        for i in reversed(str(sum)):
            resultList.append(int(i))    

        return resultList     

def main():
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    req = Solution()
    result = req.addTwoNumbers(l1,l2)
    print(result)

main()