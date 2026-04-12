# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, lst in enumerate(lists):
            heapq.heappush(minHeap, [lst.val, i, lst])
        
        dummy = curr = ListNode()
        while minHeap:
            val, i, lst = heapq.heappop(minHeap)
            curr.next = lst
            curr = curr.next
            if lst.next:
                heapq.heappush(minHeap, [lst.next.val, i, lst.next])
        return dummy.next