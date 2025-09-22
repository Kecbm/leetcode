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
# result = solution.encode(["neet","code","love","you"])
# print(f"Result: {result}")
"""
Result: neet#code#love#you
"""

solution = Solution()
# result = solution.decode("neet#code#love#you")
# print(f"Result: {result}")
"""
Result: ['neet', 'code', 'love', 'you']
"""


# 🏆 Solution

class Solution2:
    def encode2(self, strs: List[str]) -> str:
        # Se a lista estiver vazia, retorna string vazia
        if not strs:
            return ""
        
        # sizes: lista para guardar o tamanho de cada string
        # res: string resultado que será construída
        sizes, res = [], ""

        # Primeiro passo: calcular o tamanho de cada string
        for s in strs:
            sizes.append(len(s))

        # print(f"Sizes: {sizes}")

        # Segundo passo: adicionar os tamanhos seguidos de vírgula
        # Exemplo: se sizes = [4, 4, 4, 3], res ficará "4,4,4,3,"
        for sz in sizes:
            res += str(sz) # Converte número para string
            res += ',' # Adiciona vírgula como separador

        # Terceiro passo: adicionar '#' para marcar fim dos tamanhos
        res += '#'

        # print(f"Res 1: {res}")

        # Quarto passo: concatenar todas as strings originais
        # Exemplo: res ficará "4,4,4,3,#neetcodeloveyou"
        for s in strs:
            res += s

        return res

    def decode2(self, s: str) -> List[str]:
        # Se string estiver vazia, retorna lista vazia
        if not s:
            return []
        
        # sizes: lista dos tamanhos das strings originais
        # res: lista resultado com as strings decodificadas
        # i: índice para navegar pela string
        sizes, res, i = [], [], 0

        # Primeiro passo: extrair os tamanhos até encontrar '#'
        while s[i] != '#':
            cur = "" # String temporária para guardar o tamanho atual

            # Lê dígitos até encontrar vírgula
            while s[i] != ',':
                cur += s[i] # Constrói o número caractere por caractere
                i += 1

            # Converte string para int e adiciona na lista de tamanhos
            sizes.append(int(cur))
            i += 1 # Pula a vírgula

        # Pula o '#' para começar a ler as strings
        i += 1

        print(f"Sizes: {sizes}")

        # Segundo passo: extrair cada string usando os tamanhos
        for sz in sizes:
            # Usa slice para pegar exatamente 'sz' caracteres
            # Exemplo: se sz=4, pega s[i:i+4]
            res.append(s[i:i + sz])
            i += sz # Move índice para próxima string
            print(f"Res 1: {res}")
        return res

solution2 = Solution2()
# result = solution2.encode2(["Design","is","my","passion"])
# print(f"Result: {result}")
"""
Sizes: [6, 2, 2, 7]
Res 1: 6,2,2,7,#
Result: 6,2,2,7,#Designismypassion
"""

solution2 = Solution2()
result = solution2.decode2("6,2,2,7,#Designismypassion")
print(f"Result: {result}")
"""
Sizes: [6, 2, 2, 7]
Res 1: ['Design']
Res 1: ['Design', 'is']
Res 1: ['Design', 'is', 'my']
Res 1: ['Design', 'is', 'my', 'passion']
Result: ['Design', 'is', 'my', 'passion']
"""
