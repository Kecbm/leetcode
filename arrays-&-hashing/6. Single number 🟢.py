from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            # Guarda a ocorrência de cada número da lista
            count[num] = count.get(num, 0) + 1
            # print(f"Count: {count}")

        # Filtra o número que aparece apenas uma vez
        single_number = [num for num, freq in count.items() if freq == 1]
        # print(f"Single number: {single_number}")

        return single_number[0]
    
solution = Solution()
result = solution.singleNumber([7,6,6,7,8])
# print(f"Result: {result}")

"""
Count: {7: 1}
Count: {7: 1, 6: 1}
Count: {7: 1, 6: 2}
Count: {7: 2, 6: 2}
Count: {7: 2, 6: 2, 8: 1}
Single number: [8]
Result: 8
"""
