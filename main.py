from basics.qubit import basic_circuit
from qvm.weber import weber, PROCESSOR_ID, NUM_SIMULATIONS

# Google Quantum computer library
import cirq
# Argument parsing
import argparse
# Plotting results
import matplotlib.pyplot as plt


def main():

    circuit = basic_circuit()
    simulation_engine = weber()

    samples = simulation_engine.get_sampler(PROCESSOR_ID).run(
        circuit, repetitions=NUM_SIMULATIONS)

    print("Run Results: {}".format(samples))
    cirq.plot_state_histogram(samples, plt.subplot())
    plt.show()


if __name__ == "__main__":
    main()
