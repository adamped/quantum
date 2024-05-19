from qiskit import QuantumCircuit

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Apply Hadamard gate to put the qubit in superposition
qc.h(0)

# Measure qubit
result = qc.measure(0, 0)

# Measurement can be retrieved after the circuit has run