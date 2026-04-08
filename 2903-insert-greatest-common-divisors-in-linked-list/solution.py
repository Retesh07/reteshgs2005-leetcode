# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=ListNode(0)
        q=ListNode(0)

        p=head
        q=head
        q=q.next
    

        while q:
            g=self.gcd(p.val,q.val)
            k=ListNode(g)
            k.next=q
            p.next=k
            q=q.next
            p=p.next.next
        return head
    def gcd(self,a,b):
        if a%b==0:
            return b
        else:
            return self.gcd(b,a%b)
    


        