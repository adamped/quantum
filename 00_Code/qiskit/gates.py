from qiskit import QuantumCircuit
from math import pi

# Create a quantum circuit with two qubits
qc = QuantumCircuit(3)

# Hadamard gate
qc.h(0)

# Pauli-X gate
qc.x(0)

# Pauli-Y gate
qc.y(0)

# Pauli-Z gate
qc.z(0)

# S Phase Gate
qc.s(0)

# T Phase Gate
qc.t(0)

# Rotation Gates
qc.rx(3 * pi / 2, 0)   # 270 degrees in radians
qc.ry(pi / 4, 0)       # 45 degrees in radians
qc.rz(pi / 2, 0)       # 90 degrees in radians

# CNOT gate
qc.cx(0, 1)

# CZ gate
qc.cz(0, 1)

# SWAP gate
qc.swap(0, 1)

# iSWAP gate
qc.iswap(0, 1)

# CCNOT gate
qc.ccx(0, 1, 2) 

# Fredkin gate (CSWAP)
qc.cswap(0, 1, 2) 

# Measure qubit
result = qc.measure(0, 0)