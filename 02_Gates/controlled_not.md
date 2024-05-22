# Controlled NOT Gate

The Controlled NOT gate is often called the CNOT or CX gate. It is a two qubit gate, meaning it is a gate that requires two qubits to act upon.

The CNOT gate is commonly used for:

1. Entanglement - Creating a Bell State by entangling two qubits
2. Teleportation - Transferring quantum states from one location to another

In a CNOT gate there is a control and target qubit. A CNOT gate works similar to an if then statement. If the control is |1⟩, then flip the target qubit, else do nothing.

## Error Correction

You will commonly use this gate for detection of errors, where you entangle the qubit with another and then ensure the qubits are the same. These qubits are referred to as ancilla qubits. 

You can perform the CNOT gate multiple times with multiple qubits for additional protection. CNOT gates are also reversible meaning you can undo the behavior by applying to the same two qubits.

Additional gates and methods are used for actually performing the error correction.