import pytest

import matplotlib.pyplot as plt
import numpy as np

from GHEtool import *


def test_main_functionalities(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.main_functionalities import main_functionalities
    main_functionalities()


def test_custom_borefield_configuration(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.custom_borefield_configuration import custom_borefield_configuration
    custom_borefield_configuration()


def test_effect_borehole_configuration(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.effect_of_borehole_configuration import effect_borefield_configuration
    effect_borefield_configuration()


@pytest.mark.slow
def test_sizing_with_Rb(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.sizing_with_Rb_calculation import sizing_with_Rb
    sizing_with_Rb()


@pytest.mark.slow
def test_active_passive(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.active_passive_cooling import active_passive_cooling
    active_passive_cooling(FOLDER.joinpath('Examples/active_passive_example.csv'))


def test_start_in_different_month(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.start_in_different_month import start_in_different_month
    start_in_different_month()


def test_multiple_ground_layers():
    from GHEtool.Examples.multiple_ground_layers import multiple_ground_layers
    multiple_ground_layers()


def test_sizing_with_building_load(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.sizing_with_building_load import size_with_scop, \
        size_with_variable_ground_temperature, \
        size_with_part_load_data
    assert np.allclose(size_with_scop(), (96.20571306433565, 4.072466974615784))
    assert np.allclose(size_with_variable_ground_temperature(), (95.29193738536698, 4.135572636533091))
    assert np.allclose(size_with_part_load_data(), (97.77220206543687, 4.627116806553787))


def test_sizing_with_building_load_hourly(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.sizing_with_building_load_hourly import L3_sizing, L4_sizing
    assert np.allclose(L3_sizing(), (128.1582605162373, 6.291201457558123))
    assert np.allclose(L4_sizing(), (153.87202254990598, 6.387747162165882))


def test_combined_active_and_passive_cooling(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.combined_active_and_passive_cooling import active_above_threshold, default_cooling_in_summer
    assert np.isclose(active_above_threshold(), 7483.480000000002)
    assert np.isclose(default_cooling_in_summer(), 67683.27999999997)


def test_separatus(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.separatus import design_with_single_U, design_with_double_U, design_with_separatus
    design_with_single_U()
    design_with_double_U()
    design_with_separatus()


def test_tilted(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.tilted_borefield import tilted
    tilted()


def test_optimise(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.optimise_load_profile import optimise
    optimise()


def test_temperature_dependent_fluid_data(monkeypatch):
    monkeypatch.setattr(plt, 'show', lambda: None)
    from GHEtool.Examples.temperature_dependent_fluid_data_sizing import size_with_temperature_dependence
    size_with_temperature_dependence()
