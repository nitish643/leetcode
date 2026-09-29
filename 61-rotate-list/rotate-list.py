# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        temp=head
        prev=temp
        if head is None:
            return None
        cur=head
        len=0
        while cur is not None:
            len+=1
            cur=cur.next
        k=k%len
        while k>0:
            while temp.next is not None:
                prev=temp
                temp=temp.next
            temp.next=head
            head=temp
            prev.next=None
            prev=head
            k-=1
        return head