# 9. Escreva uma função em Python que implemente o algoritmo Bubble Sort para ordenar
# uma lista de números em ordem crescente. 
# Em seguida, teste a função com diferentes listas de números e verifique se ela está ordenando corretamente.

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Track if any swaps happen; if not, the list is sorted
        swapped = False
        # Last i elements are already sorted, no need to check them
        for j in range(0, n - i - 1):
            # Compare and swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, break
        if not swapped:
            break

# Test case 1: Unsorted list
list1 = [64, 34, 25, 12, 22, 11, 90]
print("Original list1:", list1)
bubble_sort(list1)
print("Sorted list1:  ", list1)
print()

# Test case 2: Already sorted list
list2 = [1, 2, 3, 4, 5]
print("Original list2:", list2)
bubble_sort(list2)
print("Sorted list2:  ", list2)
print()

# Test case 3: Reverse sorted list
list3 = [5, 4, 3, 2, 1]
print("Original list3:", list3)
bubble_sort(list3)
print("Sorted list3:  ", list3)
print()

# Test case 4: List with duplicates
list4 = [3, 6, 8, 3, 5, 6, 2]
print("Original list4:", list4)
bubble_sort(list4)
print("Sorted list4:  ", list4)
print()

# Test case 5: List with negative numbers
list5 = [0, -1, 3, -5, 2, -4]
print("Original list5:", list5)
bubble_sort(list5)
print("Sorted list5:  ", list5)
print()

# Test case 6: Empty list
list6 = []
print("Original list6:", list6)
bubble_sort(list6)
print("Sorted list6:  ", list6)
print()

# Test case 7: List with one element
list7 = [42]
print("Original list7:", list7)
bubble_sort(list7)
print("Sorted list7:  ", list7)
