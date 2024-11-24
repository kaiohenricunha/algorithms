# 7. A seguinte função aceita um array de strings e retorna um novo array que contém apenas as strings 
# que começam com o caractere "a". Use a Notação Big O para descrever a complexidade de tempo da função:

def selectAStrings(array):
    newArray = []

    for i in range(len(array)):
        if array[i].startswith("a"):
            newArray.append(array[i])

    return newArray

# Explicação:

# A função selectAStrings itera sobre cada elemento no array de entrada exatamente uma vez. 
# Para cada string, ela executa uma operação de tempo constante para verificar se começa com o caractere "a". 
# Portanto, a complexidade de tempo total é O(n), onde n é o número de elementos no array.

# Example input array
array = ["apple", "banana", "avocado", "cherry", "apricot", "blueberry", "almond"]

# Call the function
result = selectAStrings(array)

# Print the result
print(result)
# output: ['apple', 'avocado', 'apricot', 'almond']
