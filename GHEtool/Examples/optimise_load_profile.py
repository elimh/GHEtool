"""
This document is an example of load optimisation.
First an hourly profile is imported and a fixed borefield size is set.
Then, based on a load-duration curve, the heating and cooling load is altered in order to fit as much load as possible on the field.
The results are returned.

"""
import numpy as np

from GHEtool import *


def optimise():
    # initiate ground data
    data = GroundConstantTemperature(3, 10)

    # initiate borefield
    borefield = Borefield()

    # set ground data in borefield
    borefield.set_ground_parameters(data)

    # set Rb
    borefield.Rb = 0.12

    # set borefield
    borefield.create_rectangular_borefield(10, 10, 6, 6, 150, 1, 0.075)

    # load the hourly profile
    load = HourlyBuildingLoad(efficiency_heating=10 ** 6, efficiency_cooling=10 ** 6)
    load.load_hourly_profile("hourly_profile.csv", header=True, separator=";")

    # optimise the load for a 10x10 field (see data above) and a fixed depth of 150m.
    # first for an optimisation based on the power
    borefield.optimise_load_profile_power(building_load=load, depth=150)

    print(f'Max heating power (primary): {borefield.load.max_peak_extraction:,.0f}kW')
    print(f'Max cooling power (primary): {borefield.load.max_peak_injection:,.0f}kW')

    print(
        f'Total energy extracted from the borefield over simulation period: {np.sum(borefield.load.monthly_baseload_extraction_simulation_period):,.0f}MWh')
    print(
        f'Total energy injected in the borefield over simulation period): {np.sum(borefield.load.monthly_baseload_injection_simulation_period):,.0f}MWh')
    print('------------------------------------------------------------------------')
    borefield.calculate_temperatures(hourly=True)
    borefield.print_temperature_profile(plot_hourly=True)

    # first for an optimisation based on the energy
    borefield.optimise_load_profile_energy(building_load=load, depth=150)

    print(f'Max heating power (primary): {borefield.load.max_peak_extraction:,.0f}kW')
    print(f'Max cooling power (primary): {borefield.load.max_peak_injection:,.0f}kW')

    print(
        f'Total energy extracted from the borefield over simulation period: {np.sum(borefield.load.monthly_baseload_extraction_simulation_period):,.0f}MWh')
    print(
        f'Total energy injected in the borefield over simulation period): {np.sum(borefield.load.monthly_baseload_injection_simulation_period):,.0f}MWh')

    borefield.calculate_temperatures(hourly=True)
    borefield.print_temperature_profile(plot_hourly=True)


if __name__ == "__main__":  # pragma: no cover
    optimise()
