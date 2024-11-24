# Função 1: O(n)
# Justificativa:
# funcao1 contém um único laço de repetição (for) que itera n vezes. 
# Em cada iteração, é executada uma operação de tempo constante (print(i)).
# Portanto, a complexidade de tempo é proporcional a n, ou seja, O(n).
def funcao1(n):
    for i in range(n):
        print(i)

# Função 2: O(n²)
# Justificativa:
# funcao2 utiliza dois laços de repetição (for) aninhados, cada um iterando n vezes.
# O laço externo executa n vezes, e para cada iteração do laço externo, o laço interno também executa n vezes.
# Isso resulta em um total de n * n = n² iterações.
# Como cada iteração executa uma operação de tempo constante (print(i, j)), a complexidade total é O(n²).
def funcao2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# Função 3: O(2ⁿ)
# Justificativa:
# funcao3 é uma implementação recursiva da sequência de Fibonacci. 
# Para cada chamada com n > 1, são feitas duas chamadas recursivas: funcao3(n - 1) e funcao3(n - 2).
# Isso cria uma árvore de recursão binária onde o número de chamadas dobra a cada incremento de n.
# O número total de chamadas - e, portanto, a complexidade de tempo - cresce exponencialmente com n.
# Assim, a complexidade de tempo é O(2ⁿ).
def funcao3(n):
    if n <= 1:
        return n
    return funcao3(n - 1) + funcao3(n - 2)
