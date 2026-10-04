# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        listy=[]

        for node in lists:
            while node:
                listy.append(node.val)
                node=node.next

        listy.sort() 

        dummy = ListNode(-1)
        current = dummy

        for i in listy:
            current.next = ListNode(i)
            current = current.next

        return dummy.next
        
        