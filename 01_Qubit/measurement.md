# Measurement

Measurement of a qubit collapses the wave function and returns a 0 or 1. Once a qubit is measured, all information about its phase and superposition are lost. This process is not reversible.

Measurements are normally the final step in the quantum algorithm to return a deterministic classical result.

Quantum computing languages may offer ways to measure multiple qubits at the same time. Additionally they may offer ways to also measure the x-axis and y-axis values to seeif they collapse in the |+⟩ and |-⟩ or |i⟩ and |-i⟩.

## Quantum State Tomography

Quantum State Tomography (QST) is designed to attempt to reconstruct the complete quantum state of a system, since measurement collapses the wave function and you lose all the additional information of the quantum state.

QST aims to work around this limitation by making identical copies of the quantum system, taking multiple measurements on the different X, Y and Z axis, then statistically analyzing to produce the observed outcomes.

The purpose is generally for error correction and research into quantum states.