# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        head1=head
        slow=head
        fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        if fast:
            curr=slow.next
        else:
            curr=slow
        
        
    
        prev=None
        
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        head2=prev
        while head2:
            if head1.val!=head2.val:
                return False
            head1=head1.next
            head2=head2.next
        return True

            


        
        
        