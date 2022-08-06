class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = []
        top = len(cost)
        min_cost.append(cost[0])
        min_cost.append(cost[1])

        for current in range(2, top+1):
            if current == top:
                min_cost.append(min(min_cost[current - 1], min_cost[current - 2]))
            else:
                min_cost.append(min(min_cost[current - 1], min_cost[current - 2]) + cost[current])

        return min_cost.pop()


        # total_cost = total_prev_1_cost + current_cost or total_prev_2_cost + current_cost
        # total_min(n) = min(total_min(n-1), total_min(n-2))
        # total_min(10) = min(total_min(9), total_min(8))
        # total_min(8) =  min(total_min(8), total_min(7))