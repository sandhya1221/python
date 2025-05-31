#linked list cycle(cycle is present or not) OUTPUT:True or False
def linkedlist(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
    if slow==fast:
        return True
    return False
head = [3,2,0,-4], pos = 1
print(linkedlist(head))

#linked list cycle2 in leetcode
''' class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                slow=head
                while(slow!=fast):
                    slow=slow.next
                    fast=fast.next
                return slow
        return None'''
        
'''============================================================================='''
        
#length in linked list cycle in gfg
'''class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                slow=head
                while(slow!=fast):
                    slow=slow.next
                    fast=fast.next.next
                count=1
                slow=slow.next
                while(slow!=fast):
                    slow=slow.next
                    count+=1
                return count
        return 0
        '''
        
        
'''========================================================================='''
        
#DFS:
#Inorder
'''def inorder(root):
    if (root==None):
        return
    inorder(root.val)
    print(root.left)
    inorder(root.right)
def preorder(root):
    if (root==None):
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if (root==None):
        return
    print(root.val)
    postorder(root.right)
    postorder(root.left)'''
    

#Binary tree level order traversal in leetcode (102)

#depth height of the binary tree

#sort list


'''==============================================================================='''

# palinddrome linked list
'''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome(head):
    arr=[]
    temp=head
    while(temp):
        arr.append(temp.val)
        temp=temp.next
    return arr==arr[::-1]
node1 = ListNode(4)
node2 = ListNode(4)
node3 = ListNode(1)
node4 = ListNode(9)
node5 = ListNode(8)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print(isPalindrome(node1))'''





#ARRAY TO BINARY TREE


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createBST(arr):
            root=None
            for data in arr:
                if(root==None):
                    root=Node(data)
                else:
                    temp=root
                    while(True):
                        if(data<temp.val):
                            if(temp.left==None):
                                temp.left=Node(data)
                                break
                            else:
                                temp=temp.left
                        if(data>temp.val):
                            if(temp.right==None):
                                temp.right=NOde(data)
                                break
                            else:
                                temp=temp.right
                            
                    return root.left.right.val
                arr=list(map(int,input().split()))
                createBST(arr)'''
                
                
#Doubly linked list 
'''class Node:
    def __init__(self,data):
        self.prev=None
        self.val=data
        self.next=None
    def createDoublyLinkedList(arr):
        head=None
        for data in arr:
            if(head==None):
                head=Node(data)
                temp=head
            else:
                newNode=Node(data)
                newNode.prev=temp
                temp.next=newNode
                temp=temp.next
                
arr=list(map(int,input().split()))
createDoublyLinkedList(arr)'''




#chatgpt doubly linked list
'''class Node:
    def __init__(self, data):
        self.prev = None
        self.val = data
        self.next = None

def createDoublyLinkedList(arr):
    head = None
    temp = None
    for data in arr:
        if head is None:
            head = Node(data)
            temp = head
        else:
            newNode = Node(data)
            newNode.prev = temp
            temp.next = newNode
            temp = temp.next
    return head

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next

# Input
arr = list(map(int, input("Enter elements: ").split()))
head = createDoublyLinkedList(arr)
print("Doubly Linked List:")
printList(head)'''



#binary and inorder
'''class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBST(arr):
    root = None
    for data in arr:
        if root is None:
            root = TreeNode(data)
        else:
            temp = root
            while True:
                if data < temp.val:
                    if temp.left is None:
                        temp.left = TreeNode(data)
                        break
                    else:
                        temp = temp.left
                elif data > temp.val:
                    if temp.right is None:
                        temp.right = TreeNode(data)
                        break
                    else:
                        temp = temp.right
    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

arr = list(map(int, input().split()))
root = createBST(arr)
inorder(root)'''
