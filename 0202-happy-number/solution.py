class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            total = 0
            for digit in str(n):
                total += int(digit) ** 2

            n = total

        return True