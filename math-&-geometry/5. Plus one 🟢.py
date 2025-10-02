from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Converte lista para número
        number = int(''.join(map(str, digits)))
        # print(f"Number: {number}")
        number += 1
        # print(f"Number + 1: {number}")
        # Converte de volta para lista
        new_digits = list(map(int, str(number)))
        # print(f"New digits: {new_digits}")
        return new_digits
    
solution = Solution()
result = solution.plusOne([9, 9, 9])
# print(f"Result: {result}")

"""
Number: 999
Number + 1: 1000
New digits: [1, 0, 0, 0]
Result: [1, 0, 0, 0]
"""
