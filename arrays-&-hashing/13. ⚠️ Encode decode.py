from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        result = "#".join(strs)
        
        return result
        
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
            
        result = s.split("#")

        return result


solution = Solution()
result = solution.encode(["neet","code","love","you"])
# print(f"Result: {result}")
"""
Result: neet#code#love#you
"""

solution = Solution()
result = solution.decode("neet#code#love#you")
print(f"Result: {result}")
"""
Result: ['neet', 'code', 'love', 'you']
"""

# Example for solution: https://algo.monster/liteproblems/271
