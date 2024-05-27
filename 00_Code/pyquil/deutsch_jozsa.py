from pyquil import Program, get_qc
from pyquil.gates import H, X, CNOT, MEASURE

def oracle(qubits):
    # Example of a balanced oracle
    CNOT(qubits[0], qubits[-1]) 

def deutsch_jozsa(n_qubits):
    p = Program()

    # Create a quantum computer
    qc = get_qc('qvm-name') 

    # Create qubits
    register = list(range(n_qubits))
    ancilla = n_qubits 

    # Prepare initial state
    p += [H(i) for i in register]
    p += X(ancilla)
    p += H(ancilla)

    # Apply the oracle
    oracle(register + [ancilla])  

    # Apply Hadamard gates to the register qubits
    p += [H(i) for i in register]

    # Measure the register qubits
    ro = p.declare('ro', 'BIT', n_qubits)
    for i in register:
        p += MEASURE(i, ro[i])

    # Compile the program
    executable = qc.compile(p)

    # Run the program and get results
    result = qc.run(executable)
    measured_bits = result.readout_data.get('ro')

    # Check if all results are 0
    all_zero = all(bit == 0 for bit in measured_bits[0])
    return all_zero

# Example usage
n_qubits = 2 
is_constant = deutsch_jozsa(n_qubits)
print(f"Constant function: {is_constant}")