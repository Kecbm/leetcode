from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Verifica se o target existe na lista
        if target in nums:
            # Se existie, retorna o index do target
            index = nums.index(target)
            return index
        
        # Se não existir, retorna -1
        return -1

solution = Solution()
result = solution.search([-1,0,2,4,6,8], 4)
# print(f"Result: {result}")

"""
Result: 3
"""


class Solution2:
    def search2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        print(f"Iniciando busca por {target} no array {nums}")

        while left <= right:
            mid = (left + right) // 2
            print(f"left={left}, right={right}, mid={mid}, arr[mid]={nums[mid]}")

            if nums[mid] == target:
                print(f"Valor encontrado no índice {mid}")
                return mid
        
            if nums[mid] < target:
                print(f"{nums[mid]} < {target}, buscando na metade direita")
                left = mid + 1
            else:
                print(f"{nums[mid]} > {target}, buscando na metade esquerda")
                right = mid - 1
        
        print("Valor não encontrado")
        return -1
    
solution2 = Solution2()
result = solution2.search2([-1,0,2,4,6,8], 3)
print(f"Result: {result}")
"""
Iniciando busca por 3 no array [-1, 0, 2, 4, 6, 8]
left=0, right=5, mid=2, arr[mid]=2
2 < 3, buscando na metade direita
left=3, right=5, mid=4, arr[mid]=6
6 > 3, buscando na metade esquerda
left=3, right=3, mid=3, arr[mid]=4
4 > 3, buscando na metade esquerda
Valor não encontrado
Result: -1
"""
