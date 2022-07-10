from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=lambda str: len(str))

        left = 1 # stringのindex 1は1文字目。0だと空文字列
        right = len(shortest)
        prefix_at = (right + left) // 2

        if not self.isPrefixAt(left, strs):
            return ""

        if self.isPrefixAt(right, strs):
            return shortest

        while right - left > 1:
            if self.isPrefixAt(prefix_at, strs):
                left = prefix_at
            else:
                right = prefix_at

            prefix_at = (right + left) // 2

        return shortest[0:prefix_at]

    def isPrefixAt(self, prefix_at: int, strs: List[str]) -> bool:
        return all(str.startswith(strs[0][:prefix_at]) for str in strs)
