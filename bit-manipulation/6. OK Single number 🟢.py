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


# 🏆 Solution
# Hash Set

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        # print(f"🚀 Starting with nums: {nums}")
        
        for num in nums:
            if num in seen:
                seen.remove(num)
                # print(f"❌ Removed {num} from seen. Current seen: {seen}")
            else:
                seen.add(num)
                # print(f"✅ Added {num} to seen. Current seen: {seen}")
        
        result = list(seen)[0]
        # print(f"🎯 Final result: {result}")
        return result

solution2 = Solution2()
result = solution2.singleNumber([3,2,3])
# print(result)
"""
🚀 Starting with nums: [3, 2, 3]
✅ Added 3 to seen. Current seen: {3}
✅ Added 2 to seen. Current seen: {2, 3}
❌ Removed 3 from seen. Current seen: {2}
🎯 Final result: 2
"""
