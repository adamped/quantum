namespace MyQuantumProgram {

    operation Hadamard() : Result {
        
        // Allocate a qubit
        use qubit = Qubit();

        // Put qubit into superposition
        H(qubit); // <- H is the Hadamard gate

        // Measure qubit
        let result = M(qubit);

        return result;
    }

    operation PauliGates() : Result {
        
        // Allocate a qubit
        use qubit = Qubit();

        // Apply Pauli-X Gate
        X(qubit);

        // Apply Pauli-Y Gate
        Y(qubit);

        // Apply Pauli-Z Gate
        Z(qubit);

        // Measure qubit
        let result = M(qubit);

        return result;
    }
}