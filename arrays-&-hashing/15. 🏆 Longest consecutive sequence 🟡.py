from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_unique = list(set(nums))
        # print(f"Unique: {nums_unique}")
        nums_sorted = sorted(nums_unique)
        # print(f"Sorted: {nums_sorted}")
        sequence = []

        for i, num in enumerate(nums_sorted):
            if not sequence:
                sequence.append(num)

            if i < len(nums_sorted) - 1 and num + 1 == nums_sorted[i + 1]:
                # print(f"Num: {num}")
                # print(f"Next: {nums_sorted[i + 1]}")

                if nums_sorted[i + 1] not in sequence:
                    sequence.append(nums_sorted[i + 1])

            # print(f"Sequence: {sequence}")

        return len(sequence)
        
solution = Solution()
result = solution.longestConsecutive([2,20,4,10,3,4,5])
# print(f"Result: {result}")
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

# 🏆 Solution

class Solution2:
    def longestConsecutive2(self, nums: List[int]) -> int:
        # Variável para guardar o tamanho da maior sequência encontrada
        res = 0
        
        # Converte a lista para set para:
        # 1. Remover duplicatas automaticamente
        # 2. Permitir busca O(1) ao invés de O(n) da lista
        store = set(nums)
        # print(f"Store: {store}")

        # Percorre cada número único do array original
        for num in nums:
            # print(f"\n--- Analisando número: {num} ---")
            # Inicializa contadores para a sequência atual
            streak = 0  # Tamanho da sequência atual
            curr = num  # Número atual sendo verificado

            # print(f"Iniciando contagem a partir de: {curr}")
            
            # Conta quantos números consecutivos existem a partir de 'num'
            # Exemplo: se num=3 e temos [3,4,5], vai contar 3 números
            while curr in store:
                # print(f"Iniciando contagem a partir de: {curr}")
                streak += 1  # Incrementa o tamanho da sequência
                curr += 1    # Vai para o próximo número (3->4->5->6...)

            # print(f"Sequência terminada. Tamanho encontrado: {streak}")
            
            # Atualiza o resultado se encontrou uma sequência maior
            # max() compara o resultado atual com a sequência que acabou de contar
            res = max(res, streak)
            
        return res
    
solution2 = Solution2()
result = solution2.longestConsecutive2([9,1,4,7,3,-1,0,5,8,-1,6])
# print(f"Result: {result}")
"""
Store: {0, 1, 3, 4, 5, 6, 7, 8, 9, -1}

--- Analisando número: 9 ---
Iniciando contagem a partir de: 9
Iniciando contagem a partir de: 9
Sequência terminada. Tamanho encontrado: 1

--- Analisando número: 1 ---
Iniciando contagem a partir de: 1
Iniciando contagem a partir de: 1
Sequência terminada. Tamanho encontrado: 1

--- Analisando número: 4 ---
Iniciando contagem a partir de: 4
Iniciando contagem a partir de: 4
Iniciando contagem a partir de: 5
Iniciando contagem a partir de: 6
Iniciando contagem a partir de: 7
Iniciando contagem a partir de: 8
Iniciando contagem a partir de: 9
Sequência terminada. Tamanho encontrado: 6

--- Analisando número: 7 ---
Iniciando contagem a partir de: 7
Iniciando contagem a partir de: 7
Iniciando contagem a partir de: 8
Iniciando contagem a partir de: 9
Sequência terminada. Tamanho encontrado: 3

--- Analisando número: 3 ---
Iniciando contagem a partir de: 3
Iniciando contagem a partir de: 3
Iniciando contagem a partir de: 4
Iniciando contagem a partir de: 5
Iniciando contagem a partir de: 6
Iniciando contagem a partir de: 7
Iniciando contagem a partir de: 8
Iniciando contagem a partir de: 9
Sequência terminada. Tamanho encontrado: 7

--- Analisando número: -1 ---
Iniciando contagem a partir de: -1
Iniciando contagem a partir de: -1
Iniciando contagem a partir de: 0
Iniciando contagem a partir de: 1
Sequência terminada. Tamanho encontrado: 3

--- Analisando número: 0 ---
Iniciando contagem a partir de: 0
Iniciando contagem a partir de: 0
Iniciando contagem a partir de: 1
Sequência terminada. Tamanho encontrado: 2

--- Analisando número: 5 ---
Iniciando contagem a partir de: 5
Iniciando contagem a partir de: 5
Iniciando contagem a partir de: 6
Iniciando contagem a partir de: 7
Iniciando contagem a partir de: 8
Iniciando contagem a partir de: 9
Sequência terminada. Tamanho encontrado: 5

--- Analisando número: 8 ---
Iniciando contagem a partir de: 8
Iniciando contagem a partir de: 8
Iniciando contagem a partir de: 9
Sequência terminada. Tamanho encontrado: 2

--- Analisando número: -1 ---
Iniciando contagem a partir de: -1
Iniciando contagem a partir de: -1
Iniciando contagem a partir de: 0
Iniciando contagem a partir de: 1
Sequência terminada. Tamanho encontrado: 3

--- Analisando número: 6 ---
Iniciando contagem a partir de: 6
Iniciando contagem a partir de: 6
Iniciando contagem a partir de: 7
Iniciando contagem a partir de: 8
Iniciando contagem a partir de: 9
Sequência terminada. Tamanho encontrado: 4
Result: 7
"""
