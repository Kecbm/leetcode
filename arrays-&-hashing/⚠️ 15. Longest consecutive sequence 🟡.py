from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_unique = list(set(nums))
        print(f"Unique: {nums_unique}")
        nums_sorted = sorted(nums_unique)
        print(f"Sorted: {nums_sorted}")
        sequence = []

        for i, num in enumerate(nums_sorted):
            if not sequence:
                sequence.append(num)

            if i < len(nums_sorted) - 1 and num + 1 == nums_sorted[i + 1]:
                print(f"Num: {num}")
                print(f"Next: {nums_sorted[i + 1]}")

                if nums_sorted[i + 1] not in sequence:
                    sequence.append(nums_sorted[i + 1])

            print(f"Sequence: {sequence}")

        return len(sequence)
        
solution = Solution()
result = solution.longestConsecutive([2,20,4,10,3,4,5])
print(f"Result: {result}")
"""
Unique: [2, 3, 4, 5, 10, 20]
Sorted: [2, 3, 4, 5, 10, 20]
Num: 2
Next: 3
Sequence: [2, 3]
Num: 3
Next: 4
Sequence: [2, 3, 4]
Num: 4
Next: 5
Sequence: [2, 3, 4, 5]
Sequence: [2, 3, 4, 5]
Sequence: [2, 3, 4, 5]
Sequence: [2, 3, 4, 5]
Result: 4
"""
