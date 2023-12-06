# Google Quantum computer library
import cirq
# Argument parsing
import argparse
# Plotting results
import matplotlib.pyplot as plt


# Parse for user arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Basic QBbit Program")
    parser.add_argument('-d', '--debug', default=False, action='store_true',
                        help=("Should the simulation access the waveform"))

    args = parser.parse_args()
    return args


def basic_circuit():
    # Set a qubit
    qubit = cirq.GridQubit(4, 5)

    # Generate a circuit
    circuit = cirq.Circuit(cirq.X(qubit)**0.5, cirq.measure(qubit, key="m"))
    return circuit

def main():

    # Get the results of user arguments
    args = parse_arguments()

    circuit = basic_circuit()
    print("Circuit: {}".format(circuit))

    # Create a basic noiseless simulator
    simulator = cirq.Simulator()

    # If debugging
    if args.debug:
        results = simulator.simulate(circuit)
        print("Debug Results: {}".format(results))
    # Else running on hardware
    else:
        samples = simulator.run(circuit, repetitions=20)
        print("Run Results: {}".format(samples))
        cirq.plot_state_histogram(samples, plt.subplot())
        plt.show()


if __name__ == "__main__":
    main()
