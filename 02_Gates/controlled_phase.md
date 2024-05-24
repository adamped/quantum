# Controlled Phase Gate

The Controlled Phase Gate, also know as CPhase or CZ gate, is a two qubit gate that will apply a phase shift to a target qubit only if the control qubit is in a |1⟩ state.

You can create a CZ gate that acts upon the target if in the |0⟩, but it is more common to use |1⟩.

When applied a CZ gate will multiple the entire quantum state by the phase of the control qubit.

    | 1  0  0  0 |
    | 0  1  0  0 |
    | 0  0  1  0 |
    | 0  0  0  e^(iφ) |

Phi (φ) expressed in radians, represents the phase shift angle to apply to the target qubit.