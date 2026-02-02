from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_i = 0
        result = 0
        for i in range(len(height)):

            max_i = max(max_i, height[i])

            for j in range(1, len(height)):
                if height[i] < height[j]:
                    continue

                if height[i] >= height[j]:
                    if (height[i] == height[j]) == 0:
                        return result
                    
                    result += (max_i - height[j])

solution = Solution()
result = solution.trap([0,2,0,3,1,0,1,3,2,1]) # Output: 9 
# print(f"Result: {result}")

"""
Result: 0
"""


class Solution2:
    def trap2(self, height: List[int]) -> int:
        # Variável para acumular o total de água retida
        result = 0

        print(f"📊 Array de alturas: {height}")
        print(f"📏 Comprimento: {len(height)}\n")

        # Para cada posição i no array
        for i in range(len(height)):
            print(f"🔍 --- Posição i={i}, altura={height[i]} ---")

            # Encontrar a altura máxima à ESQUERDA (incluindo a posição i)
            max_left = 0

            # Percorre de 0 até i (incluindo i)
            for j in range(i + 1):
                max_left = max(max_left, height[j])

            print(f"  ⬅️  max_left (máximo de 0 até {i}): {max_left}")

            # Encontrar a altura máxima à DIREITA (incluindo a posição i)
            max_right = 0

            # Percorre de i até o final do array
            for k in range(i, len(height)):
                max_right = max(max_right, height[k])

            print(f"  ➡️  max_right (máximo de {i} até {len(height)-1}): {max_right}")

            # Calcular água retida na posição i:
            # A água retida é limitada pelo menor dos dois máximos (esquerda/direita)
            # Subtraímos a altura atual para saber quanto de água cabe acima da barra
            water = min(max_left, max_right) - height[i]
            print(f"  💧 Água retida: min({max_left}, {max_right}) - {height[i]} = {water}")

            result += water
            print(f"  🌊 Total acumulado: {result}\n")

        return result

solution2 = Solution2()
result = solution2.trap2([0,2,0,3,1,0,1,3,2,1])
print(f"===============================")
print(f"🎯 Resultado Final: {result}")

"""
📊 Array de alturas: [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
📏 Comprimento: 10

🔍 --- Posição i=0, altura=0 ---
  ⬅️  max_left (máximo de 0 até 0): 0
  ➡️  max_right (máximo de 0 até 9): 3
  💧 Água retida: min(0, 3) - 0 = 0
  🌊 Total acumulado: 0

🔍 --- Posição i=1, altura=2 ---
  ⬅️  max_left (máximo de 0 até 1): 2
  ➡️  max_right (máximo de 1 até 9): 3
  💧 Água retida: min(2, 3) - 2 = 0
  🌊 Total acumulado: 0

🔍 --- Posição i=2, altura=0 ---
  ⬅️  max_left (máximo de 0 até 2): 2
  ➡️  max_right (máximo de 2 até 9): 3
  💧 Água retida: min(2, 3) - 0 = 2
  🌊 Total acumulado: 2

🔍 --- Posição i=3, altura=3 ---
  ⬅️  max_left (máximo de 0 até 3): 3
  ➡️  max_right (máximo de 3 até 9): 3
  💧 Água retida: min(3, 3) - 3 = 0
  🌊 Total acumulado: 2

🔍 --- Posição i=4, altura=1 ---
  ⬅️  max_left (máximo de 0 até 4): 3
  ➡️  max_right (máximo de 4 até 9): 3
  💧 Água retida: min(3, 3) - 1 = 2
  🌊 Total acumulado: 4

🔍 --- Posição i=5, altura=0 ---
  ⬅️  max_left (máximo de 0 até 5): 3
  ➡️  max_right (máximo de 5 até 9): 3
  💧 Água retida: min(3, 3) - 0 = 3
  🌊 Total acumulado: 7

🔍 --- Posição i=6, altura=1 ---
  ⬅️  max_left (máximo de 0 até 6): 3
  ➡️  max_right (máximo de 6 até 9): 3
  💧 Água retida: min(3, 3) - 1 = 2
  🌊 Total acumulado: 9

🔍 --- Posição i=7, altura=3 ---
  ⬅️  max_left (máximo de 0 até 7): 3
  ➡️  max_right (máximo de 7 até 9): 3
  💧 Água retida: min(3, 3) - 3 = 0
  🌊 Total acumulado: 9

🔍 --- Posição i=8, altura=2 ---
  ⬅️  max_left (máximo de 0 até 8): 3
  ➡️  max_right (máximo de 8 até 9): 2
  💧 Água retida: min(3, 2) - 2 = 0
  🌊 Total acumulado: 9

🔍 --- Posição i=9, altura=1 ---
  ⬅️  max_left (máximo de 0 até 9): 3
  ➡️  max_right (máximo de 9 até 9): 1
  💧 Água retida: min(3, 1) - 1 = 0
  🌊 Total acumulado: 9

===============================
🎯 Resultado Final: 9
"""
