from pyquil import Program
from pyquil.gates import *
from math import pi

p = Program()

# Declare classical region for readout (ro)
ro = p.declare('ro', 'BIT', 2)

# Hadamard Gate
p += H(0)

# Pauli-X
p += X(0)

# Pauli-Y
p += Y(0)

# Pauli-Z
p += Z(0)

# S Phase Gate
p += S(0)

# T Phase Gate
p += T(0)

# Rotation Gates (Radians = degrees * PI / 180)
p += RX(270.0 * pi / 180.0, 0)
p += RY(45.0 * pi / 180.0, 0)
p += RZ(90.0 * pi / 180.0, 0)

# CNOT
p += CNOT(0, 1)

# CZ Gate
p += CZ(0, 1)  # Apply CZ to 0 (control) and 1 (target)

# Measure to classical readout
p += MEASURE(0, ro[0])