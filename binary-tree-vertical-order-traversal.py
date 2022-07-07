# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# answer ----------

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = {}
        x = 0
       
        queue = []
        queue.append((root, 0))

        while len(queue) > 0:
            (node, x) = queue.pop(0)
            if node is not None:
                if x in dict:
                    dict[x].append(node.val) # 注意
                else:
                    dict[x] = [node.val]
                queue.append((node.left, x-1))
                queue.append((node.right, x+1))

        # OrderedDictでdictをsortして、valuesのlistをつくっている
        return list(collections.OrderedDict(sorted(dict.items())).values())


        # rootの座標を(0,0)とする
        # left -> parentのxを-1
        # right -> parentのxを1
        # next node -> parentのdepth -1
        # sort nodes x ASC and depth DESC
        # どうやって探索する?
