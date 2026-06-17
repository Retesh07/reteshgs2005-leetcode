class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxarea = 0

        for i, h in enumerate(heights):

            start = i

            while stack and stack[-1][1] > h:

                indx, hei = stack.pop()

                maxarea = max(maxarea, hei * (i - indx))

                start = indx

            stack.append((start, h))

        for i, h in stack:

            maxarea = max(maxarea, (len(heights) - i) * h)

        return maxarea