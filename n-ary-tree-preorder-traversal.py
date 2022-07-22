# Definition for a Node.

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        orders = []
        stack = []
        parent = root

        while parent:
            orders.append(parent.val)
            stack.extend(parent.children[::-1]) # [::-1]でlistが逆になる？

            if len(stack) == 0:
                parent = None
            else:
                parent = stack.pop()

        return orders

        # children 1,3,2,4
        # parent children.pop(0)
        # parent.children + oldchildren
