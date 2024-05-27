from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator


def oracle(circuit, register, ancilla):
    # Example of a balanced oracle
    circuit.cx(register[0], ancilla)

def deutsch_jozsa(n_qubits):
    # Create registers
    qr = QuantumRegister(n_qubits, name="register")
    ancilla = QuantumRegister(1, name="ancilla")
    cr = ClassicalRegister(n_qubits, name="results")
    qc = QuantumCircuit(qr, ancilla, cr)

    # Prepare initial state
    qc.h(qr)  # Hadamard on all qubits in the register
    qc.x(ancilla)
    qc.h(ancilla)

    # Apply the oracle
    oracle(qc, qr, ancilla[0])  # Pass ancilla as single qubit

    # Apply Hadamard gates to the register qubits
    qc.h(qr)

    # Measure the register qubits
    qc.measure(qr, cr)

    # Simulate the circuit
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts(qc)

    # Check if all results are 0
    return '0' * n_qubits in counts

# Example usage
n_qubits = 2 
is_constant = deutsch_jozsa(n_qubits)
print(f"Constant function: {is_constant}")
