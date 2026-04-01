# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy

        minheap=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minheap, (lists[i].val, i, lists[i]))
        while minheap:
            val,indx,l=heapq.heappop(minheap)
            tail.next=l
            tail=tail.next
            if l.next:
                heapq.heappush(minheap,(l.next.val,indx,l.next))
  
        return dummy.next
        

        
 
        