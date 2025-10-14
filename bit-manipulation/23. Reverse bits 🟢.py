class Solution:
    def reverseBits(self, n: int) -> int:
        # print(f"🔢 Input recebido: {n}")
        
        # Converter inteiro para string binária de 32 bits
        # Essa conversão é necessária para realizar a operação de slicing
        bits_string = format(n, '032b')
        
        bits_reverted = bits_string[::-1]
        # print(f"↩️  Bits revertidos: {bits_reverted}")
        
        integer_number = int(bits_reverted, 2)
        
        return integer_number

solution = Solution()
result = solution.reverseBits(int("00000000000000000000000000010101", 2))
# print(f"Result: {result}")
"""
🔢 Input recebido: 21
↩️  Bits revertidos: 10101000000000000000000000000000
Result: 2818572288
"""
