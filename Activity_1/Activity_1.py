import numpy as np
import matplotlib.pyplot as plt

# 1. Array of 100,000 random values equally distributed between -2 and +3.3
x1 = np.random.uniform(-2, 3.3, 100000)
print("Task 1:")
print("Lowest:", np.min(x1))
print("Highest:", np.max(x1), "\n")

# 2. Array of sums of two random values
x2 = np.random.rand(100000) + np.random.rand(100000)
print("Task 2:")
print("Average:", np.mean(x2), "\n")

# 3. Array of multiplications of two random values
x3 = np.random.rand(100000) * np.random.rand(100000)
print("Task 3:")
print("Average:", np.mean(x3), "\n")

# 4. Array from normal distribution (mean=0.3, std=1.2)
x4 = np.random.normal(0.3, 1.2, 100000)
print("Task 4:")
print("Average:", np.mean(x4))
print("Std deviation:", np.std(x4), "\n")

# 5. Two arrays of integers (0–20), then c[i] = a[i] - b[i-1]
a = np.random.randint(0, 21, 100000)
b = np.random.randint(0, 21, 100000)
c = a[1:] - b[:-1]  # length 99,999
print("Task 5: Histogram of c values")
plt.hist(c, bins=np.arange(-20.5, 21.5, 1), edgecolor="black")
plt.title("Histogram of c = a[i] - b[i-1]")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 6. Normal distribution (mean=3, std=1.2), histogram from -0.6 to +0.6 with bin width 0.05
x6 = np.random.normal(3, 1.2, 100000)
bins = np.arange(-0.6, 0.6 + 0.05, 0.05)
print("Task 6: Histogram")
plt.hist(x6, bins=bins, edgecolor="black")
plt.title("Histogram (mean=3, std=1.2)")
plt.xlabel("Value range (-0.6 to +0.6)")
plt.ylabel("Frequency")
plt.show()