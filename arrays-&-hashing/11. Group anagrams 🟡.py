from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            # Ordena as letras de cada palavra
            # Para ser a key do dict
            key = ''.join(sorted(str))
            # print(f"Key: {key}")
            
            # Adiciona a palavra na lista do dict
            # Se a key não existir, cria uma lista vazia
            dict[key] = dict.get(key, [])
            # Adiciona a palavra na lista do dict
            dict[key].append(str)
            # print(f"Dict: {dict}")
            
        # Retorna apenas os valores do dict    
        return list(dict.values())
    
solution = Solution()
result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# print(f"Result: {result}")

"""
Key: aet
Dict: {'aet': ['eat']}
Key: aet
Dict: {'aet': ['eat', 'tea']}
Key: ant
Dict: {'aet': ['eat', 'tea'], 'ant': ['tan']}
Key: aet
Dict: {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan']}
Key: ant
Dict: {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat']}
Key: abt
Dict: {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
Result: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""
