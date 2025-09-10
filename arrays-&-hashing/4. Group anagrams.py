# 🥷🏾 FIRST SOLUTION
    # Memory: 52.2 MB
    # Runtime: 0.814 seconds
class Solution:
    def groupAnagrams(self, strs):
        """
        1. Para cada palavra, ordenar suas letras (essa será a "chave" do dicionário)
        2. Palavras com a mesma chave são anagramas
        3. Usar um dicionário para agrupar
        """
        groups = {}

        for word in strs:
            # Ordenar as letras da palavra ("chave")
            key = ''.join(sorted(word))
            # print(f"word: {word}, key: {key}")

            # Se a chave já existe, adicionar a palavra ao grupo
            if key in groups:
                # print(f"exists group[{key}]: {groups[key]}")
                groups[key].append(word)
            # Se não existe, criar um novo grupo
            else:
                # print(f"create group: [{key}]")
                groups[key] = [word]

        # Retornar apenas os valores (grupos) do dicionário
        return list(groups.values())

solution = Solution()
result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# print(f"Result: {result}")

"""
    word: eat, key: aet
    create group: [aet]
    word: tea, key: aet
    exists group[aet]: ['eat']
    word: tan, key: ant
    create group: [ant]
    word: ate, key: aet
    exists group[aet]: ['eat', 'tea']
    word: nat, key: ant
    exists group[ant]: ['tan']
    word: bat, key: abt
    create group: [abt]
    Result: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""
