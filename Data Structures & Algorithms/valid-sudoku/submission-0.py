class Solution:
    def isValidSudoku(self, board):

        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                # Ignore empty cells
                if value == ".":
                    continue

                # Find box number (0 to 8)
                box = (r // 3) * 3 + (c // 3)

                # Create sets if not present
                if r not in rows:
                    rows[r] = set()

                if c not in cols:
                    cols[c] = set()

                if box not in boxes:
                    boxes[box] = set()

                # Check duplicate in row
                if value in rows[r]:
                    return False

                # Check duplicate in column
                if value in cols[c]:
                    return False

                # Check duplicate in box
                if value in boxes[box]:
                    return False

                # Add value to row, column and box
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True