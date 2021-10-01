
# A bubble sort algorithm involves picking a pair of consequtive numbers, and then swapping values based on value
# Time complexity is O(n^2) in the worst case scenario and O(n) in the best case scenario


import array_generator
import time

def bubble_sort(array):
    for j  in range(len(array)):
        swapped = False
        
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                array_i = array[i]
                array[i] = array[i+1]
                array[i+1] = array_i
                swapped = True

            if swapped == False:
                break

    return array

def main():
    array = array_generator.array_generator()

    start_time = time.time()
    sorted_array = bubble_sort(array)
    end_time = time.time()
    print(sorted_array)
    print("Time taken is: {}".format((end_time - start_time)))

if __name__ == "__main__":
    main()
