# Google Quantum computer library
import cirq
import cirq_google
import qsimcirq
# Argument parsing
import argparse
# Plotting results
import matplotlib.pyplot as plt

PROCESSOR_ID = "weber"
NUM_SIMULATIONS = 10000


def weber():
    calibration_noise = cirq_google.engine.load_median_device_calibration(
        PROCESSOR_ID)

    noise_properties = cirq_google.noise_properties_from_calibration(
        calibration_noise)

    noise_model = cirq_google.NoiseModelFromGoogleNoiseProperties(
        noise_properties)

    simulator = qsimcirq.QSimSimulator(noise=noise_model)

    device = cirq_google.engine.create_device_from_processor_id(PROCESSOR_ID)

    virtual_processor = cirq_google.engine.SimulatedLocalProcessor(
        processor_id=PROCESSOR_ID, sampler=simulator, device=device, calibrations={calibration_noise.timestamp // 1000: calibration_noise})

    simulation_engine = cirq_google.engine.SimulatedLocalEngine([
        virtual_processor])

    print("Quantum Virtual Machine {} is ready! QBit grid: {}".format(
        PROCESSOR_ID, simulation_engine.get_processor(PROCESSOR_ID).get_device()))
    return simulation_engine
