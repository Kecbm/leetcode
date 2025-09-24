from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validação das linhas
        for row in board:
            # Números já vistos na linha
            seenRow = set()
            for num in row:
                # Ignora células vazias
                if num != '.':
                    # Se o número já foi visto na linha, é uma duplicata
                    if num in seenRow:
                        return False
                    # Adiciona o número ao conjunto de números vistos
                    seenRow.add(num)

        # Validação das colunas
        for col in range(9):
            # Números já vistos na coluna
            seenCol = set()
            # Percorre cada uma das 9 colunas
            for row in range(9):
                num = board[row][col]
                # Ignora células vazias
                if num != '.':
                    # Se o número já foi visto na coluna, é uma duplicata
                    if num in seenCol:
                        return False
                    # Adiciona o número ao conjunto de números vistos
                    seenCol.add(num)
        
        # Validação dos 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):
                # Números já vistos no box
                seenBox = set()
                # Percorre cada uma das 9 células do box
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        num = board[row][col]
                        # Ignora células vazias
                        if num != '.':
                            # Se o número já foi visto no box, é uma duplicata
                            if num in seenBox:
                                return False
                            # Adiciona o número ao conjunto de números vistos
                            seenBox.add(num)
        
        return True
    
solution = Solution()
board = (
    [["1","2",".",".","3",".",".",".","."],
     ["4",".",".","5",".",".",".",".","."],
     [".","9","8",".",".",".",".",".","3"],
     ["5",".",".",".","6",".",".",".","4"],
     [".",".",".","8",".","3",".",".","5"],
     ["7",".",".",".","2",".",".",".","6"],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".","4","1","9",".",".","8"],
     [".",".",".",".","8",".",".","7","9"]]
)
result = solution.isValidSudoku(board)
# print(f"Result: {result}")
"""
Result: True
"""


class Solution2:
    def isValid(self, numbers: List[str]) -> bool:
        seen = set()
        
        for num in numbers:
            if num != '.':
                if num in seen:
                    return False  # Duplicata encontrada
                seen.add(num)
    
        return True  # Não há duplicatas
    
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        # Validação das linhas
        for row in board:
            if not self.isValid(row):
                return False

        # Validação das colunas
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.isValid(column):
                return False
        
        # Validação dos 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):
                box = []
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        box.append(board[row][col])
                
                if not self.isValid(box):
                    return False
        
        return True

solution2 = Solution2()
board = (
    [["1","2",".",".","3",".",".",".","."],
     ["4",".",".","5",".",".",".",".","."],
     [".","9","1",".",".",".",".",".","3"],
     ["5",".",".",".","6",".",".",".","4"],
     [".",".",".","8",".","3",".",".","5"],
     ["7",".",".",".","2",".",".",".","6"],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".","4","1","9",".",".","8"],
     [".",".",".",".","8",".",".","7","9"]]
)
result = solution2.isValidSudoku2(board)
# print(f"Result: {result}")
"""
Result: False
"""
