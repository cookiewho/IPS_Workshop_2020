def validate_sudoku_board(board):
  for x in range(0, 9):             #checks x axis
    found_y = []
    for y in range(0, 9):
      if(board[x][y] == "."):
        continue
      if board[x][y] in found_y:
        return False
      else:
        found_y.extend(board[x][y])
  for y in range(0, 9):             #checks y axis
    found_x = []
    for x in range(0, 9):
      if(board[x][y] == "."):
        continue
      if board[x][y] in found_x:
        return False
      else:
        found_x.extend(board[x][y])
  start_stop = [0, 3, 6, 9]
  z1 = 1
  z2 = 1
  while z1 <= 3:
    while z2 <= 3:
      found_box = []
      for x in range(start_stop[z1-1],start_stop[z1]):
        for y in range(start_stop[z2-1],start_stop[z2]):
          if(board[x][y] == "."):
            continue
          if board[x][y] in found_box:
            return False
          else:
            found_box.extend(board[x][y])
      z2 += 1
    z1 +=1
    z2 = 1
  return True

sudoku =[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(validate_sudoku_board(sudoku))