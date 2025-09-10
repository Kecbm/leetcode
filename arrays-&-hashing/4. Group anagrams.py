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


# 🥷🏾 SECOND SOLUTION
    # Memory: 52.1 MB
    # Runtime: 0.888 seconds
class Solution2:
    def groupAnagrams(self, strs):
        from collections import defaultdict

        groups = defaultdict(list)

        for word in strs:
            # Ordenar as letras da palavra ("chave")
            key = ''.join(sorted(word))
            print(f"word: {word}, key: {key}")

            groups[key].append(word)
            print(f"groups[{key}]: {groups[key]}")

        # Retornar apenas os valores (grupos) do dicionário
        return list(groups.values())
    
solution = Solution2()
result = solution.groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(f"Result: {result}")

"""
    word: act, key: act
    groups[act]: ['act']
    word: pots, key: opst
    groups[opst]: ['pots']
    word: tops, key: opst
    groups[opst]: ['pots', 'tops']
    word: cat, key: act
    groups[act]: ['act', 'cat']
    word: stop, key: opst
    groups[opst]: ['pots', 'tops', 'stop']
    word: hat, key: aht
    groups[aht]: ['hat']
    Result: [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]
"""
