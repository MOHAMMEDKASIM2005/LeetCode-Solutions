class Solution:
    def solveSudoku(self, board):
        FULL = (1 << 9) - 1  # 111111111

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        # Build bitmasks
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    bit = 1 << (ord(board[r][c]) - ord('1'))
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + (c // 3)] |= bit

        def backtrack(pos):
            # All cells filled
            if pos == len(empty):
                return True

            # Find the empty cell with the fewest candidates
            best = pos
            best_mask = FULL

            for i in range(pos, len(empty)):
                r, c = empty[i]
                b = (r // 3) * 3 + (c // 3)

                used = rows[r] | cols[c] | boxes[b]
                candidates = FULL & ~used

                # No possible digit -> dead end
                if candidates == 0:
                    return False

                # Fewer candidates = better cell to try
                if candidates.bit_count() < best_mask.bit_count():
                    best = i
                    best_mask = candidates

                    # Only one possibility
                    if best_mask & (best_mask - 1) == 0:
                        break

            # Put the most constrained cell at current position
            empty[pos], empty[best] = empty[best], empty[pos]

            r, c = empty[pos]
            b = (r // 3) * 3 + (c // 3)

            mask = best_mask

            while mask:
                # Get lowest set bit
                bit = mask & -mask
                mask -= bit

                # Convert bit to digit
                digit = bit.bit_length()  # 1 -> 1, 2 -> 2, ..., 256 -> 9
                board[r][c] = str(digit)

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

                if backtrack(pos + 1):
                    return True

                # Undo
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[b] ^= bit
                board[r][c] = '.'

            # Restore ordering
            empty[pos], empty[best] = empty[best], empty[pos]

            return False

        backtrack(0)