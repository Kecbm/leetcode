# 🥷🏾 SOLUTION

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = s
        for letter in string.punctuation:
            # Retirando pontuação, espaços e convertendo para letra minusculas
            cleaned_string = cleaned_string.replace(letter, '').replace(' ', '').lower()

        # Invertendo a string
        reversed_string = cleaned_string[::-1]

        # print(f"Cleaned: {cleaned_string}")
        # print(f"Reversed: {reversed_string}")

        return reversed_string == cleaned_string
    
solution = Solution()
result = solution.isPalindrome("Was it a car or a cat I saw?")
# print(f"Result: {result}")

"""
Cleaned: wasitacaroracatisaw
Reversed: wasitacaroracatisaw
Result: True
"""
