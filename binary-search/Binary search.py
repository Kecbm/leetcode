# Binary Search

# https://www.w3schools.com/python/python_dsa_binarysearch.asp

# Who it works?

# 1. First, search a target in the middle of the array
# 2. If this value is lower, search in the left half of the array
# 3. If this value is higher, search in the right half of the array
# Repeat the 2 and 3 steps until the target value is found or the search area is empty
# If the target value is found, return the index
# If the search area is empty, return -1

from typing import List

class Solution:
    def binarySearch(self, arr: List, targetVal: int) -> int:
        left = 0
        right = len(arr) - 1
        print(f"Iniciando busca por {targetVal} no array {arr}")

        while left <= right:
            mid = (left + right) // 2
            print(f"left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")

            if arr[mid] == targetVal:
                print(f"Valor encontrado no índice {mid}")
                return mid
        
            if arr[mid] < targetVal:
                print(f"{arr[mid]} < {targetVal}, buscando na metade direita")
                left = mid + 1
            else:
                print(f"{arr[mid]} > {targetVal}, buscando na metade esquerda")
                right = mid - 1
        
        print("Valor não encontrado")
        return -1
    
solution = Solution()
result = solution.binarySearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 11)
print(f"Result: {result}")
"""
Iniciando busca por 11 no array [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
left=0, right=9, mid=4, arr[mid]=9
9 < 11, buscando na metade direita
left=5, right=9, mid=7, arr[mid]=15
15 > 11, buscando na metade esquerda
left=5, right=6, mid=5, arr[mid]=11
Valor encontrado no índice 5
Result: 5
"""