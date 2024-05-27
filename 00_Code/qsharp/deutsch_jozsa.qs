namespace DeutschJozsa {

    open Microsoft.Quantum.Convert;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    operation Oracle (target : Qubit[]) : Unit {
        // The black box function you wish to test is a constant or balanced function
    }

    operation DeutschJozsa (register : Qubit[]) : Bool {

        let nQubits = Length(register);
        use ancilla = Qubit();

        // Prepare the initial state
        ApplyToEach(H, register);
        X(ancilla);
        H(ancilla);

        // Apply the oracle
        Oracle(register + [ancilla]);

        // Apply Hadamard gates to all qubits in the register
        ApplyToEach(H, register);

        // Measure the qubits in the register
        let results = MeasureEachZ(register);

        // Return true if all measurement results are 0, false otherwise
        for result in results
        {
            if (result == One)
            {
                return false;
            }
        }

        return true; // All Zero
    }
}