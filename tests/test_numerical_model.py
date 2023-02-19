from amlcs.numerical_models.numerical_model import NumericalModel as NM

model_res = {"lat": 80, "lon": 40}
vars_by_layers = {"PSG0": 8}


def test_set_time_integration():
    num_model = NM(model_resolution=model_res, variables_by_layers=vars_by_layers)
    nmon, days, res = num_model.set_time_integration([2, 3, 4])
    assert nmon == 2 and days == 3 and res == 4
