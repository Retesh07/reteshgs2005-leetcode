from collections import defaultdict
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empties.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def dfs():
            if not empties:
                return True

            # choose cell with minimum possible values
            min_idx = -1
            min_choices = None

            for idx, (i, j) in enumerate(empties):
                box_id = (i // 3) * 3 + (j // 3)
                choices = []
                for ch in "123456789":
                    if ch not in rows[i] and ch not in cols[j] and ch not in boxes[box_id]:
                        choices.append(ch)

                if min_choices is None or len(choices) < len(min_choices):
                    min_choices = choices
                    min_idx = idx

                if len(min_choices) == 1:
                    break

            if not min_choices:
                return False

            i, j = empties[min_idx]
            box_id = (i // 3) * 3 + (j // 3)

            empties[min_idx], empties[-1] = empties[-1], empties[min_idx]
            empties.pop()

            for ch in min_choices:
                board[i][j] = ch
                rows[i].add(ch)
                cols[j].add(ch)
                boxes[box_id].add(ch)

                if dfs():
                    return True

                board[i][j] = "."
                rows[i].remove(ch)
                cols[j].remove(ch)
                boxes[box_id].remove(ch)

            empties.append((i, j))
            return False

        dfs()