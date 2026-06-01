# Hofstadter Butterfly in Square and Honeycomb Lattices

This project studies the Hofstadter butterfly spectrum of tight-binding lattice models in a perpendicular magnetic field. The square lattice Harper model and a two-sublattice honeycomb/hexagonal lattice model are implemented numerically using Python.

## Overview

The Hofstadter butterfly appears when electrons move on a periodic lattice under a magnetic field. The magnetic field modifies the hopping terms through a Peierls phase, producing a fractal-like energy spectrum as a function of magnetic flux.

This project includes:

- Square lattice Harper equation
- Hofstadter butterfly spectrum
- Honeycomb/two-atom lattice Harper matrix
- Numerical diagonalization
- Energy-level scaling using power-law fitting

## Physics Background

For a square lattice in the Landau gauge,

```math
\mathbf{A} = (0, Bx, 0)
the tight-binding model reduces to the one-dimensional Harper equation,

\[
-t[\phi_{m+1}+\phi_{m-1}+2\cos(2\pi \alpha m+k_y)\phi_m] = E\phi_m,
\]

where

\[
\alpha = \frac{\Phi}{\Phi_0}
\]

is the magnetic flux per plaquette in units of the flux quantum.
