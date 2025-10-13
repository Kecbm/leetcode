from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # print(f"🔢 Iniciando countBits com n = {n}")
        binary_list = []
        
        for i in range(n + 1):
            # Transformar número inteiro > bits
            binary_str = bin(i)[2:]
            # print(f"  {i} -> '{binary_str}'")
            # Adicionar o número em bits na lista
            binary_list.append(binary_str)

        # print(f"📋 Binary list: {binary_list}")
        # print("-" * 40)

        # Iterar no número em bits e conta a quantidade de 1's
        # Adicionar a quantidade de 1s em uma lista
        count_ones_list = []

        for binary_str in binary_list:
            cout_ones = binary_str.count('1')
            # print(f"  '{binary_str}' tem {cout_ones} uns")
            count_ones_list.append(cout_ones)

        return count_ones_list

solution = Solution()
result = solution.countBits(4)
# print(f"Result: {result}")

"""
🔢 Iniciando countBits com n = 4
  0 -> '0'
  1 -> '1'
  2 -> '10'
  3 -> '11'
  4 -> '100'
📋 Binary list: ['0', '1', '10', '11', '100']
----------------------------------------
  '0' tem 0 uns
  '1' tem 1 uns
  '10' tem 1 uns
  '11' tem 2 uns
  '100' tem 1 uns
Result: [0, 1, 1, 2, 1]
"""
