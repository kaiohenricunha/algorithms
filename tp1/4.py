# 4. Quantos passos a busca binária levaria para o exemplo anterior?
# R: Alvo 8 encontrado no índice 3 após 1 passo(s).

def binary_search(arr, target):
    steps = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            print(f"Target {target} found at index {mid} after {steps} step(s).")
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Target {target} not found after {steps} step(s).")
    return -1

# Given array and target
array = [2, 4, 6, 8, 10, 12, 13]
target_number = 8

# Perform binary search
binary_search(array, target_number)
