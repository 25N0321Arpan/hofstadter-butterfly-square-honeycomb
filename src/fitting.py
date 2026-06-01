def power_law(x, A, eta):
    return A * x**eta

x_fit = x_full[1:]
E_fit_data = Energy_greaterzero[1:]
popt, pcov = curve_fit(power_law, x_fit, E_fit_data, p0=[E_fit_data[0], 1.0])
A, eta = popt
print("A =", A)
print("eta =", eta)
