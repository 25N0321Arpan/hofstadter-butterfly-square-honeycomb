
#Hofstadter butterfly for square lattice one atom
import numpy as np
import matplotlib.pyplot as plt
N = 100
t = 1.0
ky = 0

def harper_matrix(N, alpha, ky=0.0, t=1.0):
    H = np.zeros((N, N), dtype=float)

    for m in range(N):
        H[m, m] = -2 * t * np.cos(ky + 2 * np.pi * alpha * m)

        if m < N-1 :
            H[m, m + 1] = -t
            H[m + 1, m] = -t

    return H

alpha_values = np.linspace(0, 1, 500)

alpha_list= []
energy = []

for alpha in alpha_values:
    H = harper_matrix(N, alpha, ky, t)
    energies = np.linalg.eigvalsh(H)

    for E in energies:
        alpha_list.append(alpha)
        energy.append(E)

plt.scatter(alpha_list, energy, s=0.1, color='green')
plt.xlabel(r"$\alpha = \Phi/\Phi_0$")
plt.ylabel(r"Energy $E$")
plt.title("Hofstadter butterfly for square lattice")
plt.show()
