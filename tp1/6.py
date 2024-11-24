# 6. Imagine que você tem um tabuleiro de xadrez e coloca um único grão de arroz em um quadrado. No segundo quadrado, você coloca 2 grãos de arroz, já que isso é o dobro da quantidade de arroz no quadrado anterior. No terceiro quadrado, você coloca 4 grãos. No quarto quadrado, você coloca 8 grãos, e no quinto quadrado, você coloca 16 grãos, e assim por diante.
# a. Escreva a função em python que calcula em qual quadrado do tabuleiro você precisará colocar uma determinada quantidade de grãos de arroz. Por exemplo, para 16 grãos, a função retornará 5, já que você colocará os 16 grãos no quinto quadrado.
# b. Use a Notação Big O para descrever a complexidade de tempo da função que você acabou de criar.

import math

def find_square_number(grains):
    """
    Calculate the square number on the chessboard where a given amount of grains will be placed.

    Parameters:
    grains (int): The number of grains of rice.

    Returns:
    int: The square number on the chessboard.
    """
    # Calculate the square number using the formula derived from the geometric series
    n = math.ceil(math.log2(grains + 1))
    return n

# Example 1:
grains = 16
square_number = find_square_number(grains)
print(f"For {grains} grains, you need to place them on square {square_number}.")
# Output: For 16 grains, you need to place them on square 5.

# Example 2:
grains = 1000
square_number = find_square_number(grains)
print(f"For {grains} grains, you need to place them on square {square_number}.")
# Output: For 1000 grains, you need to place them on square 10.

# Complexidade de Tempo: O(1) (Tempo Constante)

# Explicação:

# Operações Realizadas:

# Adição: 
# grains + 1
# Logaritmo: 
# log₂(grains + 1)
# Função Teto (Ceiling): 
# ⌈⋅⌉
# Características das Operações:

# Operações Aritméticas (Adição): Executam em tempo constante.
# Funções Matemáticas (Logaritmo e Teto): Funções matemáticas padrão que executam em tempo constante para números de precisão fixa.
# Independência do Tamanho da Entrada:

# O tempo de execução não depende do valor de grains.
# Se grains for 16 ou 1.000.000, o número de operações permanece o mesmo.
# Conclusão:

# Como a função realiza um número fixo de passos independentemente do tamanho da entrada, sua complexidade de tempo é O(1).
