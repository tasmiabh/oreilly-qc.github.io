// Programming Quantum Computers
//   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
//   O'Reilly Media

// To run this online, go to http://oreilly-qc.github.io?p=3-3

qc.reset(3);
// Create two registers
var reg1 = qint.new(2, 'Register 1');
var reg2 = qint.new(1, 'Register 2');
// TASMIA
// Initialize the registers, control is set to 0, target is set to 1
reg1.write(0);
reg2.write(1);
// Place the first register in superposition
// TASMIA
// Superposition of the control register
reg1.had();
// Perform phase rotations on second register,
//conditioned on qubits from the first
// TASMIA
// The controlled phase gates - phase shift
qc.phase(45, 0x4, 0x1);
qc.phase(90, 0x4, 0x2);
