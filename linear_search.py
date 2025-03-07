import matplotlib.pyplot as plt
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = [2, 3, 4, 10, 40]
x = 50
result = linear_search(arr, x)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
n = [10, 20, 50, 100, 200, 500, 1000]
time = [0.0001, 0.0002, 0.0005, 0.0025, 0.0030, 0.0085, 0.0150]
plt.plot(n, time)
plt.xlabel('Number of Elements')
plt.ylabel('Time Taken')
plt.title('Time Complexity of Linear Search')
plt.show()

