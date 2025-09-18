class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = sorted(s)
        # print(f"First: {first}")
        second = sorted(t)
        # print(f"Second: {second}")

        return first == second
    
solution = Solution()
result = solution.isAnagram("racecar", "carrace")
# print(f"Result: {result}")

"""
First: ['a', 'a', 'c', 'c', 'e', 'r', 'r']
Second: ['a', 'a', 'c', 'c', 'e', 'r', 'r']
Result: True
"""
