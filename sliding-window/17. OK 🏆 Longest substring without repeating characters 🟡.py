class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_letters = ''.join(set(s))
        # print(f"Unique: {unique_letters}")

        return len(unique_letters)
    
solution = Solution()
result = solution.lengthOfLongestSubstring("zxyzxyz")
# print(f"Result: {result}")
"""
Unique: yzx
Result: 3
"""

# 🏆 Solution

class Solution2:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        res = 0
        # print(f"String analisada: '{s}'")
        # print("-" * 40)
        
        for i in range(len(s)):
            # print(f"\n🔍 Iniciando substring na posição {i} ('{s[i]}')")
            charSet = set()
            
            for j in range(i, len(s)):
                if s[j] in charSet:
                    # print(f"  ❌ Caractere '{s[j]}' já existe no set {charSet}")
                    # print(f"  🛑 Parando. Substring atual: '{s[i:j]}'")
                    break
                
                charSet.add(s[j])
                # print(f"  ✅ Adicionado '{s[j]}' → set: {charSet}")
                # print(f"  📏 Substring atual: '{s[i:j+1]}' (tamanho: {len(charSet)})")
            
            # old_res = res
            res = max(res, len(charSet))
            # print(f"  🏆 Resultado: {old_res} → {res}")
        return res

solution2 = Solution2()
result = solution2.lengthOfLongestSubstring2("pwwkew")
# print(f"Result: {result}")
"""
String analisada: 'pwwkew'
----------------------------------------
🔍 Iniciando substring na posição 0 ('p')
  ✅ Adicionado 'p' → set: {'p'}
  📏 Substring atual: 'p' (tamanho: 1)
  ✅ Adicionado 'w' → set: {'p', 'w'}
  📏 Substring atual: 'pw' (tamanho: 2)
  ❌ Caractere 'w' já existe no set {'p', 'w'}
  🛑 Parando. Substring atual: 'pw'
  🏆 Resultado: 0 → 2

🔍 Iniciando substring na posição 1 ('w')
  ✅ Adicionado 'w' → set: {'w'}
  📏 Substring atual: 'w' (tamanho: 1)
  ❌ Caractere 'w' já existe no set {'w'}
  🛑 Parando. Substring atual: 'w'
  🏆 Resultado: 2 → 2

🔍 Iniciando substring na posição 2 ('w')
  ✅ Adicionado 'w' → set: {'w'}
  📏 Substring atual: 'w' (tamanho: 1)
  ✅ Adicionado 'k' → set: {'w', 'k'}
  📏 Substring atual: 'wk' (tamanho: 2)
  ✅ Adicionado 'e' → set: {'e', 'w', 'k'}
  📏 Substring atual: 'wke' (tamanho: 3)
  ❌ Caractere 'w' já existe no set {'e', 'w', 'k'}
  🛑 Parando. Substring atual: 'wke'
  🏆 Resultado: 2 → 3

🔍 Iniciando substring na posição 3 ('k')
  ✅ Adicionado 'k' → set: {'k'}
  📏 Substring atual: 'k' (tamanho: 1)
  ✅ Adicionado 'e' → set: {'e', 'k'}
  📏 Substring atual: 'ke' (tamanho: 2)
  ✅ Adicionado 'w' → set: {'e', 'w', 'k'}
  📏 Substring atual: 'kew' (tamanho: 3)
  🏆 Resultado: 3 → 3

🔍 Iniciando substring na posição 4 ('e')
  ✅ Adicionado 'e' → set: {'e'}
  📏 Substring atual: 'e' (tamanho: 1)
  ✅ Adicionado 'w' → set: {'e', 'w'}
  📏 Substring atual: 'ew' (tamanho: 2)
  🏆 Resultado: 3 → 3

🔍 Iniciando substring na posição 5 ('w')
  ✅ Adicionado 'w' → set: {'w'}
  📏 Substring atual: 'w' (tamanho: 1)
  🏆 Resultado: 3 → 3
Result: 3
"""
