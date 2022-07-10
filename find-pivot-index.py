from turtle import left
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_all = sum(nums)

        left_sum = 0
        right_sum = sum_all

        pivot = -1

        for index, num in enumerate(nums):
            if (index == 0):
                left_sum = 0
                right_sum = right_sum - num 
            else:
                left_sum = left_sum + nums[index-1]
                right_sum = right_sum - num 

            if left_sum == right_sum:
                pivot = index
                break

        return pivot

        # left_sum[0] = 0  
        # right_sum[0] = sum_all - num[0]

        # left_sum[1] = num[0] + num[1]
        # right_sum[1] = sum_all - (num[0] + num[1])

        # left_sum[i+1] = left_sum[i] + num[i+1]
        # right_sum[i+1] = right_sum[i] - num[i+1]