class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        is_duplicate = False

        for num in nums:
            if num in num_map: # これで、keyの中にあるかどうかわかる？
                num_map[num] = 1
            else:
                is_duplicate = True
                break
        
        return is_duplicate