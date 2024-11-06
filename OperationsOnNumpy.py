import numpy as np

original_array = np.linspace(0, 9, num=10)
print("Original Array:")
print(original_array)

modified_array = np.copy(original_array)
modified_array[modified_array % 2 != 0] = 1
print("\nModified Array (odd numbers replaced with 1):")
print(modified_array)

two_dimensional_array = original_array.reshape(2, -1)
print("\n2-Dimensional Array (2 rows):")
print(two_dimensional_array)

sum_of_evens = np.sum(original_array[original_array % 2 == 0])
print("\nSum of all even numbers in the original array:")
print(sum_of_evens)