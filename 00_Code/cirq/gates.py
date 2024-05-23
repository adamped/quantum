import cirq

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)
target_qubit = cirq.GridQubit(0, 1)

# CNOT gate
cnot_gate = cirq.CNOT(qubit, target_qubit)

# Create a circuit
circuit = cirq.Circuit(
 cirq.H(qubit), # Hadamard
 cirq.X(qubit), # Pauli-X
 cirq.Y(qubit), # Pauli-Y
 cirq.Z(qubit), # Pauli-Z
 cirq.S(qubit), # S Phase Gate
 cirq.T(qubit), # T Phase Gate
 cirq.measure(qubit, key='m') # Measurement.
)