class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.xor(0, 0, nums)
    
    def xor(self, current_index: int, current_xor: int, nums: List[int]) -> int:
        if current_index >= len(nums)-1: return current_xor

        next_index = current_index+1
        with_current = self.xor(next_index, current_xor ^ nums[current_index], nums)
        without_current = self.xor(next_index, current_xor, nums)
        return with_current + without_current