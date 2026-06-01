#Hofstadter butterfly for hexagonal lattice 2 atom
import numpy as np
import matplotlib.pyplot as plt

N =100         
t = 0   
tp = 1  
ky = 0

def h_block(m, alpha):
    theta = ky + 2*np.pi*alpha*m
    eta1=2*np.pi*alpha*m-ky

    h = np.array([
        [-2*t*np.cos(theta),        -tp*(1 + np.exp(-1j*eta1))],
        [-tp*(1 + np.exp(1j*eta1)), -2*t*np.cos(theta)]
    ], dtype=complex)

    return h

def T_block(m, alpha):
    eta1=2*np.pi*alpha*m-ky

    T = np.array([
        [-t*(1 + np.exp(-1j*eta1)), 0],
        [-tp,                         -t*(1 + np.exp(-1j*eta1))]
    ], dtype=complex)

    return T

def harper_matrix(N, alpha):
    H = np.zeros((2*N, 2*N), dtype=complex)

    for m in range(N):
        h = h_block(m, alpha)

        H[2*m:2*m+2, 2*m:2*m+2] = h

        if m < N - 1:
            T = T_block(m, alpha)

            H[2*m:2*m+2, 2*(m+1):2*(m+1)+2] = T
            H[2*(m+1):2*(m+1)+2, 2*m:2*m+2] = T.conj().T

    return H

alpha_values = np.linspace(0, 1, 500)

alpha_list = []
energy_list = []

for alpha in alpha_values:
    H = harper_matrix(N, alpha)
    energies = np.linalg.eigvalsh(H)

    for E in energies:
        alpha_list.append(alpha)
        energy_list.append(E)

plt.figure(figsize=(7, 6))
plt.scatter(alpha_list, energy_list, s=0.2)
plt.xlabel(r"$\alpha=\Phi/\Phi_0$")
plt.ylabel(r"$E$")
plt.title("Hofstadter butterfly for two-atom hexagonal lattice")
plt.show()

