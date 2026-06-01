#This is for E vs n for two atom honey comb lattice
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

N = 100         
t = 0   
tp = 1  
ky = 0

def h_block(m, alpha):
    theta = ky + 2*np.pi*alpha*m

    h = np.array([
        [-2*t*np.cos(theta),          -tp*(1 + np.exp(-1j*theta))],
        [-tp*(1 + np.exp(1j*theta)),  -2*t*np.cos(theta)]
    ], dtype=complex)

    return h

def T_block(m, alpha):
    theta = ky + 2*np.pi*alpha*m

    T = np.array([
        [-t*(1 + np.exp(-1j*theta)), 0],
        [-tp,                         -t*(1 + np.exp(-1j*theta))]
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

alpha_values = [1/70]

alpha_list = []
energy_list = []

for alpha in alpha_values:
    H = harper_matrix(N, alpha)
    energies = np.linalg.eigvalsh(H)

    for E in energies:
        alpha_list.append(alpha)
        energy_list.append(E)

c = [float(E) for E in energy_list]

Energy_greaterzero = []

for E in c:
    if E > 0:
        Energy_greaterzero.append(E)

Energy_greaterzero = np.array(Energy_greaterzero)
Energy_greaterzero = Energy_greaterzero[:20]

n_full = np.arange(0, len(Energy_greaterzero) )


x_full = n_full 

def power_law(x, A, eta):
    return A * x**eta

x_fit = x_full[1:]
E_fit_data = Energy_greaterzero[1:]
popt, pcov = curve_fit(power_law, x_fit, E_fit_data, p0=[E_fit_data[0], 1.0])
A, eta = popt
print("A =", A)
print("eta =", eta)
x_smooth = np.linspace(0, x_full[-1], 300)
Energy_fit = power_law(x_smooth, A, eta)

plt.scatter(x_full, Energy_greaterzero, label="Numerical energy")
plt.plot(x_smooth, Energy_fit, color="red",
         label=rf"Fit: $E = {A:.5f}(n)^{{{eta:.5f}}}$")

plt.xlabel(r"$n$")
plt.ylabel(r"$E_n - E_1$")
plt.legend()
plt.grid(True)
plt.show()

