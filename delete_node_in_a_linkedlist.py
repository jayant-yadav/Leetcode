# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    head = None # head is not a node initially.
    temp = ListNode(None)
    ls = [1,2,3,4,5,6]

    for i in ls:
        node = ListNode(None)
        node.val = i
        if head == None:
            head = node
            temp.next = head
        
        else:
            temp.next.next = node                                                                                                                 
        temp.next = node

    print(f'following is the full LL:')
    temp = head
    while temp != None:
        print(temp.val)
        temp = temp.next

    sol = Solution()

    delnode = head
    while delnode != None:
        if delnode.val == 4:
            break
        delnode = delnode.next


    sol.deleteNode(delnode)

    print(f'LL after deleting node: ')
    temp = head
    while temp != None:
        print(temp.val)
        temp = temp.next
    
    