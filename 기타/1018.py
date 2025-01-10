def change(board, row, col, color):
    colors = ['B', 'W']
    count = 0
    for i in range(8):
        for j in range(8):
            expected_color = colors[(i + j) % 2] if color == 'B' else colors[(i + j + 1) % 2]
            if board[row + i][col + j] != expected_color:
                count += 1
    return count

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

min_changes = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        changes_B = change(board, i, j, 'B')
        changes_W = change(board, i, j, 'W')
        min_changes = min(min_changes, changes_B, changes_W)

print(min_changes)