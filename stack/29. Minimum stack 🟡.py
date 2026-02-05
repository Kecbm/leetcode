import json
from typing import List

class Solution:
    def minStack(self, commands: List) -> List:
        results = []
        stack = []  # pilha separada para armazenar os valores
        
        i = 0
        while i < len(commands):
            if commands[i] == "MinStack":
                results.append(None)
                i += 1
            
            elif commands[i] == "push":
                stack.append(commands[i + 1])
                results.append(None)
                # Considera o "push", adiciona o valor e pula para o próximo comando
                i += 2
            
            elif commands[i] == "getMin":
                results.append(min(stack))
                i += 1
            
            elif commands[i] == "pop":
                stack.pop()
                results.append(None)
                i += 1
            
            elif commands[i] == "top":
                results.append(stack[-1])
                i += 1
            
            else:
                i += 1
        
        return results

solution = Solution()
result = solution.minStack(["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"])
print(f"Result: {json.dumps(result)}")