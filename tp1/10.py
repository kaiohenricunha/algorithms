# 10. Modifique a função bubbleSort() para que ela ordene uma lista de strings em ordem alfabética.
# Em seguida, teste a função com diferentes listas de strings e verifique se ela está ordenando corretamente.

def bubble_sort_strings(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Track if any swaps happen; if not, the list is sorted
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent strings and swap if they are in the wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps occurred, the list is sorted
        if not swapped:
            break

# Test case 1: Unsorted list of lowercase strings
list1 = ["banana", "apple", "cherry", "date"]
print("Original list1:", list1)
bubble_sort_strings(list1)
print("Sorted list1:  ", list1)
print()

# Test case 2: List with mixed case strings
list2 = ["Banana", "apple", "Cherry", "date"]
print("Original list2:", list2)
bubble_sort_strings(list2)
print("Sorted list2:  ", list2)
print()

# Test case 3: List with duplicate strings
list3 = ["apple", "banana", "apple", "cherry", "banana"]
print("Original list3:", list3)
bubble_sort_strings(list3)
print("Sorted list3:  ", list3)
print()

# Test case 4: List with empty strings
list4 = ["banana", "", "apple", "", "cherry"]
print("Original list4:", list4)
bubble_sort_strings(list4)
print("Sorted list4:  ", list4)
print()

# Test case 5: List with numbers as strings
list5 = ["10", "2", "1", "20", "11"]
print("Original list5:", list5)
bubble_sort_strings(list5)
print("Sorted list5:  ", list5)
print()

# Test case 6: List with special characters
list6 = ["apple!", "apple", "apple?", "Apple", "apple."]
print("Original list6:", list6)
bubble_sort_strings(list6)
print("Sorted list6:  ", list6)
print()

# Test case 7: Already sorted list
list7 = ["apple", "banana", "cherry", "date"]
print("Original list7:", list7)
bubble_sort_strings(list7)
print("Sorted list7:  ", list7)
print()

# Test case 8: Reverse sorted list
list8 = ["date", "cherry", "banana", "apple"]
print("Original list8:", list8)
bubble_sort_strings(list8)
print("Sorted list8:  ", list8)
print()

# Test case 9: List with one element
list9 = ["apple"]
print("Original list9:", list9)
bubble_sort_strings(list9)
print("Sorted list9:  ", list9)
print()

# Test case 10: Empty list
list10 = []
print("Original list10:", list10)
bubble_sort_strings(list10)
print("Sorted list10:  ", list10)
