def harper_matrix(N, alpha, ky=0.0, t=1.0):
    H = np.zeros((N, N), dtype=float)

    for m in range(N):
        H[m, m] = -2 * t * np.cos(ky + 2 * np.pi * alpha * m)

        if m < N-1 :
            H[m, m + 1] = -t
            H[m + 1, m] = -t

    return H
