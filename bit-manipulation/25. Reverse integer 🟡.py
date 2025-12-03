class Solution:
    def reverse(self, x: int) -> int:
        x_string = str(x)
        # print(f"🔢 Input: {x} -> String: '{x_string}'")
        
        # Verificar se é negativo
        is_negative = x_string[0] == '-'
        # print(f"❓ É negativo? {is_negative}")
        
        # Se for negativo, remove o sinal
        if is_negative:
            x_string = x_string[1:]
            # print(f"➖ Removendo sinal: '{x_string}'")
        
        # Reverter a string
        reversed_string = x_string[::-1]
        # print(f"🔄 String revertida: '{reversed_string}'")
        
        # Converte para número
        result = int(reversed_string)
        # print(f"🔢 Convertido para número: {result}")
        
        # Se era negativo, multiplica por -1
        if is_negative:
            result = result * -1
            # print(f"➖ Aplicando sinal negativo: {result}")
        
        # Verificar se está dentro dos limites
        if result < -2**31 or result > 2**31 - 1:
            # print(f"⚠️  Overflow detectado! Retornando 0")
            return 0
        
        # print(f"✅ Resultado final: {result}")
        return result
    
solution = Solution()
result = solution.reverse(-1234)
# print(f"{result}")
"""
🔢 Input: -1234 -> String: '-1234'
❓ É negativo? True
➖ Removendo sinal: '1234'
🔄 String revertida: '4321'
🔢 Convertido para número: 4321
➖ Aplicando sinal negativo: -4321
✅ Resultado final: -4321
"""

# 🏆 Solution
# Brute Force

class Solution2:
    def reverse2(self, x: int) -> int:
        x_string = str(x)
        print(f"🔢 Input: {x} -> String: '{x_string}'")
        
        is_negative = x_string[0] == '-'
        print(f"❓ É negativo? {is_negative}")
        
        if is_negative:
            x_string = x_string[1:]
            print(f"➖ Removendo sinal: '{x_string}'")
        
        reversed_string = x_string[::-1]
        print(f"🔄 String revertida: '{reversed_string}'")
        
        result = int(reversed_string)
        print(f"🔢 Convertido para número: {result}")
        
        if is_negative:
            result = result * -1
            print(f"➖ Aplicando sinal negativo: {result}")
        
        if result < -2**31 or result > 2**31 - 1:
            print(f"⚠️  Overflow detectado! Retornando 0")
            return 0
        
        print(f"✅ Resultado final: {result}")
        return result
    
solution2 = Solution2()
result2 = solution2.reverse2(1234)
# print(f"{result2}")

"""
🔢 Input: 1234 -> String: '1234'
❓ É negativo? False
🔄 String revertida: '4321'
🔢 Convertido para número: 4321
✅ Resultado final: 4321
"""
