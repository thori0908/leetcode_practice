# Definition for singly-linked list.
from heapq import merge


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        current = merged_list

        while (not list1 is None) or (not list2 is None):
            if (not list1 is None) and (not list2 is None):
                if list1.val <= list2.val:
                    current.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    current.next = ListNode(list2.val)
                    list2 = list2.next

            elif not list1 is None:
                current.next = ListNode(list1.val)
                list1 = list1.next

            elif not list2 is None:
                current.next = ListNode(list2.val)
                list2 = list2.next

            current = current.next

        return merged_list.next



        # (list1 is None) and (list2 is None):
        # (list1 is None) and (not list2 is None):
        # (not list1 is None) and (list2 is None):
        # (not list1 is None) and (not list2 is None):

        # compare
        # list1.val < list2.val -> push(list1)
        # list1.val == list2.val -> push(list1) and push(list2)
        # list1.val > list2.val ->  push(list2)

        # push list1
        # list1 = list1.next

        # push list2
        # list2 = list2.next
