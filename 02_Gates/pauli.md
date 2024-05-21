# Pauli Gates

As shown in the Bloch Sphere there are 3 axis on which a qubit could be flipped mathematically.

## Pauli-X

Will rotate the phase 180° around the X-axis, between |+⟩ and |-⟩.

Given the mirror rotation it will flip the probabilities between |0⟩ and |1⟩.

    X = | 0  1 |
        | 1  0 |

Hence the gate will flip the qubit as shown

    X|0⟩ = |1⟩
    X|1⟩ = |0⟩

## Pauli-Y

Will rotate the phase 180° around the Y-axis, between i|0⟩ and -i|1⟩.

Given the mirror rotation it will also flip the probabilities between |0⟩ and |1⟩, while also introducing a phase shift.

    Y = | 0 -i |
        | i  0 |

Hence the gate will flip the qubit as shown

    Y|0⟩ = i|1⟩
    Y|1⟩ = -i|0⟩

## Pauli-Z

Will not rotate 180° around the Z-axis, between |0⟩ and |1⟩. This is a key difference between the X and Y gates. The qubit will only phase shift on the Z-axis, and only flipping the phase for the |1⟩ state.

This will keep the probabilities between |0⟩ and |1⟩ the same but produce a phase shift along the |+⟩ and |-⟩ (x-axis). 

    Z|0⟩ = |0⟩ 
    Z|1⟩ = -|1⟩