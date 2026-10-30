# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        # if head is None:
        #     return head
        # temp=head
        # prev=None
        ans=ListNode(0,head)
        dummy=ans
        while dummy is not None:
            while dummy.next is not None and dummy.next.val==val:
            #     if temp==head:
            #         head=head.next
            #     else:
            #         prev.next=temp.next
            #     temp=temp.next
            # prev=temp
            # if temp:
            #     temp=temp.next
                dummy.next=dummy.next.next
            dummy=dummy.next
        return ans.next#head
                