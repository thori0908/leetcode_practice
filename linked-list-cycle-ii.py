# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       # 3, 2, 0, 4, 2, 0, 4, 2, 0, 4 -> a[i+k] + b[i+k] = a[i] + b[i] and (a[i+k] = a[i], b[i+k] = b[i])
       # {}
