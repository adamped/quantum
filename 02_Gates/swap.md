# SWAP Gate

The SWAP gate literally swaps the state of two qubits, including both the phase and amplitudes.

    | 1  0  0  0 |
    | 0  0  1  0 |
    | 0  1  0  0 |
    | 0  0  0  1 |

The main purpose of this gate is for reordering qubits or transferring quantum states between qubits in commmunication protocols.

## iSWAP Gate

The iSWAP gate is a derivation of the SWAP gate, also know as the square root of SWAP gate. It is a two qubit gate that combines the swapping action of the SWAP gate with a phase shift.

In addition to swapping quantum states it adds a phase factor to the imaginary unit "i" in the amplitudes.

    | 1  0  0  0 |
    | 0  0  i  0 |
    | 0  i  0  0 |
    | 0  0  0  1 |

The iSWAP gate has many uses in simulating physical interactions and certain quantum algorithms.

## Fredkin (CSWAP) Gate

The Fredkin gate swaps the state of the two target qubits only if the control qubit is in state |1⟩.