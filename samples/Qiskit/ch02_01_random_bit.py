## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

## This sample generates a single random bit.

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, IBMQ, BasicAer
import math
## Uncomment the next line to see diagrams when running in a notebook
#%matplotlib inline

## Example 2-1: Random bit
# Set up the program

## TASMIA
## Intention:
# Prepare one qubits, put it in superposition,
# measure it to get one random bit, and print the counts and the state.
#setup of the register
reg = QuantumRegister(1, name='reg')
reg_c = ClassicalRegister(1, name='regc')
qc = QuantumCircuit(reg, reg_c)

##TASMIA
#(1) initialization in next step (reset) with write 0
qc.reset(reg)          # write the value 0
##TASMIA
#(2) superposition in next step (h gate)
qc.h(reg)              # put it into a superposition of 0 and 1
##TASMIA
#(3)quantum-classical split? Through measurement and print
qc.measure(reg, reg_c) # read the result as a digital bit

backend = BasicAer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()

counts = result.get_counts(qc)
print('counts:',counts)

outputstate = result.get_statevector(qc, decimals=3)
print(outputstate)
qc.draw()        # draw the circuit
