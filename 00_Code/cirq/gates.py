import cirq
import numpy as np

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
 cirq.rx(3 * np.pi / 2)(qubit), # 270 degrees in radians
 cirq.ry(np.pi / 4)(qubit), # 45 degrees in radians
 cirq.rz(np.pi / 2)(qubit), # 90 degrees in radians
 cirq.measure(qubit, key='m') # Measurement.
)