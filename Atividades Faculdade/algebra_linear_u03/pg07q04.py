import matplotlib.pyplot as plt
import numpy as np

# Given data
t_data = np.array([0, 1, 2, 3, 4])
p_data = np.array([1.0, 1.8, 3.3, 6.0, 11.0])

# Exponential function


def exponential_func(t, a, b):
    return a * np.exp(b * t)


# Perform matrix manipulation
A = np.column_stack((np.exp(t_data), t_data))
b = np.log(p_data)

# Calculate the parameters using the normal equation
x = np.linalg.inv(A.T @ A) @ A.T @ b
a = np.exp(x[0])
b = x[1]

# Predict the population after 5 hours
t_pred = 5
p_pred = exponential_func(t_pred, a, b)

# Print the parameters and predicted population
print("Parameters (a, b):", a, b)
print("Predicted population after 5 hours:", p_pred)

# Plot the data points and fitted curve
plt.xlabel('Time (hours)')
plt.ylabel('Population (thousands)')
plt.scatter(t_data, p_data, label='Data Points')
plt.plot(t_data, exponential_func(t_data, a, b), label='Fitted Curve')
plt.legend()

# Predict the population for additional hours
t_extra = np.linspace(0, 5, 100)  # Generate more points for smoother curve
p_extra = exponential_func(t_extra, a, b)
plt.plot(t_extra, p_extra, linestyle='dashed', label='Extrapolated Curve')

# Display the plot
plt.legend()
plt.show()
