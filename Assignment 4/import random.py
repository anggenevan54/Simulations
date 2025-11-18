import random
import math
import numpy as np
import matplotlib.pyplot as plt

# 1. Monte Carlo Estimation of PI

def estimate_pi(n_points=1_000_000):
    inside = 0
    for _ in range(n_points):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / n_points


print("\n=== Monte Carlo Estimation of π ===")
pi_est = estimate_pi(1_000_000)
print("Estimated π:", pi_est)
print("Actual π:", math.pi)


# 2. Central Limit Theorem (Uniform Distribution)

n_samples = 10000     # number of sample means
sample_size = 50      # sample size

means_uniform = []

for _ in range(n_samples):
    sample = np.random.uniform(0, 1, sample_size)
    means_uniform.append(np.mean(sample))

means_uniform = np.array(means_uniform)

print("\n=== Central Limit Theorem (Uniform Distribution) ===")
print("Mean of sample means:", np.mean(means_uniform))
print("Std of sample means:", np.std(means_uniform))

plt.figure()
plt.hist(means_uniform, bins=40, density=True)
plt.title("CLT Demonstration (Uniform → Sample Means)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()


# 3. Central Limit Theorem (Gamma Distribution)

shape = 2
scale = 2

means_gamma = []

for _ in range(n_samples):
    sample = np.random.gamma(shape, scale, sample_size)
    means_gamma.append(np.mean(sample))

means_gamma = np.array(means_gamma)

print("\n=== Central Limit Theorem (Gamma Distribution) ===")
print("Mean of Gamma sample means:", np.mean(means_gamma))
print("Std of Gamma sample means:", np.std(means_gamma))

plt.figure()
plt.hist(means_gamma, bins=40, density=True)
plt.title("CLT Demonstration (Gamma → Sample Means)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.show()
