class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        l = 2
        r = num // 2

        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq < num:
                l = mid + 1
            else:
                r = mid - 1

        return False