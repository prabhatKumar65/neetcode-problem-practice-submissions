class Solution:
    def isValidSudoku(self, board):

        # Store numbers seen in each row
        rows = {}

        # Store numbers seen in each column
        cols = {}

        # Store numbers seen in each 3x3 box
        boxes = {}

        # Go through every cell of the board
        for r in range(9):
            for c in range(9):

                value = board[r][c]

                # Skip empty cells
                if value == ".":
                    continue

                # Find which 3x3 box this cell belongs to
                box = (r // 3) * 3 + (c // 3)

                # Create empty set for row if not created
                if r not in rows:
                    rows[r] = set()

                # Create empty set for column if not created
                if c not in cols:
                    cols[c] = set()

                # Create empty set for box if not created
                if box not in boxes:
                    boxes[box] = set()

                # Check duplicate in current row
                if value in rows[r]:
                    return False

                # Check duplicate in current column
                if value in cols[c]:
                    return False

                # Check duplicate in current 3x3 box
                if value in boxes[box]:
                    return False

                # Save value in row set
                rows[r].add(value)

                # Save value in column set
                cols[c].add(value)

                # Save value in box set
                boxes[box].add(value)

        # No duplicates found
        return True