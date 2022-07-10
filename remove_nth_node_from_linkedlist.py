# https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # this one is considering LL starts from head and not head.next
        # size = 0
        # temp = ListNode()
        # temp = head.next
        # while temp != None:    
        #     size+=1
        #     temp = temp.next

        # temp = head.next

        # if size == 1:
        #     head = None
            
        # else:
        #     for i in range(size-n-1):
        #         temp = temp.next

        #     temp.next = temp.next.next
            
        # return head

        
        #print(head)
        size = 0
        temp = ListNode()
        temp = head
        while temp != None:    
            size+=1
            temp = temp.next

        temp = head
        
        if size == 1:
            head = None
            return head
            
        else:
            if size-n-1 >= 0:
                for i in range(size-n-1):
                    temp = temp.next

                temp.next = temp.next.next
            else:
                head = head.next
                
        return head
        

            

if __name__ == '__main__':
    head = ListNode()
    temp = ListNode()
    ls = [1,2,3,4,5,6]

    # for i in ls:
    #     node = ListNode()
    #     node.val = i
    #     if head.next == None:
    #         head.next = node
        
    #     else:
    #         temp.next.next = node                                                                                                                 
    #     temp.next = node

    for i in ls:
        node = ListNode()
        node.val = i
        if head.next == None:
            head.next = node
        
        else:
            temp.next.next = node                                                                                                                 
        temp.next = node

    print(head)
    sol = Solution()
    # head = sol.removeNthFromEnd(head,1)

    if head == None:
        print(head)
    
    else:

        temp = head.next
        while temp != None:
            print(temp.val)
            temp = temp.next
    
    