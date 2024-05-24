from qiskit import QuantumCircuit
from math import pi

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2)

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

# Measure qubit
result = qc.measure(0, 0)