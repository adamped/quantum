import cirq

def deutsch_jozsa(oracle_circuit: cirq.Circuit, n_qubits: int) -> cirq.Circuit:
   
    qubits = cirq.LineQubit.range(n_qubits + 1) # Input qubits + 1 ancilla qubit
    
    # Prepare initial state
    circuit = cirq.Circuit(cirq.H.on_each(qubits[:-1]), # Hadamard on input qubits
                           cirq.X(qubits[-1]),
                           cirq.H(qubits[-1]))

    # Apply the oracle
    circuit.append(oracle_circuit.all_operations())

    # Apply Hadamard gates to input qubits again
    circuit.append(cirq.H.on_each(qubits[:-1]))

    # Measure input qubits
    circuit.append(cirq.measure(*qubits[:-1], key='result')) 

    return circuit

# Example: Defining Oracles
def constant_oracle(qubits):
    return cirq.Circuit()  # Does nothing (all outputs are 0)

def balanced_oracle(qubits):
    return cirq.Circuit(cirq.CNOT(qubits[0], qubits[-1])) # Flips the output based on the first input qubit

# Example Usage
n_qubits = 3 

# Test with a constant oracle
oracle = constant_oracle(cirq.LineQubit.range(n_qubits + 1))
dj_circuit = deutsch_jozsa(oracle, n_qubits)

# Test with a balanced oracle
oracle = balanced_oracle(cirq.LineQubit.range(n_qubits + 1))
dj_circuit = deutsch_jozsa(oracle, n_qubits)

# Simulate to get results
simulator = cirq.Simulator()
result = simulator.run(dj_circuit, repetitions=10)
print(result) 
