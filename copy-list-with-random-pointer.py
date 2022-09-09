# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head 

        dict = {}
        copied = Node(0)
        current_copied = copied
        current_origin = head

        while current_origin:
            new_node = Node(current_origin.val, None, None)
            dict[id(current_origin)] = new_node
            current_copied.next = new_node

            current_copied = current_copied.next
            current_origin = current_origin.next

        current_copied = copied.next
        current_origin = head
        
        while current_origin:
            if current_origin.random:
                current_copied.random = dict[id(current_origin.random)]
            else:
                current_copied.random = None

            current_copied = current_copied.next
            current_origin = current_origin.next


        return copied.next