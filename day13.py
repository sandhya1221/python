'''class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


def createLinkedList(arr):
    head = None
    for data in arr:
        if head is None:
            head = Node(data)
            temp = head
        else:
            temp.next = Node(data)
            temp = temp.next
    printLL(head)
def printLL(head):
    temp=head
    while temp:
        print(str(temp.data)+"-->",end="")
        temp=temp.next
    print("None")
arr=list(map(int,input().split()))
createLinkedList(arr)'''



#middle of the linked list or slow and fast pointer
# Time com:O(N)
  
#delete the middle element done in leetcode(2095)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def deleteMiddle(head):
        if(head==None or head.next==None):
            return None
        slow=head
        fast=head
        prev=None
        while(fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next=slow.next
        slow.next=None
    # Delete middle node
         
        return head
head = [1,3,4,7,1,2,6]
