# first solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = s.lower()
        t = t.lower()

        for letter in s:
            # Quando você faz palavra1.count(letra), o Python:
            # 1. Percorre cada caractere da string palavra1
            # 2. Compara cada caractere com 'letra'
            # 3. Incrementa um contador interno a cada match
            # 4. Retorna o total de ocorrências
            countS = s.count(letter)
            countT = t.count(letter)

            if countS != countT:
                return False
            
        return True
    