# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
            tortoise = head
            hare = head
            
            # Traverse the list. Since the hare moves faster, we only need to 
            # check if the hare or the hare's next node hits a null (end of list).
            while hare and hare.next:
                tortoise = tortoise.next       # Moves 1 step
                hare = hare.next.next          # Moves 2 steps
                
                # If they meet, a cycle exists
                if tortoise == hare:
                    return True
                    
            # If the loop terminates, the hare reached the end, so no cycle exists
            return False