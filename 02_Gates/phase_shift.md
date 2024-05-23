# Phase Shift Gates

Phase shift gates are designed to modify the phase of the qubit without affecting its probabilities. These gates don't affect the magnitude of the vector, only its complex plane direction.

Excluding the Pauli-Z gate and Rz, there are two common phase shift gates, S and T.

S and T gates are considered part of the universal gate set and are often implemented at a hardware level, giving faster and more reliable results.

## S Gate

S gate is a 90° rotation around the Z-axis.


## T Gate

T gate is a 45° rotation around the Z-axis.

The T gate is a type of non-Clifford gate. A non-Clifford gate means this can not be efficiently simulated on a classical computer; hence any algorithm using this gate would have the potential to gain a quantum advantage.