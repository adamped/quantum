from qiskit import QuantumCircuit

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Hadamard gate
qc.h(0)

# Pauli-X gate
qc.x(0)

# Pauli-Y gate
qc.y(0)

# Pauli-Z gate
qc.z(0)

# Measure qubit
result = qc.measure(0, 0)