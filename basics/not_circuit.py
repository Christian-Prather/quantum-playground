import cirq 

def not_circuit():
    # Use a 4,5 qbit grid  so its compatible with a QVM
    qbit = cirq.GridQubit(4,5)

    circuit = cirq.Circuit(cirq.X(qbit), cirq.measure(qbit, key='m'))

    return circuit
