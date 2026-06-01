#This is for square lattice
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

N = 100
t = 1.0
ky = 0

def harper_matrix(N, alpha, ky=0.0, t=1.0):
    H = np.zeros((N, N), dtype=float)

    for m in range(N):
        H[m, m] = -2 * t * np.cos(ky + 2 * np.pi * alpha * m)

        if m < N - 1:
            H[m, m + 1] = -t
            H[m + 1, m] = -t

    return H

alpha = 1 / 90

H = harper_matrix(N, alpha, ky, t)
energies = np.linalg.eigvalsh(H)


Energy_edge = energies[:20]


Energy_edge = Energy_edge - Energy_edge[0]


n_full = np.arange(0, len(Energy_edge) )


x_full = n_full 

def power_law(x, A, eta):
    return A * x**eta

x_fit = x_full[1:]
E_fit_data = Energy_edge[1:]
popt, pcov = curve_fit(power_law, x_fit, E_fit_data, p0=[E_fit_data[0], 1.0])
A, eta = popt
print("A =", A)
print("eta =", eta)
x_smooth = np.linspace(0, x_full[-1], 300)
Energy_fit = power_law(x_smooth, A, eta)

plt.scatter(x_full, Energy_edge, label="Numerical energy")
plt.plot(x_smooth, Energy_fit, color="red",
         label=rf"Fit: $E = {A:.5f}(n)^{{{eta:.5f}}}$")

plt.xlabel(r"$n$")
plt.ylabel(r"$E_n - E_1$")
plt.legend()
plt.grid(True)
plt.show()
