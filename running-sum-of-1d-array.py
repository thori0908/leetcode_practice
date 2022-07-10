
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        sum = 0

        for num in nums:
            sum = sum + num
            sums.append(sum)

        return sums


        # sum[i+1] = sum[i] + num[i+1]
        # next_sum = current_sum + current_num
        # sum[2] = sum[1] + num[2]

