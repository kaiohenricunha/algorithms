def count_even_orders(order_stack):
    """
    Counts the number of orders with even identification numbers in the order stack.

    Parameters:
    order_stack (list): The stack of order IDs, with the top of the stack at the end of the list.

    Returns:
    int: The number of orders with even identification numbers.
    """
    count = 0
    temp_stack = []

    # Process the stack and move elements to temp_stack
    while order_stack:
        # Pop the top element from the order_stack
        order_id = order_stack.pop()

        # Check if the order ID is even
        if order_id % 2 == 0:
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

# Get the number of orders with even IDs
even_order_count = count_even_orders(order_stack)

# Display the result
print("Number of orders with even IDs:", even_order_count)  # Output: 3

# Verify that the order stack is unchanged
print("Order Stack After Counting (Top to Bottom):", order_stack[::-1])  # Reversed for clarity)

# Output:
# Original Order Stack (Top to Bottom): [1007, 1006, 1005, 1004, 1003, 1002]
# Number of orders with even IDs: 3
# Order Stack After Counting (Top to Bottom): [1007, 1006, 1005, 1004, 1003, 1002]

# Justificativa:

# Função 1 (count_even_orders):

# Complexidade de Tempo: O(n)
# - A função percorre a pilha duas vezes: uma para contar e transferir os elementos para 'temp_stack',
#   e outra para restaurar 'order_stack' a partir de 'temp_stack'.
# - Cada operação dentro dos laços (pop, append, verificação de módulo) tem tempo constante.
# - Portanto, a complexidade total de tempo é linear, O(n), onde n é o número de pedidos.

# Complexidade de Espaço: O(n)
# - Uma pilha auxiliar 'temp_stack' é usada para armazenar temporariamente os pedidos.
# - No pior caso, 'temp_stack' pode conter todos os 'n' elementos de 'order_stack'.
# - Assim, a complexidade de espaço é proporcional ao tamanho da pilha de entrada, O(n).

# Explicação da Função:
# - A função 'count_even_orders' conta de forma eficiente o número de pedidos com IDs pares
#   sem alterar a pilha original.
# - Ela utiliza uma pilha temporária 'temp_stack' para armazenar os elementos enquanto os processa.
# - Após contar, a pilha original 'order_stack' é restaurada movendo os elementos de volta de 'temp_stack'.

# Etapas do Algoritmo:
# 1. Inicialize 'count' como 0 e 'temp_stack' como uma lista vazia.
# 2. Enquanto 'order_stack' não estiver vazia:
#    - Faça pop do ID do pedido no topo de 'order_stack'.
#    - Verifique se o ID do pedido é par usando 'order_id % 2 == 0'.
#    - Se for par, incremente 'count'.
#    - Insira o ID do pedido em 'temp_stack' para preservar a ordem original.
# 3. Após processar todos os elementos, 'order_stack' estará vazia e 'temp_stack' conterá todos os elementos.
# 4. Restaure 'order_stack' fazendo pop de 'temp_stack' e inserindo os elementos de volta em 'order_stack'.
# 5. Retorne o valor de 'count' com o número de IDs pares.

# Tratamento de Casos Extremos:
# - Se a pilha estiver vazia, a função retorna corretamente 0, indicando que não há pedidos pares.
# - A função funciona com qualquer ID inteiro, incluindo números negativos.

# Aplicação Prática:
# - Esta função permite que a equipe identifique pedidos com IDs pares, que podem ser relevantes para promoções ou análises específicas.
# - Restaurando a pilha original, a integridade do sistema de gerenciamento de pedidos é mantida, garantindo que nenhum dado seja perdido ou alterado durante o processo de contagem.

# Importância de Restaurar a Pilha:
# - Preservar a ordem original da pilha é crucial para a continuidade do processamento dos pedidos.
# - Esta abordagem não-destrutiva garante que a operação de contagem não interfira em outras funcionalidades que dependem do estado da pilha.

# Comparação com a Contagem de Pedidos Ímpares:
# - Semelhante à contagem de pedidos ímpares, a contagem de pedidos pares segue a mesma lógica e eficiência.
# - Ambas as operações possuem complexidade linear em tempo e espaço, tornando-as adequadas para grandes conjuntos de dados com milhões de pedidos.
