import matplotlib.pyplot as plt
import numpy as np

# Data provided
V = [0.88, 1.10, 1.42, 1.77, 2.14]
R = [3.00, 2.30, 1.65, 1.25, 1.01]

# Calculate eccentricity and constant
e = np.sqrt((np.max(R)**2 - np.min(R)**2) + (np.max(V)**2 - np.min(V)**2))
beta = np.min(R) - e * np.min(V)

# Print the eccentricity and constant
print("Eccentricity (e):", e)
print("Constant (beta):", beta)

theta = np.linspace(0, 4.6, 100)
r = beta + e * np.cos(theta)

# Plot the orbit
plt.figure(figsize=(8, 6))
plt.plot(theta, r)
plt.xlabel('ϑ (radians)')
plt.ylabel('r')
plt.title('Orbit of the Comet')
plt.grid(True)

# Plot the predicted position
plt.scatter(4.6, beta + e * np.cos(4.6),
            color='red', label='Predicted Position')
plt.legend()

# Show the plot
plt.show()
