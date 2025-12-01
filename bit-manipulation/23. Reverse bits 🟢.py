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

# 🏆 Solution
# Brute Force

class Solution2:
    def reverseBits2(self, n: int) -> int:
        print(f"🔢 Input recebido: {n}")
        print(f"📊 Representação binária original: {format(n, '032b')}")
        print("-" * 50)
        
        binary = ""
        print("🔍 Primeira etapa: Extraindo bits um por um")
        for i in range(32):
            if n & (1 << i):
                binary += "1"
                print(f"  Posição {i:2d}: bit é 1 → binary = '{binary}'")
            else:
                binary += "0"
                print(f"  Posição {i:2d}: bit é 0 → binary = '{binary}'")
        
        print(f"\n📝 String binária construída: '{binary}'")
        print(f"🔄 String revertida: '{binary[::-1]}'")
        print("-" * 50)

        res = 0
        print("🔍 Segunda etapa: Convertendo string revertida para inteiro")
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= (1 << i)
                print(f"  Posição {i:2d}: bit é 1 → res = {res}")
            else:
                print(f"  Posição {i:2d}: bit é 0 → res = {res} (sem mudança)")

        print(f"\n✅ Resultado final: {res}")
        return res
    
solution2 = Solution2()
result = solution2.reverseBits2(int("00000000000000000000000000010101", 2))
print(f"Result: {result}")
"""
🔢 Input recebido: 21
📊 Representação binária original: 00000000000000000000000000010101
--------------------------------------------------
🔍 Primeira etapa: Extraindo bits um por um
  Posição  0: bit é 1 → binary = '1'
  Posição  1: bit é 0 → binary = '10'
  Posição  2: bit é 1 → binary = '101'
  Posição  3: bit é 0 → binary = '1010'
  Posição  4: bit é 1 → binary = '10101'
  Posição  5: bit é 0 → binary = '101010'
  Posição  6: bit é 0 → binary = '1010100'
  Posição  7: bit é 0 → binary = '10101000'
  Posição  8: bit é 0 → binary = '101010000'
  Posição  9: bit é 0 → binary = '1010100000'
  Posição 10: bit é 0 → binary = '10101000000'
  Posição 11: bit é 0 → binary = '101010000000'
  Posição 12: bit é 0 → binary = '1010100000000'
  Posição 13: bit é 0 → binary = '10101000000000'
  Posição 14: bit é 0 → binary = '101010000000000'
  Posição 15: bit é 0 → binary = '1010100000000000'
  Posição 16: bit é 0 → binary = '10101000000000000'
  Posição 17: bit é 0 → binary = '101010000000000000'
  Posição 18: bit é 0 → binary = '1010100000000000000'
  Posição 19: bit é 0 → binary = '10101000000000000000'
  Posição 20: bit é 0 → binary = '101010000000000000000'
  Posição 21: bit é 0 → binary = '1010100000000000000000'
  Posição 22: bit é 0 → binary = '10101000000000000000000'
  Posição 23: bit é 0 → binary = '101010000000000000000000'
  Posição 24: bit é 0 → binary = '1010100000000000000000000'
  Posição 25: bit é 0 → binary = '10101000000000000000000000'
  Posição 26: bit é 0 → binary = '101010000000000000000000000'
  Posição 27: bit é 0 → binary = '1010100000000000000000000000'
  Posição 28: bit é 0 → binary = '10101000000000000000000000000'
  Posição 29: bit é 0 → binary = '101010000000000000000000000000'
  Posição 30: bit é 0 → binary = '1010100000000000000000000000000'
  Posição 31: bit é 0 → binary = '10101000000000000000000000000000'

📝 String binária construída: '10101000000000000000000000000000'
🔄 String revertida: '00000000000000000000000000010101'
--------------------------------------------------
🔍 Segunda etapa: Convertendo string revertida para inteiro
  Posição  0: bit é 0 → res = 0 (sem mudança)
  Posição  1: bit é 0 → res = 0 (sem mudança)
  Posição  2: bit é 0 → res = 0 (sem mudança)
  Posição  3: bit é 0 → res = 0 (sem mudança)
  Posição  4: bit é 0 → res = 0 (sem mudança)
  Posição  5: bit é 0 → res = 0 (sem mudança)
  Posição  6: bit é 0 → res = 0 (sem mudança)
  Posição  7: bit é 0 → res = 0 (sem mudança)
  Posição  8: bit é 0 → res = 0 (sem mudança)
  Posição  9: bit é 0 → res = 0 (sem mudança)
  Posição 10: bit é 0 → res = 0 (sem mudança)
  Posição 11: bit é 0 → res = 0 (sem mudança)
  Posição 12: bit é 0 → res = 0 (sem mudança)
  Posição 13: bit é 0 → res = 0 (sem mudança)
  Posição 14: bit é 0 → res = 0 (sem mudança)
  Posição 15: bit é 0 → res = 0 (sem mudança)
  Posição 16: bit é 0 → res = 0 (sem mudança)
  Posição 17: bit é 0 → res = 0 (sem mudança)
  Posição 18: bit é 0 → res = 0 (sem mudança)
  Posição 19: bit é 0 → res = 0 (sem mudança)
  Posição 20: bit é 0 → res = 0 (sem mudança)
  Posição 21: bit é 0 → res = 0 (sem mudança)
  Posição 22: bit é 0 → res = 0 (sem mudança)
  Posição 23: bit é 0 → res = 0 (sem mudança)
  Posição 24: bit é 0 → res = 0 (sem mudança)
  Posição 25: bit é 0 → res = 0 (sem mudança)
  Posição 26: bit é 0 → res = 0 (sem mudança)
  Posição 27: bit é 1 → res = 134217728
  Posição 28: bit é 0 → res = 134217728 (sem mudança)
  Posição 29: bit é 1 → res = 671088640
  Posição 30: bit é 0 → res = 671088640 (sem mudança)
  Posição 31: bit é 1 → res = 2818572288

✅ Resultado final: 2818572288
"""
