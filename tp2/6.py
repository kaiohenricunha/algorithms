def count_odd_orders(order_stack):
    """
    Counts the number of orders with odd identification numbers in the order stack.

    Parameters:
    order_stack (list): The stack of order IDs, with the top of the stack at the end of the list.

    Returns:
    int: The number of orders with odd identification numbers.
    """
    count = 0
    temp_stack = []

    # Process the stack and move elements to temp_stack
    while order_stack:
        # Pop the top element from the order_stack
        order_id = order_stack.pop()

        # Check if the order ID is odd
        if order_id % 2 == 1:
            count += 1

        # Push the order ID onto the temp_stack to preserve order
        temp_stack.append(order_id)

    # Restore the original stack by moving elements back from temp_stack
    while temp_stack:
        order_stack.append(temp_stack.pop())

    # At this point, order_stack is restored to its original state
    return count

# Usage Example:

# Create a stack of order IDs (the end of the list represents the top of the stack)
order_stack = [1002, 1003, 1004, 1005, 1006, 1007]  # 1007 is on top

# Display the original stack
print("Original Order Stack (Top to Bottom):", order_stack[::-1])  # Reversed for clarity

# Get the number of orders with odd IDs
odd_order_count = count_odd_orders(order_stack)

# Display the result
print("Number of orders with odd IDs:", odd_order_count)  # Output: 3

# Verify that the order stack is unchanged
print("Order Stack After Counting (Top to Bottom):", order_stack[::-1])  # Reversed for clarity

# Output:
# Original Order Stack (Top to Bottom): [1007, 1006, 1005, 1004, 1003, 1002]
# Number of orders with odd IDs: 3
# Order Stack After Counting (Top to Bottom): [1007, 1006, 1005, 1004, 1003, 1002]

# Justificativa:

# Explicação da Função:
# - A função 'count_odd_orders' conta o número de pedidos com IDs ímpares sem modificar a pilha original.
# - Ela utiliza uma pilha auxiliar 'temp_stack' para armazenar temporariamente os elementos enquanto os processa.
# - Movendo os elementos para 'temp_stack', podemos fazer pop de 'order_stack' e, posteriormente, restaurá-la ao estado original.

# Etapas do Algoritmo:
# 1. Inicialize 'count' como 0 e 'temp_stack' como uma lista vazia.
# 2. Enquanto 'order_stack' não estiver vazia:
#    - Faça pop do ID do pedido no topo de 'order_stack'.
#    - Se o ID do pedido for ímpar (order_id % 2 == 1), incremente 'count'.
#    - Insira o ID do pedido em 'temp_stack' para preservar a ordem.
# 3. Após processar todos os elementos, 'order_stack' estará vazia e 'temp_stack' conterá todos os elementos.
# 4. Restaure 'order_stack' fazendo pop de 'temp_stack' e inserindo os elementos de volta em 'order_stack'.
# 5. Retorne o valor de 'count' com o número de IDs ímpares.

# Complexidade de Tempo:
# - A função possui complexidade de tempo O(n), onde n é o número de pedidos na pilha.
# - Explicação:
#   - Percorremos a pilha duas vezes: uma para contar e transferir elementos para 'temp_stack', e outra para restaurar 'order_stack'.
#   - Cada operação dentro dos laços tem complexidade O(1), resultando em uma complexidade linear.

# Complexidade de Espaço:
# - A complexidade de espaço é O(n) devido ao uso de 'temp_stack' para armazenar os elementos.
# - Precisamos de espaço adicional proporcional ao número de elementos na pilha original.

# Importância de Restaurar a Pilha:
# - Restaurando 'order_stack' ao estado original, garantimos que a função seja não-destrutiva.
# - Isso é crucial em aplicações onde a integridade da estrutura de dados deve ser mantida após a análise.

# Tratamento de Casos Extremos:
# - Se a pilha estiver vazia, a função retorna corretamente 0.
# - A função funciona com qualquer ID inteiro, incluindo números negativos.

# Aplicação Prática:
# - Esta função permite à equipe identificar pedidos promocionais (com IDs ímpares) de forma eficiente.
# - Ela suporta análises adicionais sem interromper o sistema de processamento de pedidos.

# Observação:
# - A pilha é representada como uma lista, com o topo da pilha no final da lista.
# - A notação 'order_stack[::-1]' é usada para exibir a pilha do topo para a base de forma clara.
