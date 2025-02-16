#Problema 14

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    arr = list(map(int, input("Ingresa los números separados por espacios: ").split()))
    print("Métodos de ordenamiento:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    elige = int(input("Elige un método (1-3): "))
    
    if elige == 1:
        bubble_sort(arr)
    elif elige == 2:
        selection_sort(arr)
    elif elige == 3:
        insertion_sort(arr)
    else:
        print("Opción no válida")
        return
    
    print("Lista ordenada:", arr)

if __name__ == "__main__":
    main()
