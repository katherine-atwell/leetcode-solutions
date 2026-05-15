class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            for i in range(1, 10):
                if row.count(str(i)) > 1:
                    print("row returns false at", i)
                    return False
        for i in range(9):
            column = []
            for row in board:
                column.append(row[i])
            for j in range(1, 10):
                if column.count(str(j)) > 1:
                    print("column returns False")
                    return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = []
                print("i:", i)
                print("j:", j)
                sub_box.append(board[i][j:j+3])
                sub_box.append(board[i+1][j:j+3])
                sub_box.append(board[i+2][j:j+3])
                sub_box_items = [x for item in sub_box for x in item]
                print(sub_box_items)
                if any([sub_box_items.count(str(k)) > 1 for k in range(1, 10)]):
                    return False

        return True
