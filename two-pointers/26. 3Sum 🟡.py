from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            # range(start, stop, step)
            # start: onde começa (por default é 0)
            # stop: onde para (não inclui esse número)
            # step: o passo/incremento (por default é 1)
            for j in range(1, len(nums)):
                for k in range(2, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        return [nums[i], nums[j], nums[k]]

solution = Solution()
result = solution.threeSum([-1,0,1,2,-1,-4])
# print(f"Result: {result}")

"""
Result: [-1, 0, 1]
"""

class Solution2:
    def threeSum2(self, nums):
        print("=" * 60)
        print(f"📥 ENTRADA: {nums}")
        
        # Passo 1: Ordenar
        nums.sort()
        print(f"📊 ORDENADO: {nums}")
        print("=" * 60)
        
        resultado = []
        
        # Passo 2: Fixar o primeiro número
        for i in range(len(nums) - 2):
            print(f"\n🔵 ITERAÇÃO i={i}")
            print(f"   Número fixo: nums[{i}] = {nums[i]}")
            
            # Pular duplicatas do primeiro número
            if i > 0 and nums[i] == nums[i - 1]:
                print(f"   ⏭️  PULANDO duplicata: {nums[i]} (já processado)")
                continue
            
            # Passo 3: Two Pointers
            esquerda = i + 1
            direita = len(nums) - 1
            
            print(f"   Iniciando Two Pointers:")
            print(f"   esquerda={esquerda}, direita={direita}")
            print(f"   {nums}")
            print(f"   {' ' * (i * 4)}↑{' ' * ((esquerda - i - 1) * 4)}↑{' ' * ((direita - esquerda - 1) * 4)}↑")
            print(f"   {' ' * (i * 4)}i{' ' * ((esquerda - i - 1) * 4)}L{' ' * ((direita - esquerda - 1) * 4)}R")
            
            passo = 0
            while esquerda < direita:
                passo += 1
                soma = nums[i] + nums[esquerda] + nums[direita]
                
                print(f"\n   📍 Passo {passo}:")
                print(f"      nums[{i}]={nums[i]}, nums[{esquerda}]={nums[esquerda]}, nums[{direita}]={nums[direita]}")
                print(f"      Soma: {nums[i]} + {nums[esquerda]} + {nums[direita]} = {soma}")
                
                if soma == 0:
                    tripla = [nums[i], nums[esquerda], nums[direita]]
                    print(f"      ✅ ENCONTROU! {tripla}")
                    resultado.append(tripla)
                    
                    # Pular duplicatas da esquerda
                    while esquerda < direita and nums[esquerda] == nums[esquerda + 1]:
                        esquerda += 1
                        print(f"      ⏭️  Pulando duplicata esquerda: {nums[esquerda]}")
                    
                    # Pular duplicatas da direita
                    while esquerda < direita and nums[direita] == nums[direita - 1]:
                        direita -= 1
                        print(f"      ⏭️  Pulando duplicata direita: {nums[direita]}")
                    
                    esquerda += 1
                    direita -= 1
                    print(f"      ➡️  Movendo ambos: esquerda={esquerda}, direita={direita}")
                    
                elif soma < 0:
                    print(f"      ⬆️  Soma muito pequena ({soma} < 0)")
                    esquerda += 1
                    print(f"      ➡️  Movendo esquerda para: {esquerda}")
                    
                else:  # soma > 0
                    print(f"      ⬇️  Soma muito grande ({soma} > 0)")
                    direita -= 1
                    print(f"      ⬅️  Movendo direita para: {direita}")
        
        print("\n" + "=" * 60)
        print(f"🎯 RESULTADO FINAL: {resultado}")
        print("=" * 60)
        
        return resultado

solution2 = Solution2()
result2 = solution2.threeSum2([-1,0,1,2,-1,-4])

"""
============================================================
📥 ENTRADA: [-1, 0, 1, 2, -1, -4]
📊 ORDENADO: [-4, -1, -1, 0, 1, 2]
============================================================

🔵 ITERAÇÃO i=0
   Número fixo: nums[0] = -4
   Iniciando Two Pointers:
   esquerda=1, direita=5
   [-4, -1, -1, 0, 1, 2]
   ↑↑            ↑
   iL            R

   📍 Passo 1:
      nums[0]=-4, nums[1]=-1, nums[5]=2
      Soma: -4 + -1 + 2 = -3
      ⬆️  Soma muito pequena (-3 < 0)
      ➡️  Movendo esquerda para: 2

   📍 Passo 2:
      nums[0]=-4, nums[2]=-1, nums[5]=2
      Soma: -4 + -1 + 2 = -3
      ⬆️  Soma muito pequena (-3 < 0)
      ➡️  Movendo esquerda para: 3

   📍 Passo 3:
      nums[0]=-4, nums[3]=0, nums[5]=2
      Soma: -4 + 0 + 2 = -2
      ⬆️  Soma muito pequena (-2 < 0)
      ➡️  Movendo esquerda para: 4

   📍 Passo 4:
      nums[0]=-4, nums[4]=1, nums[5]=2
      Soma: -4 + 1 + 2 = -1
      ⬆️  Soma muito pequena (-1 < 0)
      ➡️  Movendo esquerda para: 5

🔵 ITERAÇÃO i=1
   Número fixo: nums[1] = -1
   Iniciando Two Pointers:
   esquerda=2, direita=5
   [-4, -1, -1, 0, 1, 2]
       ↑↑        ↑
       iL        R

   📍 Passo 1:
      nums[1]=-1, nums[2]=-1, nums[5]=2
      Soma: -1 + -1 + 2 = 0
      ✅ ENCONTROU! [-1, -1, 2]
      ➡️  Movendo ambos: esquerda=3, direita=4

   📍 Passo 2:
      nums[1]=-1, nums[3]=0, nums[4]=1
      Soma: -1 + 0 + 1 = 0
      ✅ ENCONTROU! [-1, 0, 1]
      ➡️  Movendo ambos: esquerda=4, direita=3

🔵 ITERAÇÃO i=2
   Número fixo: nums[2] = -1
   ⏭️  PULANDO duplicata: -1 (já processado)

🔵 ITERAÇÃO i=3
   Número fixo: nums[3] = 0
   Iniciando Two Pointers:
   esquerda=4, direita=5
   [-4, -1, -1, 0, 1, 2]
               ↑↑↑
               iLR

   📍 Passo 1:
      nums[3]=0, nums[4]=1, nums[5]=2
      Soma: 0 + 1 + 2 = 3
      ⬇️  Soma muito grande (3 > 0)
      ⬅️  Movendo direita para: 4

============================================================
🎯 RESULTADO FINAL: [[-1, -1, 2], [-1, 0, 1]]
============================================================
"""