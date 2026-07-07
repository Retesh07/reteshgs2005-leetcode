# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:   
            return head
        t=head
        s=head
        m=head
        len=0
        while t!=None:
            len+=1
            t=t.next
        k=k % len
        if k==0:
            return head
    
        for i in range(len-k-1):
            s=s.next
        m=s.next
        new_head=m
        s.next=None
        while(m.next!=None):
            m=m.next
        m.next=head
        return new_head


        


        