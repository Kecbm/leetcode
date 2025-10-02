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
