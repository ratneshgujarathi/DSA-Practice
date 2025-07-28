class Solution:
    def soduko_solver(self, board: list[list[str]]):
        N = len(board)
        def possible(r, c, num):
            for i in range(9):
                if board[r][i] == num or board[i][c] == num:
                    return False
                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == num:
                    return False
            return True
        
        def solve(b):
            for r in range(N):
                for c in range(N):
                    if b[r][c] == ".":
                        for num in map(str, range(1, 10)):
                            if possible(r, c, num):
                                b[r][c] = num

                                if solve(b):
                                    return True
                                b[r][c] = '.'

                        return False
            return True
        
        solve(board)

s = Solution()
soduku = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
s.soduko_solver(soduku)

print(soduku)
