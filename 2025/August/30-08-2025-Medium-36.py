# 36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

from typing import List
import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp_j = [[],[],[],[],[],[],[],[],[]]
        tempMiniBox = [[],[],[]]
        for i in range(9):
            # print(f"Running i = {i} loop")
            temp_i = []
            for j in range(9):
                # print(f"Running j = {j} loop")
                num = board[i][j]
                if num.isdigit():
                    temp_i.append(num)
                    temp_j[j].append(num)
                    tempMiniBox[j//3].append(num)
                    # print(f'{num} added in {tempMiniBox[j//3]}')
            if len(temp_i) != len(set(temp_i)):
                return False
            # print("")

            if (i+1) % 3 == 0:
                for miniBox in tempMiniBox:
                    # print(miniBox)
                    if len(miniBox) != len(set(miniBox)):
                        return False
                tempMiniBox = [[],[],[]]
                # print(tempMiniBox)

        for t_j in temp_j:
            if len(t_j) != len(set(t_j)):
                return False
                
        return True

    
sol = Solution()
print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(sol.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(sol.isValidSudoku([[".",".",".",".",".",".","5",".","."]
                         ,[".",".",".",".",".",".",".",".","."]
                         ,[".",".",".",".",".",".",".",".","."]
                         ,["9","3",".",".","2",".","4",".","."]
                         ,[".",".","7",".",".",".","3",".","."]
                         ,[".",".",".",".",".",".",".",".","."]
                         ,[".",".",".","3","4",".",".",".","."]
                         ,[".",".",".",".",".","3",".",".","."]
                         ,[".",".",".",".",".","5","2",".","."]]))



# class Solution:
#     def isSquareUnique(self, board: List[List[str]],  m : int , n : int):
#         temp = []
#         for i in range(m, m+3):
#             for j in range(n, n+3):
#                 temp.append(board[m][n])
#         if len(temp) != len(set(temp)):
#             return False
#         return True

#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         isSudoko = True
#         print("Checking For Horzontal")
#         for i in range(9):
#             print(board[i])
#             if len(board[i]) != len(set(board[i])):
#                 isSudoko = False
#                 return isSudoko
#         for i in range(9):
#             temp = []
#             for j in range(9):
#                 temp.append(board[i][j])
#             if len(temp) != len(set(temp)):
#                 isSudoko = False
#                 return isSudoko
#             temp = []
#         for i in range(9):
#             for j in range(9):
#                 if i % 3 == 0 and j % 3 == 0:
#                     if self.isSquareUnique(board=board, m=i, n=j):
#                         pass
#                     else:
#                         return False
#         return isSudoko