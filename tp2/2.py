def merge_sort(lst):
    # Base case: If the list is of length 0 or 1, it is already sorted
    if len(lst) > 1:
        # Divide Step: Find the midpoint and split the list into left and right halves
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        # Recursively sort both halves
        # This recursion divides the list log n times
        merge_sort(left_half)
        merge_sort(right_half)

        # Conquer Step: Merge the sorted halves back into a single list
        # Initialize pointers for left_half (i), right_half (j), and lst (k)
        i = j = k = 0

        # Merge elements from left_half and right_half in sorted order
        # This loop runs in O(n) time at each level of recursion
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from left_half (if any)
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half (if any)
        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

    # Justificativa da Complexidade de Tempo:
    # - A lista é dividida em metades recursivamente até que listas de tamanho 1 sejam obtidas.
    # - A etapa de divisão leva O(log n) de tempo porque o tamanho da lista é reduzido à metade a cada vez.
    # - A etapa de mesclagem combina todas as listas divididas de volta em uma lista ordenada.
    # - A mesclagem em cada nível processa todos os n elementos, portanto, leva O(n) de tempo.
    # - Assim, a complexidade total de tempo é O(n log n).

# Usage Example:
data = [5, 2, 9, 1, 5, 6]
merge_sort(data)
print(data)  # Output: [1, 2, 5, 5, 6, 9]
