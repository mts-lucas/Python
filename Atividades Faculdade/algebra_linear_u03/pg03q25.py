import numpy as np

# Given matrix A
A = np.array([[-3, -2, 0], [14, 7, -1], [-6, 3, 1]])
print(A)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Create the diagonal matrix D
D = np.diag(eigenvalues)

# Calculate P*D*inv(P)
P = eigenvectors
reconstructed_A = P @ D @ np.linalg.inv(P)

# Calculate A*P - P*D
check_eigendecomposition = A @ P - P @ D

# Print eigenvalues, eigenvectors, reconstructed A, 
# and the difference A*P - P*D
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
print("\nReconstructed A:")
print(reconstructed_A)
print("\nA*P - P*D:")
print(check_eigendecomposition)
