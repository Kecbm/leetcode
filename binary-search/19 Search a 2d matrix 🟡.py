from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [item for row in matrix for item in row]

        left = 0
        right = len(arr) - 1
        # print(f"Iniciando busca por {target} no array {arr}")
        
        while left <= right:
            mid = (left + right) // 2
            # print(f"left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")

            if arr[mid] == target:
                # print(f"Valor encontrado no índice {mid}")
                return True
        
            if arr[mid] < target:
                # print(f"{arr[mid]} < {target}, buscando na metade direita")
                left = mid + 1
            else:
                # print(f"{arr[mid]} > {target}, buscando na metade esquerda")
                right = mid - 1
        
        # print("Valor não encontrado")
        return False
    
solution = Solution()
result = solution.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)
# print(f"Result: {result}")
"""
Iniciando busca por 10 no array [1, 2, 4, 8, 10, 11, 12, 13, 14, 20, 30, 40]
left=0, right=11, mid=5, arr[mid]=11
11 > 10, buscando na metade esquerda
left=0, right=4, mid=2, arr[mid]=4
4 < 10, buscando na metade direita
left=3, right=4, mid=3, arr[mid]=8
8 < 10, buscando na metade direita
left=4, right=4, mid=4, arr[mid]=10
Valor encontrado no índice 4
Result: 4
"""
