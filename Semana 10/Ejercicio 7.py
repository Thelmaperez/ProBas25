import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


size = 10  
random_list = [random.randint(1, 100) for _ in range(size)]
print("Lista original:", random_list)


sorted_list = quicksort(random_list)
print("Lista ordenada:", sorted_list)

target = int(input("Ingrese un número para buscar: "))
index = binary_search(sorted_list, target)


if index != -1:
    print(f"El número {target} se encuentra en la posición {index} de la lista ordenada.")
else:
    print(f"El número {target} no está en la lista.")
