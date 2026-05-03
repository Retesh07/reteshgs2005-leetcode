class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []

        # If only one row
        if m == 1:
            return ["." * n]

        # If only one column
        if n == 1:
            return ["." for _ in range(m)]

        # First row all free cells
        grid.append("." * n)

        # Remaining rows: block everything except last column
        for i in range(1, m):
            grid.append("#" * (n - 1) + ".")

        return grid