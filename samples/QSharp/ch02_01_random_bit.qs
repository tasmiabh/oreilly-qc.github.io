namespace QSharp.Chapter2
{
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    // Example 2-1: Random bit

    operation RandomBit () : Unit {
        //TASMIA
        //The language handles the initialization through use.
        // allocate one qubit
        use q = Qubit();
        //TASMIA
        //h gate is used for superposition
        // put it into superposition of 0 and 1
        H(q);

        //TASMIA
        //quantum-classical split, measure and the return a value
        // measure the qubit and store the result
        let bit = M(q);
        
        // make sure the qubit is back to the 0 state
        Reset(q);
        
        Message($"{bit}");
    }
}
