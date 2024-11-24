# 5. A seguinte função encontra o maior número único dentro de um array,
# mas tem uma eficiência de O(N²). 
# Reescreva a função para que se torne uma eficiência O(N):

import time
import random
from collections import Counter

# O(N²) version
def greatestNumber(array):
    for i in array:
        # Assume for now that i is the greatest:
        isValTheGreatest = True

        for j in array:
            # If we find another value that is greater than i,
            # i is not the greatest:
            if j > i:
                isValTheGreatest = False

        # If, by the time we checked all the other numbers, i
        # is still the greatest, it means that i is the greatest number:
        if isValTheGreatest:
            return i

# O(N) version
def greatestNumberON(array):
    # Count the occurrences of each number
    counts = Counter(array)

    # Initialize the variable to store the largest unique number
    max_unique = -1

    # Iterate over the items in the counter
    for num, count in counts.items():
        # Check if the number is unique (occurs only once)
        if count == 1:
            # Update max_unique if this number is greater
            if num > max_unique:
                max_unique = num

    return max_unique

# Generate a large array of random integers
array_size = 10000  # Adjust the size as needed
array = [random.randint(0, 10000) for _ in range(array_size)]

# Measure time for the O(N²) version
start_time = time.time()
result_n2 = greatestNumber(array)
end_time = time.time()
time_n2 = end_time - start_time

# Measure time for the O(N) version
start_time = time.time()
result_n = greatestNumberON(array)
end_time = time.time()
time_n = end_time - start_time

print(f"O(N²) version result: {result_n2}, Time taken: {time_n2:.6f} seconds")
print(f"O(N) version result: {result_n}, Time taken: {time_n:.6f} seconds")
