import numpy as np
arr = np.arange(1,11)
#Array slicing methods
print(arr[1:4])
print(arr[::2])
print(arr[::-1])
#Array staitical methods
print(np.std(arr))
print(np.sum(arr))
print(np.median(arr))
#Array Broadcasting methods
print(arr + 5)
print(arr * 5)
print(arr / 10 * 100)