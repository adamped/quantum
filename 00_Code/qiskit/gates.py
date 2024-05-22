from qiskit import QuantumCircuit

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

# CNOT gate
qc.cx(0, 1)

# Measure qubit
result = qc.measure(0, 0)