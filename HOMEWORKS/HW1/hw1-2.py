import numpy as np
import matplotlib.pyplot as plt

# Taylor series-based approximation
def taylor_approx_cos_diff(x, delta):
    return -delta * np.sin(x) - (delta**2 / 2) * np.cos(x)

# Trigonometric identity: -2 sin((δ)/2) sin((2x + δ)/2)
def identity_cos_diff(x, delta):
    return -2 * np.sin(delta / 2) * np.sin((2 * x + delta) / 2)

# Pick two values for x
x1 = np.pi      # x = π
x2 = 10**6      # x = 1,000,000

# Create δ values from 10^-16 to 1 (logarithmic spacing)
delta_values = np.logspace(-16, 0, num=16)

# Calculate the approximations for x = π
taylor_diffs_x1 = taylor_approx_cos_diff(x1, delta_values)
identity_diffs_x1 = identity_cos_diff(x1, delta_values)

# Calculate the approximations for x = 1,000,000
taylor_diffs_x2 = taylor_approx_cos_diff(x2, delta_values)
identity_diffs_x2 = identity_cos_diff(x2, delta_values)

# Calculate absolute differences for x = π
diff_x1_taylor_vs_identity = np.abs(taylor_diffs_x1 - identity_diffs_x1)

# Calculate absolute differences for x = 1,000,000
diff_x2_taylor_vs_identity = np.abs(taylor_diffs_x2 - identity_diffs_x2)

# Plot the results
plt.figure(figsize=(12, 6))

# Plot for x = π
plt.subplot(1, 2, 1)
plt.plot(delta_values, diff_x1_taylor_vs_identity, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.title('Taylor vs Identity for x = π')
plt.xlabel('δ')
plt.ylabel('Difference')
plt.legend()

# Plot for x = 1,000,000
plt.subplot(1, 2, 2)
plt.plot(delta_values, diff_x2_taylor_vs_identity, marker='x')
plt.xscale('log')
plt.yscale('log')
plt.title('Taylor vs Identity for x = 10^6')
plt.xlabel('δ')
plt.ylabel('Difference')
plt.legend()

plt.tight_layout()
plt.show()
