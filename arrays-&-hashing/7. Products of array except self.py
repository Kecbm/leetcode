# 🥷🏾 SOLUTION

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Para cada posição i, caucular o produto de todos os elementos exceto o elemento na posição i
        result = []

        for i in range(len(nums)):
            product = 1

            # Multiplicar todos os elementos exceto o da posição i
            for j in range(len(nums)):
                # Pula o elemento da posição atual
                if i != j:
                    product *= nums[j]
                    # print(f"i={i}, j={j}, nums[{j}]={nums[j]}, product={product}")
                
            result.append(product)
            # print(f"Position {i}: product = {product}")
        
        return result
    
solution = Solution()
result = solution.productExceptSelf([1,2,4,6])
print(f"Result: {result}")

"""
    i=0, j=1, nums[1]=2, product=2
    i=0, j=2, nums[2]=4, product=8
    i=0, j=3, nums[3]=6, product=48
    Position 0: product = 48
    i=1, j=0, nums[0]=1, product=1
    i=1, j=2, nums[2]=4, product=4
    i=1, j=3, nums[3]=6, product=24
    Position 1: product = 24
    i=2, j=0, nums[0]=1, product=1
    i=2, j=1, nums[1]=2, product=2
    i=2, j=3, nums[3]=6, product=12
    Position 2: product = 12
    i=3, j=0, nums[0]=1, product=1
    i=3, j=1, nums[1]=2, product=2
    i=3, j=2, nums[2]=4, product=8
    Position 3: product = 8
    Result: [48, 24, 12, 8]
"""
