class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n > 150:
            return 0
        if n % 2 == 0:
            return n
        return n * 2
        