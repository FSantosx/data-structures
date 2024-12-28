import time 

def binary_search (arr, item):
    down = 0
    top = len(arr) - 1
    while down <= top:
        middle = (down + top) // 2 # two slashes considers the integer part of division
        guess = arr[middle]
        if guess == item:
            return middle
        if guess > item:
            top = middle - 1
        else:
            down = middle + 1

my_list = [1, 3, 4, 5, 6 , 7, 8, 9, 10, 11, 12, 14, 16, 40, 55, 65, 66, 67, 68, 69]


st = time.time()
print(binary_search(my_list, 14))
et = time.time()
elepesed_time = (et - st) * 1000 # to calculate a execution time in milliseconds
print('Execution time:', elepesed_time, 'milliseconds')
