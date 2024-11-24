# 8. No algoritmo Bubble Sort:

# def bubbleSort(self):                           # Ordenar comparando valores adjs.
#       for last in range(self.__nItems-1, 0, -1):  # e subir
#          for inner in range(last):                # o loop interno vai até o último
#             if self.__a[inner] > self.__a[inner+1]:  # Se o item for menor
#                self.swap(inner, inner+1)          # que o item adjacente, trocar
# O índice interno sempre vai da esquerda para a direita, encontrando o maior item e levando-o para a direita. 
# Modifique o método bubbleSort() para que ele seja bidirecional. 
# Isso significa que o índice interno primeiro levará o maior item da esquerda para a direita como antes,
# mas quando alcançar o último, ele se inverterá e levará o menor item da direita para a esquerda.
# Você precisará de dois índices externos, um à direita (o antigo último) e outro à esquerda.

class Array:
    def __init__(self, array):
        self.__a = array  # The array to be sorted
        self.__nItems = len(array)  # Number of items in the array

    def swap(self, index1, index2):
        # Swap the elements at the given indices
        self.__a[index1], self.__a[index2] = self.__a[index2], self.__a[index1]

    def bubbleSort(self):
        # Bidirectional Bubble Sort (Cocktail Shaker Sort)
        left = 0
        right = self.__nItems - 1
        while left < right:
            # Pass from left to right
            for i in range(left, right):
                if self.__a[i] > self.__a[i + 1]:
                    self.swap(i, i + 1)
            right -= 1  # Reduce the right boundary

            # Pass from right to left
            for i in range(right, left, -1):
                if self.__a[i - 1] > self.__a[i]:
                    self.swap(i - 1, i)
            left += 1  # Increase the left boundary

    def display(self):
        print(self.__a)

# Example usage:
if __name__ == "__main__":
    # Create an instance of Array with unsorted data
    arr = Array([5, 3, 8, 4, 2, 7, 1, 6])

    print("Before sorting:")
    arr.display()

    # Perform bidirectional bubble sort
    arr.bubbleSort()

    print("After sorting:")
    arr.display()

