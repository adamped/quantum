# Deutsch-Jozsa Algorithm

The Deutsch-Jozsa Algorithm is a simple algorithm. While it has little practical purpose it currently shows an algorithm with a quantum advantage and is a good introduction.

The algorithm determines if a given function is constant, always gives the same output regardless of input; or balanced, produces 0 or 1 with equal probability.

## Oracle

The oracle is a quantum function that accepts n qubits and returns a |0⟩ or |1⟩. This is the black box or function that we want to test if it is constant or balanced.

## Algorithm

1. Apply Hadamard Gate to every qubit for the input
2. Create an ancilla qubit (this is just an extra qubit)
3. Apply the X Gate, then the Hadamard Gate to the ancilla qubit. This sets the qubit to the |1⟩ state and then the |-⟩ state. This ensures the correct phase kickback.
4. Send the original qubits, plus the ancilla qubit through the Oracle
5. Apply Hadamard Gate to all input (original) qubits
6. Measure all input qubits, not the ancilla
7. If all measured qubits return 0, it is a constant function
8. Else it is a balanced function