import time
import matplotlib.pyplot as plt import random
def linear_search(arr, x):
for i in range(len(arr)):
if arr[i] == x: return i
return -1
n_values = [100, 1000, 10000, 100000, 1000000]
time_values = []
for n in n_values:
arr = [random.randint(0, n) for _ in range(n)]
x = random.randint(0, n)
start_time = time.time()
linear_search(arr, x) end_time =
time.time()
time_values.append(end_time - start_time)
plt.plot(n_values, time_values)
plt.title('Linear Search')
plt.xlabel('Number of Elements')
plt.ylabel('Time Taken (seconds)')
plt.show()
