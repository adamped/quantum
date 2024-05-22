# Quantum Basics

A basic guide to quantum programming across multiple quantum languages, with an explanation of each concept. 

## Languages

The following Quantum programming languages will be used for demonstrating concepts.

### Cirq
- Superconducting qubits
- Google owned
- Python
- https://quantumai.google/cirq

### Qiskit
- Superconducting qubits
- IBM owned
- Python
- https://www.ibm.com/quantum/qiskit

### QSharp
- Topological qubits
- Microsoft owned
- Uses .NET for a runner but not a .NET language
- https://github.com/microsoft/qsharp

### pyQuil
- Superconducting qubits
- Rigetti owned
- Python
- https://pyquil-docs.rigetti.com/en/stable/


## 01_Qubit

- [What is a qubit?](01_Qubit/what_is_qubit.md)
- [Qubit types](01_Qubit/qubit_types.md)
- [Qubit phase](01_Qubit/qubit_phase.md)

### Examples
- [Cirq](00_Code/cirq/qubit.py)
- [Qiskit](00_Code/qiskit/qubit.py)
- [QSharp](00_Code/qsharp/qubit.qs)
- [pyQuil](00_Code/pyquil/qubit.py)

## 02_Gates

Gates are similar to logic gates in classical computing. A qubit will go through a gate and potentially transform based on the gate.

A bit in a classical computer going through an NOT gate will flip from a 0 to a 1.

A qubit in a quantum computer going through a Pauli-X gate will rotate to the opposite on that axis.

### Types of gates

- [Hadamard](02_Gates/hadamard.md) - Places qubit into superposition
- [Pauli](02_Gates/pauli.md) - Changes phase or probabilities of qubit

### Examples
- [Cirq](00_Code/cirq/gates.py)
- [Qiskit](00_Code/qiskit/gates.py)
- [QSharp](00_Code/qsharp/gates.qs)
- [pyQuil](00_Code/pyquil/gates.py)