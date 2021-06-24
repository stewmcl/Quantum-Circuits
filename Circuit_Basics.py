import numpy as np
from qiskit import QuantumCircuit

#creation of a quantum circuit acting on a quantum register of three qubits
circ = QuantumCircuit(3)

#Applying a Hadamard gate on qubit 0, this places the qubit in superposition
circ.h(0)

#Add a controlled-Not operation (CNOT \ CX) gate on the control qubit 0 and targate bit 1.
#This puts the qubits in a Bell State
circ.cx(0, 1)

#Add a controlled-Not operation (CNOT \ CX) gate on the control qubit 0 and targate bit 2.
#This puts the qubits in a GHZ state.
circ.cx(0, 2)

#draws the circuit
#print(circ.draw('mpl'))
print(circ)
