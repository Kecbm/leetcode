from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return heights[0] * heights[1]
    
solution = Solution()
result = solution.maxArea([2, 2, 2])
# print(f"Result: {result}")

"""
Result: 4
"""

class Solution2:
    def maxArea2(self, heights: List[int]) -> int:
        # Two Pointers
        # i is ths left
        right = len(heights) - 1

        for i in range(len(heights)):
            if (heights[i] < heights[right]):
                i += 1
                continue
            
            if (heights[i] <= heights[right]):
                return heights[i] * heights[right]

    
solution2 = Solution2()
result2 = solution2.maxArea2([1,7,2,5,4,7,3,6])
# print(f"Result: {result2}")

"""
Result: 36
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return heights[0] * heights[1]
    
solution = Solution()
result = solution.maxArea([2, 2, 2])
# print(f"Result: {result}")

"""
Result: 4
"""

# 🏆 Solution

class Solution3:
    def maxArea3(self, heights: List[int]) -> int:
        print(f"\n🚀 Iniciando maxArea3 com heights: {heights}")
        print(f"📏 Tamanho do array: {len(heights)}\n")

        res = 0
        print(f"💧 Área máxima inicial: {res}\n")

        for i in range(len(heights)):
            print(f"{'='*60}")
            print(f"🔵 Ponteiro esquerdo i={i}, altura[{i}]={heights[i]}")

            for j in range(i + 1, len(heights)):
                altura_esquerda = heights[i]
                altura_direita = heights[j]
                altura_minima = min(altura_esquerda, altura_direita)
                largura = j - i
                area_atual = altura_minima * largura

                print(f"  🔴 Ponteiro direito j={j}, altura[{j}]={altura_direita}")
                print(f"     📐 Largura (j-i): {j}-{i} = {largura}")
                print(f"     📊 Altura mínima: min({altura_esquerda}, {altura_direita}) = {altura_minima}")
                print(f"     🧮 Área calculada: {altura_minima} × {largura} = {area_atual}")
                print(f"     🏆 Área máxima anterior: {res}")

                res = max(res, area_atual)

                if area_atual > res or area_atual == res:
                    print(f"     ✅ Nova área máxima: {res}")
                else:
                    print(f"     ❌ Área atual ({area_atual}) não supera máxima ({res})")
                print()

        print(f"{'='*60}")
        print(f"🎯 RESULTADO FINAL: {res}\n")
        return res
    
solution3 = Solution3()
result3 = solution3.maxArea3([1,7,2,5,12,3,500,500,7,8,4,7,3,6])

"""
🚀 Iniciando maxArea3 com heights: [1, 7, 2, 5, 12, 3, 500, 500, 7, 8, 4, 7, 3, 6]
📏 Tamanho do array: 14

💧 Área máxima inicial: 0

============================================================
🔵 Ponteiro esquerdo i=0, altura[0]=1
  🔴 Ponteiro direito j=1, altura[1]=7
     📐 Largura (j-i): 1-0 = 1
     📊 Altura mínima: min(1, 7) = 1
     🧮 Área calculada: 1 × 1 = 1
     🏆 Área máxima anterior: 0
     ✅ Nova área máxima: 1

  🔴 Ponteiro direito j=2, altura[2]=2
     📐 Largura (j-i): 2-0 = 2
     📊 Altura mínima: min(1, 2) = 1
     🧮 Área calculada: 1 × 2 = 2
     🏆 Área máxima anterior: 1
     ✅ Nova área máxima: 2

  🔴 Ponteiro direito j=3, altura[3]=5
     📐 Largura (j-i): 3-0 = 3
     📊 Altura mínima: min(1, 5) = 1
     🧮 Área calculada: 1 × 3 = 3
     🏆 Área máxima anterior: 2
     ✅ Nova área máxima: 3

  🔴 Ponteiro direito j=4, altura[4]=12
     📐 Largura (j-i): 4-0 = 4
     📊 Altura mínima: min(1, 12) = 1
     🧮 Área calculada: 1 × 4 = 4
     🏆 Área máxima anterior: 3
     ✅ Nova área máxima: 4

  🔴 Ponteiro direito j=5, altura[5]=3
     📐 Largura (j-i): 5-0 = 5
     📊 Altura mínima: min(1, 3) = 1
     🧮 Área calculada: 1 × 5 = 5
     🏆 Área máxima anterior: 4
     ✅ Nova área máxima: 5

  🔴 Ponteiro direito j=6, altura[6]=500
     📐 Largura (j-i): 6-0 = 6
     📊 Altura mínima: min(1, 500) = 1
     🧮 Área calculada: 1 × 6 = 6
     🏆 Área máxima anterior: 5
     ✅ Nova área máxima: 6

  🔴 Ponteiro direito j=7, altura[7]=500
     📐 Largura (j-i): 7-0 = 7
     📊 Altura mínima: min(1, 500) = 1
     🧮 Área calculada: 1 × 7 = 7
     🏆 Área máxima anterior: 6
     ✅ Nova área máxima: 7

  🔴 Ponteiro direito j=8, altura[8]=7
     📐 Largura (j-i): 8-0 = 8
     📊 Altura mínima: min(1, 7) = 1
     🧮 Área calculada: 1 × 8 = 8
     🏆 Área máxima anterior: 7
     ✅ Nova área máxima: 8

  🔴 Ponteiro direito j=9, altura[9]=8
     📐 Largura (j-i): 9-0 = 9
     📊 Altura mínima: min(1, 8) = 1
     🧮 Área calculada: 1 × 9 = 9
     🏆 Área máxima anterior: 8
     ✅ Nova área máxima: 9

  🔴 Ponteiro direito j=10, altura[10]=4
     📐 Largura (j-i): 10-0 = 10
     📊 Altura mínima: min(1, 4) = 1
     🧮 Área calculada: 1 × 10 = 10
     🏆 Área máxima anterior: 9
     ✅ Nova área máxima: 10

  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-0 = 11
     📊 Altura mínima: min(1, 7) = 1
     🧮 Área calculada: 1 × 11 = 11
     🏆 Área máxima anterior: 10
     ✅ Nova área máxima: 11

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-0 = 12
     📊 Altura mínima: min(1, 3) = 1
     🧮 Área calculada: 1 × 12 = 12
     🏆 Área máxima anterior: 11
     ✅ Nova área máxima: 12

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-0 = 13
     📊 Altura mínima: min(1, 6) = 1
     🧮 Área calculada: 1 × 13 = 13
     🏆 Área máxima anterior: 12
     ✅ Nova área máxima: 13

============================================================
🔵 Ponteiro esquerdo i=1, altura[1]=7
  🔴 Ponteiro direito j=2, altura[2]=2
     📐 Largura (j-i): 2-1 = 1
     📊 Altura mínima: min(7, 2) = 2
     🧮 Área calculada: 2 × 1 = 2
     🏆 Área máxima anterior: 13
     ❌ Área atual (2) não supera máxima (13)

  🔴 Ponteiro direito j=3, altura[3]=5
     📐 Largura (j-i): 3-1 = 2
     📊 Altura mínima: min(7, 5) = 5
     🧮 Área calculada: 5 × 2 = 10
     🏆 Área máxima anterior: 13
     ❌ Área atual (10) não supera máxima (13)

  🔴 Ponteiro direito j=4, altura[4]=12
     📐 Largura (j-i): 4-1 = 3
     📊 Altura mínima: min(7, 12) = 7
     🧮 Área calculada: 7 × 3 = 21
     🏆 Área máxima anterior: 13
     ✅ Nova área máxima: 21

  🔴 Ponteiro direito j=5, altura[5]=3
     📐 Largura (j-i): 5-1 = 4
     📊 Altura mínima: min(7, 3) = 3
     🧮 Área calculada: 3 × 4 = 12
     🏆 Área máxima anterior: 21
     ❌ Área atual (12) não supera máxima (21)

  🔴 Ponteiro direito j=6, altura[6]=500
     📐 Largura (j-i): 6-1 = 5
     📊 Altura mínima: min(7, 500) = 7
     🧮 Área calculada: 7 × 5 = 35
     🏆 Área máxima anterior: 21
     ✅ Nova área máxima: 35

  🔴 Ponteiro direito j=7, altura[7]=500
     📐 Largura (j-i): 7-1 = 6
     📊 Altura mínima: min(7, 500) = 7
     🧮 Área calculada: 7 × 6 = 42
     🏆 Área máxima anterior: 35
     ✅ Nova área máxima: 42

  🔴 Ponteiro direito j=8, altura[8]=7
     📐 Largura (j-i): 8-1 = 7
     📊 Altura mínima: min(7, 7) = 7
     🧮 Área calculada: 7 × 7 = 49
     🏆 Área máxima anterior: 42
     ✅ Nova área máxima: 49

  🔴 Ponteiro direito j=9, altura[9]=8
     📐 Largura (j-i): 9-1 = 8
     📊 Altura mínima: min(7, 8) = 7
     🧮 Área calculada: 7 × 8 = 56
     🏆 Área máxima anterior: 49
     ✅ Nova área máxima: 56

  🔴 Ponteiro direito j=10, altura[10]=4
     📐 Largura (j-i): 10-1 = 9
     📊 Altura mínima: min(7, 4) = 4
     🧮 Área calculada: 4 × 9 = 36
     🏆 Área máxima anterior: 56
     ❌ Área atual (36) não supera máxima (56)

  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-1 = 10
     📊 Altura mínima: min(7, 7) = 7
     🧮 Área calculada: 7 × 10 = 70
     🏆 Área máxima anterior: 56
     ✅ Nova área máxima: 70

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-1 = 11
     📊 Altura mínima: min(7, 3) = 3
     🧮 Área calculada: 3 × 11 = 33
     🏆 Área máxima anterior: 70
     ❌ Área atual (33) não supera máxima (70)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-1 = 12
     📊 Altura mínima: min(7, 6) = 6
     🧮 Área calculada: 6 × 12 = 72
     🏆 Área máxima anterior: 70
     ✅ Nova área máxima: 72

============================================================
🔵 Ponteiro esquerdo i=2, altura[2]=2
  🔴 Ponteiro direito j=3, altura[3]=5
     📐 Largura (j-i): 3-2 = 1
     📊 Altura mínima: min(2, 5) = 2
     🧮 Área calculada: 2 × 1 = 2
     🏆 Área máxima anterior: 72
     ❌ Área atual (2) não supera máxima (72)

  🔴 Ponteiro direito j=4, altura[4]=12
     📐 Largura (j-i): 4-2 = 2
     📊 Altura mínima: min(2, 12) = 2
     🧮 Área calculada: 2 × 2 = 4
     🏆 Área máxima anterior: 72
     ❌ Área atual (4) não supera máxima (72)

  🔴 Ponteiro direito j=5, altura[5]=3
     📐 Largura (j-i): 5-2 = 3
     📊 Altura mínima: min(2, 3) = 2
     🧮 Área calculada: 2 × 3 = 6
     🏆 Área máxima anterior: 72
     ❌ Área atual (6) não supera máxima (72)

  🔴 Ponteiro direito j=6, altura[6]=500
     📐 Largura (j-i): 6-2 = 4
     📊 Altura mínima: min(2, 500) = 2
     🧮 Área calculada: 2 × 4 = 8
     🏆 Área máxima anterior: 72
     ❌ Área atual (8) não supera máxima (72)

  🔴 Ponteiro direito j=7, altura[7]=500
     📐 Largura (j-i): 7-2 = 5
     📊 Altura mínima: min(2, 500) = 2
     🧮 Área calculada: 2 × 5 = 10
     🏆 Área máxima anterior: 72
     ❌ Área atual (10) não supera máxima (72)

  🔴 Ponteiro direito j=8, altura[8]=7
     📐 Largura (j-i): 8-2 = 6
     📊 Altura mínima: min(2, 7) = 2
     🧮 Área calculada: 2 × 6 = 12
     🏆 Área máxima anterior: 72
     ❌ Área atual (12) não supera máxima (72)

  🔴 Ponteiro direito j=9, altura[9]=8
     📐 Largura (j-i): 9-2 = 7
     📊 Altura mínima: min(2, 8) = 2
     🧮 Área calculada: 2 × 7 = 14
     🏆 Área máxima anterior: 72
     ❌ Área atual (14) não supera máxima (72)

  🔴 Ponteiro direito j=10, altura[10]=4
     📐 Largura (j-i): 10-2 = 8
     📊 Altura mínima: min(2, 4) = 2
     🧮 Área calculada: 2 × 8 = 16
     🏆 Área máxima anterior: 72
     ❌ Área atual (16) não supera máxima (72)

  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-2 = 9
     📊 Altura mínima: min(2, 7) = 2
     🧮 Área calculada: 2 × 9 = 18
     🏆 Área máxima anterior: 72
     ❌ Área atual (18) não supera máxima (72)

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-2 = 10
     📊 Altura mínima: min(2, 3) = 2
     🧮 Área calculada: 2 × 10 = 20
     🏆 Área máxima anterior: 72
     ❌ Área atual (20) não supera máxima (72)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-2 = 11
     📊 Altura mínima: min(2, 6) = 2
     🧮 Área calculada: 2 × 11 = 22
     🏆 Área máxima anterior: 72
     ❌ Área atual (22) não supera máxima (72)

============================================================
🔵 Ponteiro esquerdo i=3, altura[3]=5
  🔴 Ponteiro direito j=4, altura[4]=12
     📐 Largura (j-i): 4-3 = 1
     📊 Altura mínima: min(5, 12) = 5
     🧮 Área calculada: 5 × 1 = 5
     🏆 Área máxima anterior: 72
     ❌ Área atual (5) não supera máxima (72)

  🔴 Ponteiro direito j=5, altura[5]=3
     📐 Largura (j-i): 5-3 = 2
     📊 Altura mínima: min(5, 3) = 3
     🧮 Área calculada: 3 × 2 = 6
     🏆 Área máxima anterior: 72
     ❌ Área atual (6) não supera máxima (72)

  🔴 Ponteiro direito j=6, altura[6]=500
     📐 Largura (j-i): 6-3 = 3
     📊 Altura mínima: min(5, 500) = 5
     🧮 Área calculada: 5 × 3 = 15
     🏆 Área máxima anterior: 72
     ❌ Área atual (15) não supera máxima (72)

  🔴 Ponteiro direito j=7, altura[7]=500
     📐 Largura (j-i): 7-3 = 4
     📊 Altura mínima: min(5, 500) = 5
     🧮 Área calculada: 5 × 4 = 20
     🏆 Área máxima anterior: 72
     ❌ Área atual (20) não supera máxima (72)

  🔴 Ponteiro direito j=8, altura[8]=7
     📐 Largura (j-i): 8-3 = 5
     📊 Altura mínima: min(5, 7) = 5
     🧮 Área calculada: 5 × 5 = 25
     🏆 Área máxima anterior: 72
     ❌ Área atual (25) não supera máxima (72)

  🔴 Ponteiro direito j=9, altura[9]=8
     📐 Largura (j-i): 9-3 = 6
     📊 Altura mínima: min(5, 8) = 5
     🧮 Área calculada: 5 × 6 = 30
     🏆 Área máxima anterior: 72
     ❌ Área atual (30) não supera máxima (72)

  🔴 Ponteiro direito j=10, altura[10]=4
     📐 Largura (j-i): 10-3 = 7
     📊 Altura mínima: min(5, 4) = 4
     🧮 Área calculada: 4 × 7 = 28
     🏆 Área máxima anterior: 72
     ❌ Área atual (28) não supera máxima (72)

  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-3 = 8
     📊 Altura mínima: min(5, 7) = 5
     🧮 Área calculada: 5 × 8 = 40
     🏆 Área máxima anterior: 72
     ❌ Área atual (40) não supera máxima (72)

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-3 = 9
     📊 Altura mínima: min(5, 3) = 3
     🧮 Área calculada: 3 × 9 = 27
     🏆 Área máxima anterior: 72
     ❌ Área atual (27) não supera máxima (72)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-3 = 10
     📊 Altura mínima: min(5, 6) = 5
     🧮 Área calculada: 5 × 10 = 50
     🏆 Área máxima anterior: 72
     ❌ Área atual (50) não supera máxima (72)

============================================================
🔵 Ponteiro esquerdo i=4, altura[4]=12
  🔴 Ponteiro direito j=5, altura[5]=3
     📐 Largura (j-i): 5-4 = 1
     📊 Altura mínima: min(12, 3) = 3
     🧮 Área calculada: 3 × 1 = 3
     🏆 Área máxima anterior: 72
     ❌ Área atual (3) não supera máxima (72)

  🔴 Ponteiro direito j=6, altura[6]=500
     📐 Largura (j-i): 6-4 = 2
     📊 Altura mínima: min(12, 500) = 12
     🧮 Área calculada: 12 × 2 = 24
     🏆 Área máxima anterior: 72
     ❌ Área atual (24) não supera máxima (72)

  🔴 Ponteiro direito j=7, altura[7]=500
     📐 Largura (j-i): 7-4 = 3
     📊 Altura mínima: min(12, 500) = 12
     🧮 Área calculada: 12 × 3 = 36
     🏆 Área máxima anterior: 72
     ❌ Área atual (36) não supera máxima (72)

  🔴 Ponteiro direito j=8, altura[8]=7
     📐 Largura (j-i): 8-4 = 4
     📊 Altura mínima: min(12, 7) = 7
     🧮 Área calculada: 7 × 4 = 28
     🏆 Área máxima anterior: 72
     ❌ Área atual (28) não supera máxima (72)

  🔴 Ponteiro direito j=9, altura[9]=8
     📐 Largura (j-i): 9-4 = 5
     📊 Altura mínima: min(12, 8) = 8
     🧮 Área calculada: 8 × 5 = 40
     🏆 Área máxima anterior: 72
     ❌ Área atual (40) não supera máxima (72)

  🔴 Ponteiro direito j=10, altura[10]=4
     📐 Largura (j-i): 10-4 = 6
     📊 Altura mínima: min(12, 4) = 4
     🧮 Área calculada: 4 × 6 = 24
     🏆 Área máxima anterior: 72
     ❌ Área atual (24) não supera máxima (72)

  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-4 = 7
     📊 Altura mínima: min(12, 7) = 7
     🧮 Área calculada: 7 × 7 = 49
     🏆 Área máxima anterior: 72
     ❌ Área atual (49) não supera máxima (72)

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-4 = 8
     📊 Altura mínima: min(12, 3) = 3
     🧮 Área calculada: 3 × 8 = 24
     🏆 Área máxima anterior: 72
     ❌ Área atual (24) não supera máxima (72)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-4 = 9
     📊 Altura mínima: min(12, 6) = 6
     🧮 Área calculada: 6 × 9 = 54
     🏆 Área máxima anterior: 72
     ❌ Área atual (54) não supera máxima (72)

============================================================
🔵 Ponteiro esquerdo i=5, altura[5]=3
  🔴 Ponteiro direito j=6, altura[6]=500
     📐 Largura (j-i): 6-5 = 1
     📊 Altura mínima: min(3, 500) = 3
     🧮 Área calculada: 3 × 1 = 3
     🏆 Área máxima anterior: 72
     ❌ Área atual (3) não supera máxima (72)

  🔴 Ponteiro direito j=7, altura[7]=500
     📐 Largura (j-i): 7-5 = 2
     📊 Altura mínima: min(3, 500) = 3
     🧮 Área calculada: 3 × 2 = 6
     🏆 Área máxima anterior: 72
     ❌ Área atual (6) não supera máxima (72)

  🔴 Ponteiro direito j=8, altura[8]=7
     📐 Largura (j-i): 8-5 = 3
     📊 Altura mínima: min(3, 7) = 3
     🧮 Área calculada: 3 × 3 = 9
     🏆 Área máxima anterior: 72
     ❌ Área atual (9) não supera máxima (72)

  🔴 Ponteiro direito j=9, altura[9]=8
     📐 Largura (j-i): 9-5 = 4
     📊 Altura mínima: min(3, 8) = 3
     🧮 Área calculada: 3 × 4 = 12
     🏆 Área máxima anterior: 72
     ❌ Área atual (12) não supera máxima (72)

  🔴 Ponteiro direito j=10, altura[10]=4
     📐 Largura (j-i): 10-5 = 5
     📊 Altura mínima: min(3, 4) = 3
     🧮 Área calculada: 3 × 5 = 15
     🏆 Área máxima anterior: 72
     ❌ Área atual (15) não supera máxima (72)

  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-5 = 6
     📊 Altura mínima: min(3, 7) = 3
     🧮 Área calculada: 3 × 6 = 18
     🏆 Área máxima anterior: 72
     ❌ Área atual (18) não supera máxima (72)

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-5 = 7
     📊 Altura mínima: min(3, 3) = 3
     🧮 Área calculada: 3 × 7 = 21
     🏆 Área máxima anterior: 72
     ❌ Área atual (21) não supera máxima (72)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-5 = 8
     📊 Altura mínima: min(3, 6) = 3
     🧮 Área calculada: 3 × 8 = 24
     🏆 Área máxima anterior: 72
     ❌ Área atual (24) não supera máxima (72)

============================================================
🔵 Ponteiro esquerdo i=6, altura[6]=500
  🔴 Ponteiro direito j=7, altura[7]=500
     📐 Largura (j-i): 7-6 = 1
     📊 Altura mínima: min(500, 500) = 500
     🧮 Área calculada: 500 × 1 = 500
     🏆 Área máxima anterior: 72
     ✅ Nova área máxima: 500

  🔴 Ponteiro direito j=8, altura[8]=7
     📐 Largura (j-i): 8-6 = 2
     📊 Altura mínima: min(500, 7) = 7
     🧮 Área calculada: 7 × 2 = 14
     🏆 Área máxima anterior: 500
     ❌ Área atual (14) não supera máxima (500)

  🔴 Ponteiro direito j=9, altura[9]=8
     📐 Largura (j-i): 9-6 = 3
     📊 Altura mínima: min(500, 8) = 8
     🧮 Área calculada: 8 × 3 = 24
     🏆 Área máxima anterior: 500
     ❌ Área atual (24) não supera máxima (500)

  🔴 Ponteiro direito j=10, altura[10]=4
     📐 Largura (j-i): 10-6 = 4
     📊 Altura mínima: min(500, 4) = 4
     🧮 Área calculada: 4 × 4 = 16
     🏆 Área máxima anterior: 500
     ❌ Área atual (16) não supera máxima (500)

  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-6 = 5
     📊 Altura mínima: min(500, 7) = 7
     🧮 Área calculada: 7 × 5 = 35
     🏆 Área máxima anterior: 500
     ❌ Área atual (35) não supera máxima (500)

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-6 = 6
     📊 Altura mínima: min(500, 3) = 3
     🧮 Área calculada: 3 × 6 = 18
     🏆 Área máxima anterior: 500
     ❌ Área atual (18) não supera máxima (500)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-6 = 7
     📊 Altura mínima: min(500, 6) = 6
     🧮 Área calculada: 6 × 7 = 42
     🏆 Área máxima anterior: 500
     ❌ Área atual (42) não supera máxima (500)

============================================================
🔵 Ponteiro esquerdo i=7, altura[7]=500
  🔴 Ponteiro direito j=8, altura[8]=7
     📐 Largura (j-i): 8-7 = 1
     📊 Altura mínima: min(500, 7) = 7
     🧮 Área calculada: 7 × 1 = 7
     🏆 Área máxima anterior: 500
     ❌ Área atual (7) não supera máxima (500)

  🔴 Ponteiro direito j=9, altura[9]=8
     📐 Largura (j-i): 9-7 = 2
     📊 Altura mínima: min(500, 8) = 8
     🧮 Área calculada: 8 × 2 = 16
     🏆 Área máxima anterior: 500
     ❌ Área atual (16) não supera máxima (500)

  🔴 Ponteiro direito j=10, altura[10]=4
     📐 Largura (j-i): 10-7 = 3
     📊 Altura mínima: min(500, 4) = 4
     🧮 Área calculada: 4 × 3 = 12
     🏆 Área máxima anterior: 500
     ❌ Área atual (12) não supera máxima (500)

  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-7 = 4
     📊 Altura mínima: min(500, 7) = 7
     🧮 Área calculada: 7 × 4 = 28
     🏆 Área máxima anterior: 500
     ❌ Área atual (28) não supera máxima (500)

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-7 = 5
     📊 Altura mínima: min(500, 3) = 3
     🧮 Área calculada: 3 × 5 = 15
     🏆 Área máxima anterior: 500
     ❌ Área atual (15) não supera máxima (500)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-7 = 6
     📊 Altura mínima: min(500, 6) = 6
     🧮 Área calculada: 6 × 6 = 36
     🏆 Área máxima anterior: 500
     ❌ Área atual (36) não supera máxima (500)

============================================================
🔵 Ponteiro esquerdo i=8, altura[8]=7
  🔴 Ponteiro direito j=9, altura[9]=8
     📐 Largura (j-i): 9-8 = 1
     📊 Altura mínima: min(7, 8) = 7
     🧮 Área calculada: 7 × 1 = 7
     🏆 Área máxima anterior: 500
     ❌ Área atual (7) não supera máxima (500)

  🔴 Ponteiro direito j=10, altura[10]=4
     📐 Largura (j-i): 10-8 = 2
     📊 Altura mínima: min(7, 4) = 4
     🧮 Área calculada: 4 × 2 = 8
     🏆 Área máxima anterior: 500
     ❌ Área atual (8) não supera máxima (500)

  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-8 = 3
     📊 Altura mínima: min(7, 7) = 7
     🧮 Área calculada: 7 × 3 = 21
     🏆 Área máxima anterior: 500
     ❌ Área atual (21) não supera máxima (500)

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-8 = 4
     📊 Altura mínima: min(7, 3) = 3
     🧮 Área calculada: 3 × 4 = 12
     🏆 Área máxima anterior: 500
     ❌ Área atual (12) não supera máxima (500)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-8 = 5
     📊 Altura mínima: min(7, 6) = 6
     🧮 Área calculada: 6 × 5 = 30
     🏆 Área máxima anterior: 500
     ❌ Área atual (30) não supera máxima (500)

============================================================
🔵 Ponteiro esquerdo i=9, altura[9]=8
  🔴 Ponteiro direito j=10, altura[10]=4
     📐 Largura (j-i): 10-9 = 1
     📊 Altura mínima: min(8, 4) = 4
     🧮 Área calculada: 4 × 1 = 4
     🏆 Área máxima anterior: 500
     ❌ Área atual (4) não supera máxima (500)

  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-9 = 2
     📊 Altura mínima: min(8, 7) = 7
     🧮 Área calculada: 7 × 2 = 14
     🏆 Área máxima anterior: 500
     ❌ Área atual (14) não supera máxima (500)

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-9 = 3
     📊 Altura mínima: min(8, 3) = 3
     🧮 Área calculada: 3 × 3 = 9
     🏆 Área máxima anterior: 500
     ❌ Área atual (9) não supera máxima (500)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-9 = 4
     📊 Altura mínima: min(8, 6) = 6
     🧮 Área calculada: 6 × 4 = 24
     🏆 Área máxima anterior: 500
     ❌ Área atual (24) não supera máxima (500)

============================================================
🔵 Ponteiro esquerdo i=10, altura[10]=4
  🔴 Ponteiro direito j=11, altura[11]=7
     📐 Largura (j-i): 11-10 = 1
     📊 Altura mínima: min(4, 7) = 4
     🧮 Área calculada: 4 × 1 = 4
     🏆 Área máxima anterior: 500
     ❌ Área atual (4) não supera máxima (500)

  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-10 = 2
     📊 Altura mínima: min(4, 3) = 3
     🧮 Área calculada: 3 × 2 = 6
     🏆 Área máxima anterior: 500
     ❌ Área atual (6) não supera máxima (500)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-10 = 3
     📊 Altura mínima: min(4, 6) = 4
     🧮 Área calculada: 4 × 3 = 12
     🏆 Área máxima anterior: 500
     ❌ Área atual (12) não supera máxima (500)

============================================================
🔵 Ponteiro esquerdo i=11, altura[11]=7
  🔴 Ponteiro direito j=12, altura[12]=3
     📐 Largura (j-i): 12-11 = 1
     📊 Altura mínima: min(7, 3) = 3
     🧮 Área calculada: 3 × 1 = 3
     🏆 Área máxima anterior: 500
     ❌ Área atual (3) não supera máxima (500)

  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-11 = 2
     📊 Altura mínima: min(7, 6) = 6
     🧮 Área calculada: 6 × 2 = 12
     🏆 Área máxima anterior: 500
     ❌ Área atual (12) não supera máxima (500)

============================================================
🔵 Ponteiro esquerdo i=12, altura[12]=3
  🔴 Ponteiro direito j=13, altura[13]=6
     📐 Largura (j-i): 13-12 = 1
     📊 Altura mínima: min(3, 6) = 3
     🧮 Área calculada: 3 × 1 = 3
     🏆 Área máxima anterior: 500
     ❌ Área atual (3) não supera máxima (500)

============================================================
🔵 Ponteiro esquerdo i=13, altura[13]=6
============================================================
🎯 RESULTADO FINAL: 500
"""
