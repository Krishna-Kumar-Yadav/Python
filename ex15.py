
class Solution(object):
  def validity(self,boardCol):
    column = None
    row = None
    box = None
    board = [item for item in boardCol]

    for i in range(len(board)):
      board[i].sort()
      for j in range(len(board[i])-1):
        row = True
        if board[i][j] != ".":
          if (int(board[i][j]) == int(board[i][j+1])) or (int(board[i][j]) < 1 or int(board[i][j]) > 9) or (int(board[i][j+1]) < 1 or int(board[i][j+1]) > 9):
            row = False
            break
      if not row :
        break   

    print(boardCol)

       

board = [
  ["5","3",".",".","7",".",".","1","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

req = Solution()
req.validity(board)