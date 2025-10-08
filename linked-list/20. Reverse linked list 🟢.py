from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(f"🔄 Iniciando reversão da linked list")
        # print(f"Head inicial: {head.val if head else 'None'}")
        # print("-" * 40)
        
        # Três ponteiros: anterior, atual e próximo
        prev = None
        current = head
        step = 1
        
        while current:
            # print(f"\n📍 Passo {step}:")
            # print(f"  prev: {prev.val if prev else 'None'}")
            # print(f"  current: {current.val}")
            # print(f"  current.next: {current.next.val if current.next else 'None'}")
            
            # Salva o próximo nó antes de perder a referência
            next_node = current.next
            # print(f"  next_node salvo: {next_node.val if next_node else 'None'}")
            
            # Reverte a ligação
            current.next = prev
            # print(f"  ✅ Ligação revertida: {current.val} -> {prev.val if prev else 'None'}")
            
            # Move os ponteiros para frente
            prev = current
            current = next_node
            # print(f"  📈 Ponteiros movidos: prev={prev.val}, current={current.val if current else 'None'}")
            
            step += 1
        
        # print(f"\n🏁 Reversão completa!")
        # print(f"Novo head: {prev.val if prev else 'None'}")
        
        # prev agora aponta para o novo head
        return prev
    
    @staticmethod
    def print_linked_list(head):
        values = []
        current = head
        
        while current:
            values.append(current.val)
            current = current.next
        
        return " -> ".join(map(str, values)) + " -> None"

# Criar a linked list: 0 -> 1 -> 2 -> 3 -> None
node0 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node0.next = node1
node1.next = node2
node2.next = node3

solution = Solution()
result = solution.reverseList(node0)
# print(f"Lista revertida: {Solution.print_linked_list(result)}")

"""
🔄 Iniciando reversão da linked list
Head inicial: 0
----------------------------------------

📍 Passo 1:
  prev: None
  current: 0
  current.next: 1
  next_node salvo: 1
  ✅ Ligação revertida: 0 -> None
  📈 Ponteiros movidos: prev=0, current=1

📍 Passo 2:
  prev: 0
  current: 1
  current.next: 2
  next_node salvo: 2
  ✅ Ligação revertida: 1 -> 0
  📈 Ponteiros movidos: prev=1, current=2

📍 Passo 3:
  prev: 1
  current: 2
  current.next: 3
  next_node salvo: 3
  ✅ Ligação revertida: 2 -> 1
  📈 Ponteiros movidos: prev=2, current=3

📍 Passo 4:
  prev: 2
  current: 3
  current.next: None
  next_node salvo: None
  ✅ Ligação revertida: 3 -> 2
  📈 Ponteiros movidos: prev=3, current=None

🏁 Reversão completa!
Novo head: 3
Lista revertida: 3 -> 2 -> 1 -> 0 -> None
"""
