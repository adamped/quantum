from pyquil import Program
from pyquil.gates import *

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

# CNOT
p += CNOT(0, 1)

# Measure to classical readout
p += MEASURE(0, ro[0])