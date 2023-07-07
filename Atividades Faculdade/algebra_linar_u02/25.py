import numpy as np
from scipy.linalg import null_space

A = np.array([[3, 4, 5], [7, 4, 3], [8, 8, 9]])
B = np.array([66, 74, 136])

amp = np.hstack((A, B.reshape(-1, 1)))  # Combine A and B into a single matrix

rref_values = np.round(null_space(amp), decimals=4)

print('A: ', A, '\n\n', 'B: ', B, '\n\n', 'Amp:',
      amp, '\n\n', 'rref_values:', rref_values)
