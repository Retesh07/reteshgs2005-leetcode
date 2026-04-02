# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        l,r=head,head
        lef=left-1
        righ=right-1
        beforeleft=None
        while lef!=0:
            beforeleft=l
            l=l.next
            lef-=1
        k=l
        
        
        while righ!=0:
            r=r.next
            righ-=1
    
        afterright=r.next
        prev=None

        counter=right-left+1
        while counter!=0:
            tmp1=l.next
            l.next=prev
            prev=l
            l=tmp1
            counter-=1
        if beforeleft:

            beforeleft.next=r
        else:
            head=prev
        k.next=afterright
        return head
        

    
        

        