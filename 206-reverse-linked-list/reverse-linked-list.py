# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None
        curr=head
        if head is not None:
            temp=head.next
        else:
            return head
        while temp is not None:
            curr.next=prev
            prev=curr
            curr=temp
            temp=temp.next
        curr.next=prev
        return curr