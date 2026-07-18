class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)  # Step 1
        longest_streak = 0

        for num in num_set:  # Step 2
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:  # Step 3
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
