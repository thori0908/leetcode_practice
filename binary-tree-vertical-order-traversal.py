# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# answer ----------

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        orders_map = {}
        queue = []
        if root:
            queue.append((root, 0))

        while queue:
            (node, x) = queue.pop(0)
            if orders_map.get(x):
                # dictのlistに要素を追加するとき、こうする
                orders_map[x].append(node.val)
            else:
                orders_map[x] = [node.val]

            if node.left:
                queue.append((node.left, x-1))
            if node.right:
                queue.append((node.right, x+1))

        return [orders_map[key] for key in sorted(orders_map.keys())]