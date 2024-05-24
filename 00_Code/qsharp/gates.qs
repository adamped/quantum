namespace MyQuantumProgram {

open Microsoft.Quantum.Math;

    operation Hadamard() : Result {
        
        // Allocate a qubit
        use qubit = Qubit();

        // Put qubit into superposition
        H(qubit); // <- H is the Hadamard gate

        // Measure qubit
        let result = M(qubit);

        return result;
    }

    operation Gates() : Result {
        
        // Allocate a qubit
        use qubit = Qubit();

        // Apply Pauli-X Gate
        X(qubit);

        // Apply Pauli-Y Gate
        Y(qubit);

        // Apply Pauli-Z Gate
        Z(qubit);

        // Apply S Phase Gate
        S(qubit);

        // Apply T Phase Gate
        T(qubit);

        // Rotation Gates (Radians = degrees * PI / 180)
        Rx(270.0 * PI() / 180.0, qubit);
        Ry(45.0 * PI() / 180.0, qubit);
        Rz(90.0 * PI() / 180.0, qubit);

        use targetQubit = Qubit();

        // CNOT Gate
        CX(qubit, targetQubit);

        // Controlled Phase Gate
        Controlled Z([qubit], targetQubit);

        // SWAP Gate
        SWAP(qubit, targetQubit);

        // iSWAP Gate not available as function but can build own

        // Measure qubit
        let result = M(qubit);

        return result;
    }
}