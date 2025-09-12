# 🥷🏾 FIRST SOLUTION
from typing import List

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
                # print(f"freq[{n}]: {freq[n]}")
            else:
                freq[n] = 1
                # print(f"create freq[{n}]: {freq[n]}")

        # Ordenar os elementos pela frequência (do maior para o menor)
        # key=lambda x: x[1] -> Ordena pelo valor (segundo elemento da tupla)
        # reverse=True -> Ordena do maior para o menor
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # print(f"Sorted items: {sorted_items}")

        # Pegar apenas os k primeiros elementos (somente as chaves)
        result = [item[0] for item in sorted_items[:k]]

        return result

solution = Solution1()
result = solution.topKFrequent([1,2,2,3,3,3], 2)
# print(f"Result: {result}")

"""
    create freq[1]: 1
    create freq[2]: 1
    freq[2]: 2
    create freq[3]: 1
    freq[3]: 2
    freq[3]: 3
    Sorted items: [(3, 3), (2, 2), (1, 1)]
    Result: [3, 2]
"""

# 🏆 FINAL SOLUTION

# In video on the site
