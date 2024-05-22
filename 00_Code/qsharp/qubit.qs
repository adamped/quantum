namespace MyQuantumProgram {

    @EntryPoint()
    operation Main() : Result {
        
        // Allocate a qubit
        use qubit = Qubit();

        // Put qubit into superposition
        H(qubit);

        // Measure qubit
        let result = M(qubit);

        return result;
    }
}