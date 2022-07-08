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
        # BUG: how to input linkedlist?
        temp = ListNode(None)
        temp.next = head
        while temp.next != None:
            if temp.next.next.val == node.val:
                break
            temp = temp.next
        
        temp.next = temp.next.next
                




if __name__ == "__main__":

    l1 = ListNode(4)
    l2 = ListNode(5)
    l3 = ListNode(6)
    l1.next = l2
    l2.next = l3
    l = ListNode(None)
    l.next = l1
    while l.next != None:
        print(l.next.val)
        l.next = l1.next
        break
    sol = Solution()
    sol.deleteNode(5)