import cirq

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
 cirq.H(qubit), # Hadamard
 cirq.X(qubit), # Pauli-X
 cirq.Y(qubit), # Pauli-Y
 cirq.Z(qubit), # Pauli-Z
 cirq.measure(qubit, key='m') # Measurement.
)