def sort_stack(stack):
    # Create a temporary stack to hold sorted elements
    temp_stack = []
    
    # Process each element in the original stack
    while stack:
        # Pop the top element from the original stack
        temp = stack.pop()
        
        # Move elements from temp_stack back to the original stack
        # if they are greater than the current element 'temp'
        while temp_stack and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())
        
        # Push the current element 'temp' onto temp_stack
        temp_stack.append(temp)
    
    # Transfer the sorted elements back to the original stack
    while temp_stack:
        stack.append(temp_stack.pop())
    
    # At this point, the original stack is sorted in ascending order
    # with the smallest elements at the bottom and largest at the top

# Usage Example:
# Create a stack of grades (the end of the list is the top of the stack)
grades_stack = [85, 70, 95, 60, 90, 75]
print("Original Stack (Top to Bottom):", grades_stack[::-1])  # Reverse for clarity

# Sort the stack
sort_stack(grades_stack)

# Display the sorted stack
print("Sorted Stack (Top to Bottom):", grades_stack[::-1])  # Reverse for clarity

# Output:
# Original Stack (Top to Bottom): [75, 90, 60, 95, 70, 85]
# Sorted Stack (Top to Bottom): [60, 70, 75, 85, 90, 95]

# Justification:

# Algorithm Explanation:
# - Objective: Sort the stack so that grades are in ascending order from bottom to top.
# - Method:
#   - Use an auxiliary stack (temp_stack) to hold elements in sorted order.
#   - For each element (temp) popped from the original stack:
#     - Compare it with the elements in temp_stack.
#     - Move any elements greater than temp back to the original stack.
#     - Push temp onto temp_stack.
#   - Once all elements are processed, transfer the sorted elements back to the original stack.

# Why It Works:
# - The algorithm maintains the sorted order in temp_stack at all times.
# - By moving larger elements back to the original stack, we ensure that each element is placed in its correct position relative to the elements processed so far.
# - After all elements are transferred back, the original stack contains the elements in ascending order.

# Time Complexity:
# - Worst-Case Time Complexity: O(n^2), where n is the number of elements in the stack.
#   - Explanation:
#     - For each element in the original stack, we may have to move all elements from temp_stack back to the original stack.
#     - This nested operation results in a quadratic number of moves in the worst case.

# Space Complexity:
# - Space Complexity: O(n)
#   - Explanation:
#     - We use an additional stack (temp_stack) that can hold up to n elements.
#     - The space used is proportional to the size of the input stack.

# Alternative Efficient Approach:

# If performance is critical and using additional data structures is acceptable, we can achieve better time complexity by converting the stack to a list:

def sort_stack_efficient(stack):
    # Transfer elements from the stack to a list
    temp_list = []
    while stack:
        temp_list.append(stack.pop())
    
    # Sort the list in ascending order
    temp_list.sort()
    
    # Push the sorted elements back onto the stack
    for item in temp_list:
        stack.append(item)
    
    # The stack is now sorted in ascending order

# Usage Example:
# Create a stack of grades
grades_stack = [85, 70, 95, 60, 90, 75]
print("Original Stack (Top to Bottom):", grades_stack[::-1])  # Reverse for clarity

# Sort the stack efficiently
sort_stack_efficient(grades_stack)

# Display the sorted stack
print("Sorted Stack (Top to Bottom):", grades_stack[::-1])  # Reverse for clarity

# Output:
# Original Stack (Top to Bottom): [75, 90, 60, 95, 70, 85]
# Sorted Stack (Top to Bottom): [60, 70, 75, 85, 90, 95]

# Justificativa:

# Complexidade de Tempo:
# - Complexidade de Tempo: O(n log n)
#   - Explicação:
#     - Ordenar a lista com temp_list.sort() leva O(n log n) de tempo.
#     - Transferir elementos entre a pilha e a lista leva O(n) de tempo.
#     - No geral, o termo dominante é O(n log n).

# Complexidade de Espaço:
# - Complexidade de Espaço: O(n)
#   - Explicação:
#     - Usamos uma lista (temp_list) que pode conter até n elementos.
#     - O espaço utilizado é proporcional ao tamanho da pilha de entrada.

# Conclusão:
# - A função 'sort_stack' ordena a pilha usando apenas operações de pilha, respeitando as restrições de uso de pilhas.
# - Ela possui uma complexidade de tempo de O(n^2), o que pode não ser eficiente para pilhas grandes.
# - A função 'sort_stack_efficient' melhora a complexidade de tempo para O(n log n) ao usar uma lista e a ordenação embutida.
# - Escolha o método que melhor se adapta aos seus requisitos em relação ao desempenho e às restrições sobre estruturas de dados.
