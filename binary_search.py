def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
import matplotlib.pyplot as plt
X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [0, 1, 4, 9, 20, 25, 36, 55, 64, 90, 100]
plt.plot(X, Y)
plt.xlabel('Input Size (n)')
plt.ylabel('Time Complexity (n^2)')
plt.title('Time Complexity Graph of Binary Search')
plt.show()

