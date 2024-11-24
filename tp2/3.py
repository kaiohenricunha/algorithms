# Function 1: Brute-force approach
def find_duplicates_brute_force(lst):
    duplicates = set()
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] == lst[j]:
                duplicates.add(lst[i])
    return list(duplicates)

# Function 2: Efficient approach using a hash table
def find_duplicates_hash_table(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Justificativa:

# Função 1 (find_duplicates_brute_force):
# - Complexidade de Tempo: O(n^2)
#   - A função utiliza um laço aninhado para comparar cada elemento com todos os outros.
#   - O laço externo executa 'n' vezes, e o laço interno executa até 'n-1' vezes.
#   - Isso resulta em aproximadamente n(n-1)/2 comparações.
# - Complexidade de Espaço: O(d)
#   - O conjunto 'duplicates' armazena os elementos duplicados, onde 'd' é o número de duplicados encontrados.
# - Este método de força bruta não é eficiente para listas grandes com milhões de elementos devido à sua complexidade de tempo quadrática.

# Função 2 (find_duplicates_hash_table):
# - Complexidade de Tempo: O(n)
#   - A função itera sobre a lista uma única vez.
#   - As operações em conjuntos (add, in) têm, em média, complexidade de tempo O(1).
# - Complexidade de Espaço: O(n)
#   - O conjunto 'seen' pode armazenar até 'n' elementos se todos forem únicos.
#   - O conjunto 'duplicates' armazena os elementos duplicados.
# - Usando uma tabela hash (conjunto), reduzimos a complexidade de tempo de O(n^2) para O(n), tornando o método eficiente para grandes volumes de dados.
