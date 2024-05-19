import cirq

# Pick a qubit.
qubit = cirq.GridQubit(0, 0)

# Create a circuit
circuit = cirq.Circuit(
 cirq.H(qubit),
 cirq.measure(qubit, key='m') # Measurement.
)