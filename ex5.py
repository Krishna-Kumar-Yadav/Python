class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

#class Solution(object):
#    def mergeKLists(self, lists):
        

def display_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def main():
    l1node1 = ListNode(1)
    l1node2 = ListNode(4)
    l1node3 = ListNode(5)  

    l1node1.next = l1node2
    l1node2.next = l1node3   

    l2node1 = ListNode(1)
    l2node2 = ListNode(3)
    l2node3 = ListNode(4)  

    l2node1.next = l2node2
    l2node2.next = l2node3   

    l3node1 = ListNode(2)
    l3node2 = ListNode(6) 

    l3node1.next = l1node2     

    display_linked_list(l1node1)
    display_linked_list(l2node1)
    display_linked_list(l3node1)

main()    