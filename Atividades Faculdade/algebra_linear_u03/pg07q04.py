import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Given data
t = np.array([0, 1, 2, 3, 4])
p = np.array([1.0, 1.8, 3.3, 6.0, 11.0])

# Exponential function


def exponential_func(t, a, b):
    return a * np.exp(b * t)


# Perform curve fitting
params, _ = curve_fit(exponential_func, t, p)

# Extract the parameters
a, b = params

# Predict the population after 5 hours
p_pred = exponential_func(5, a, b)

# Print the parameters and predicted population
print("Parameters (a, b):", a, b)
print("Predicted population after 5 hours:", p_pred)

# Plot the data points and fitted curve
plt.xlabel('Time (hours)')
plt.ylabel('Population (thousands)')
plt.scatter(t, p, label='Data Points')
plt.plot(t, exponential_func(t, a, b), label='Fitted Curve')
plt.legend()

# Predict the population for additional hours
t_extra = np.linspace(0, 5, 100)  # Generate more points for smoother curve
p_extra = exponential_func(t_extra, a, b)
plt.plot(t_extra, p_extra, linestyle='dashed', label='Extrapolated Curve')

# Display the plot
plt.legend()
plt.show()
