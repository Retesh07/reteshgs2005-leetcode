class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            n = len(arr)
            left = merge_sort(arr[:n // 2])
            right = merge_sort(arr[n // 2:])
            return merge(left, right)

        def merge(left, right):
            i, j = 0, 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            res.extend(left[i:])
            res.extend(right[j:])
            return res

        return merge_sort(nums)