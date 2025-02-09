 #ASSIGNMENT-4
import numpy as np
# Q.1 Creating a 1D NumPy array with 5 elements
arr1 = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr1)
print("Addition of 2:", arr1 + 2)
print("Multiplication by 3:", arr1 * 3)
print("Division by 2:", arr1 / 2)


# Q.2(a) Reverse a NumPy array
arr2 = np.array([1, 2, 3, 6, 4, 5])
print("Reversed Array:", arr2[::-1])


# Q.2(b) Find most frequent value and its indices
x = np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
most_freq_x = np.bincount(x).argmax()
x_indices = np.where(x == most_freq_x)
print("Most frequent value in x:", most_freq_x, "at indices", x_indices)

most_freq_y = np.bincount(y).argmax()
y_indices = np.where(y == most_freq_y)
print("Most frequent value in y:", most_freq_y, "at indices", y_indices)


# Q.3 Accessing elements in a 2D array
arr3 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("1st row, 2nd column:", arr3[0, 1])
print("3rd row, 1st column:", arr3[2, 0])


# Q.4 Creating a 1D NumPy array with linspace()
ishank = np.linspace(10, 100, 25)
print(ishank)
print("Dimensions:", ishank.ndim)
print("Shape:", ishank.shape)
print("Total Elements:", ishank.size)
print("Data Type:", ishank.dtype)
print("Total Bytes:", ishank.nbytes)

# Transposing the array using reshape()
reshaped_name = ishank.reshape(25, 1)
print("Reshaped Array:\n", reshaped_name)

# Checking T attribute
print("Using T attribute:\n", ishank.T)


# Q.5 Creating a 2D array and performing operations
ucs420_ishank = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])
print("Mean:", np.mean(ucs420_ishank))
print("Median:", np.median(ucs420_ishank))
print("Max:", np.max(ucs420_ishank))
print("Min:", np.min(ucs420_ishank))
print("Unique Elements:", np.unique(ucs420_ishank))

# Reshape to 4 rows, 3 columns
reshaped_ucs420_ishank = ucs420_ishank.reshape(4, 3)
print("Reshaped Array:\n", reshaped_ucs420_ishank)

# Resize to 2 rows, 3 columns
resized_ucs420_ishank = np.resize(ucs420_ishank, (2, 3))
print("Resized Array:\n", resized_ucs420_ishank)