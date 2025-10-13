class Solution:
    def hammingWeight(self, n: int) -> int:
        # Converte o número para string binária
        # e conta quantos caracteres '1' existem na string
        count = bin(n).count('1')

        return count

solution = Solution()
result = solution.hammingWeight(int("00000000000000000000000000010111", 2))
print(f"Result: {result}")

"""
Result: 4
"""
