## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io
##
## A complete notebook of all Chapter 4 samples (including this one) can be found at
##  https://github.com/oreilly-qc/oreilly-qc.github.io/tree/master/samples/Qiskit

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, IBMQ, BasicAer
import math
## Uncomment the next line to see diagrams when running in a notebook
#%matplotlib inline

## Example 4-1: Basic Teleportation

# Set up the program
#TASMIA
#Setup the registers and circuit
alice = QuantumRegister(1, name='alice')
ep    = QuantumRegister(1, name='ep')
bob   = QuantumRegister(1, name='bob')
alice_c = ClassicalRegister(1, name='alicec')
ep_c    = ClassicalRegister(1, name='epc')
bob_c   = ClassicalRegister(1, name='bobc')
qc = QuantumCircuit(alice, ep, bob, alice_c, ep_c, bob_c)

# entangle
# TASMIA
# Superposition and entanglement (bell pair)
qc.h(ep)
qc.cx(ep, bob)
qc.barrier()

# prep payload
# TASMIA
# Initialize the payload state
qc.reset(alice)
qc.h(alice)
qc.rz(math.radians(45), alice)
qc.h(alice)
qc.barrier()

# send
qc.cx(alice, ep)
qc.h(alice)
# TASMIA
# quantum to classical
qc.measure(alice, alice_c)
qc.measure(ep, ep_c)
qc.barrier()

# receive
#TASMIA
#classical to quantum
qc.x(bob).c_if(ep_c, 1)
qc.z(bob).c_if(alice_c, 1)

# verify
# TASMIA
# Verfication
qc.h(bob)
qc.rz(math.radians(-45), bob)
qc.h(bob)
# TASMIA
# Quantum to classical for measure
qc.measure(bob, bob_c)

## That's the program. Everything below runs and draws it.

backend = BasicAer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()

#TASMIA
#Classical post processing
counts = result.get_counts(qc)
print('counts:',counts)

outputstate = result.get_statevector(qc, decimals=3)
print(outputstate)
qc.draw()        # draw the circuit

