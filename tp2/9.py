def sort_list(numbers):
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.
    
    Parameters:
        numbers (list): A list of integers to be sorted.
        
    Returns:
        list: The sorted list in ascending order.
    """
    n = len(numbers)
    # Perform the sorting using the bubble sort algorithm.
    for i in range(n - 1):
        # Traverse the list up to the unsorted section.
        for j in range(n - 1 - i):
            # Compare adjacent elements and swap if needed.
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# Example usage
unsorted_list = [34, 2, 23, 12, 45, 10]
sorted_list = sort_list(unsorted_list)
print(sorted_list)  # Output: [2, 10, 12, 23, 34, 45]

# Explicação:
# Bubble Sort:
#
# O algoritmo percorre repetidamente a lista, compara elementos adjacentes e os troca se estiverem na ordem errada.
# Após cada passagem, o maior elemento não ordenado "sobe" para sua posição correta.
#
# Laço Externo: Controla o número de passagens (n-1 passagens para n elementos).
#
# Laço Interno: Itera pela seção não ordenada, trocando elementos adjacentes, se necessário.
#
# Troca: Realizada usando a atribuição múltipla do Python: numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j].
#
# Esta implementação evita o uso de funções prontas de ordenação e fornece um método simples e passo a passo para ordenar.
