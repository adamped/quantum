from qiskit import QuantumCircuit

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Apply Hadamard gate to put the qubit in superposition
# 0 is the index in the quantum circuit for the particular qubit
qc.h(0)

# Measure qubit
result = qc.measure(0, 0)

# Measurement can be retrieved after the circuit has run