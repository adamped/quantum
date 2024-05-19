from pyquil import Program
from pyquil.gates import *

p = Program()

# Declare classical region for readout (ro)
ro = p.declare('ro', 'BIT', 1)

# Hadamard Gate
p += H(0)

# Measure to classical readout
p += MEASURE(0, ro[0])