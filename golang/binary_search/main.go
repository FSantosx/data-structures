package main

import "fmt"

func binarySearch(arr []int, item int) int {
    down := 0
    top := len(arr) - 1
    for down <= top {
        middle := (down + top) / 2
        guess := arr[middle]
        if guess == item {
            return middle
        }
        if guess > item { 
            top = middle - 1
        } else {
            down = middle + 1
        }
    }
    return -1
}

func main() {
    fmt.Println("Hello, World!")
    list := []int{1, 3, 4, 5, 6 , 7, 8, 9, 10, 11, 12, 14, 16, 40, 55, 65, 66, 67, 68, 69}
    item := binarySearch(list, 66)
    fmt.Println(item)
}