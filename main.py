from basics.qubit import basic_circuit
from basics.not_circuit import not_circuit
from qvm.weber import weber, PROCESSOR_ID, NUM_SIMULATIONS

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
                        help=("Should the results be printed to console"))

    args = parser.parse_args()
    return args

def main():

    args = parse_arguments()

    circuit = basic_circuit()
    not_cir = not_circuit()
    simulation_engine = weber()

    samples = simulation_engine.get_sampler(PROCESSOR_ID).run(
        circuit, repetitions=NUM_SIMULATIONS)

    if args.debug:
        print("Sqrt Results: {}".format(samples))
    cirq.plot_state_histogram(samples, plt.subplot(), title="Sqrt Results")
    plt.show()

    ## NOT Circuit
    samples = simulation_engine.get_sampler(PROCESSOR_ID).run(
    not_cir, repetitions=NUM_SIMULATIONS)

    if args.debug:
        print("NOT Results: {}".format(samples))
    cirq.plot_state_histogram(samples, plt.subplot(), title="NOT Results")
    plt.show()


if __name__ == "__main__":
    main()
