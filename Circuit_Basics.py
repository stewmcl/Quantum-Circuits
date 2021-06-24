import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def basic_circuit():
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
    return circ

def simulating_circuits(circ):
    #setting the initial state of the simulator to the ground state using from_int
    state = Statevector.from_int(0, 2**3)

    #evolve the state by the quantum circuit
    state = state.evolve(circ)


def main():
    circ = basic_circuit()
    sleep(1)
    simulating_circuits(circ)

if __name__ == "__main__":
    main()
