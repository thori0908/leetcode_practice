# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []
        current = head

        while current:
            list.append(current.val)
            current = current.next

        size = len(list)

        if len == 0:
            return None

        middle = (len(list) // 2) + 1 if size % 2 == 0 else (len(list) // 2) + 1 # 小数は切り捨てられる
        

        result = head

        for i in range(middle - 1):
            result = result.next

        return result

