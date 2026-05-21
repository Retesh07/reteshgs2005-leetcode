class Solution:
    def permuteUnique(self, nums):
        nums.sort()

        def helper(arr):
            if not arr:
                return [[]]

            perms = helper(arr[1:])
            res = []

            for p in perms:
                for i in range(len(p) + 1):
                    p_copy=p.copy()
                    p_copy.insert(i,arr[0])
                    res.append(p_copy)

                    if i < len(p) and p[i] == arr[0]:
                        break

            return res

        return helper(nums)