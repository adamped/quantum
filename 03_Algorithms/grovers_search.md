# Grovers Search

Designed for finding a metaphorical needle in a haystack, Grover's search algorithm provides a large speed advantage when finding data in a large unstructured search space. It is able to achieve this by exploring multiple elements in the search space simultaneously.

## Oracle

The Oracle is the special function that can determine if the element is the one you are looking for. Grover's search doesn't need to know how the Oracle works, just that it can distinguish the element being searched for.

## Algorithm

### Qubit Initialization

Take the node count and divide by 2. Create this many qubits and apply the Hadamard gate to each, as each qubit can be a superposition of |0⟩ and |1⟩, hence can represent 2 nodes per qubit.

### Grover Diffusion Operator

Apply the Grover Diffusion operator to every qubit. This particular operation applies multiple gates that rotate the state of the qubits in a way where the target node will be amplified.

### Apply Oracle

For each node in the graph, apply the oracle by passing the node and qubit register to the Oracle operation. Afterwards, apply the Grover Diffusion operator again to the qubit register each time you pass a node to the Oracle.

### Measurement

Finally, measure all qubits and see which one has collapsed to One. This will be node that contains the value you are looking for.

While this algorithm looks like you are looping through every node, it is a quantum circuit and these operations are applied differently than in a classical circuit.