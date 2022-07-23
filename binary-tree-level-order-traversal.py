# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = [] 
        if root:
            queue.append([root])
        else:
            return result

        current_nodes = []
        while len(queue) > 0:
            current_nodes = queue.pop(0)
            result.append(map(lambda node: node.val, current_nodes))

            tmp = []
            for node in current_nodes:
                if node.left:
                    tmp.append(node.left)

                if node.right:
                    tmp.append(node.right)

            if len(tmp) > 0:
                queue.append(tmp)
        return result