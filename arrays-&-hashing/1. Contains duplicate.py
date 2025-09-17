from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        if not nums:
            return False

        for num in nums:
            # Guarda a ocorrência de cada número da lista
            count[num] = count.get(num, 0) + 1

        # Ordena o dicionário por ordem decrescente
        result = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

        print(f"count: {result}")

        # Verifica se o primeiro valor é maior que 1
        if list(result.values())[0] > 1:
            return True
        else:
            return False
    
solution = Solution()
result = solution.hasDuplicate([1, 2, 3, 3])
print(f"Result: {result}")

"""
count: {3: 2, 1: 1, 2: 1}
Result: True
"""
