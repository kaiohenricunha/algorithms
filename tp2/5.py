def task_on_top(task_stack):
    """
    Returns the element on top of the stack without removing it.

    Parameters:
    task_stack (list): The stack of tasks, with the top of the stack at the end of the list.

    Returns:
    The task at the top of the stack, or None if the stack is empty.
    """
    # Time Complexity: O(1)
    # - Accessing the last element of a list is a constant-time operation.

    # Check if the stack is empty
    if not task_stack:
        # Return None or raise an exception if preferred
        return None

    # Return the top element without removing it
    return task_stack[-1]

# Usage Example:

# Create a stack of tasks (the end of the list represents the top of the stack)
tasks = ["Design UI", "Implement Login", "Write Tests"]  # 'Write Tests' is on top

# Get the task on top
top_task = task_on_top(tasks)

# Display the top task
print("The task on top is:", top_task)  # Output: The task on top is: Write Tests

# Verify that the task is not removed from the stack
print("Current Task Stack:", tasks)
# Output: Current Task Stack: ['Design UI', 'Implement Login', 'Write Tests']

# Justificativa:

# Explicação da Função:
# - A função 'task_on_top' oferece uma maneira de acessar a tarefa mais recente sem modificar a pilha.
# - Ela verifica se a pilha está vazia para evitar erros ao acessar o último elemento.
# - Usando 'task_stack[-1]', recuperamos o elemento no topo da pilha de forma eficiente.

# Complexidade de Tempo:
# - A operação possui complexidade de tempo O(1), pois acessar um elemento pelo índice em uma lista é uma operação de tempo constante.
# - Essa eficiência é importante para uma aplicação de gerenciamento de tarefas, onde é necessário acesso rápido à próxima tarefa.

# Complexidade de Espaço:
# - A complexidade de espaço é O(1), já que nenhum espaço adicional é usado em relação ao tamanho da entrada.

# Tratamento de Casos Extremos:
# - Se a pilha estiver vazia, a função retorna None.
# - Alternativamente, pode-se lançar uma exceção (por exemplo, IndexError) para indicar que a pilha está vazia.

# Aplicação Prática:
# - Esta função permite que os usuários visualizem a próxima tarefa a ser concluída sem alterar a pilha de tarefas.
# - Ela auxilia no gerenciamento de tarefas ao fornecer uma visão rápida sobre as tarefas pendentes.
