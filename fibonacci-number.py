class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        current = 0
        previous1 = 1
        previous2 = 0

        # n >= 2 
        for i in range(2, n+1):
            current = previous1 + previous2

            previous2 = previous1
            previous1 = current

        return current