# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: return None
        current = head
        new_list = ListNode()
        new_list_current = new_list

        while current != None:
            if current.val != val: 
                new_list_current.next = ListNode(current.val)
                new_list_current = new_list.next
            current = current.next

        return new_list.next
    