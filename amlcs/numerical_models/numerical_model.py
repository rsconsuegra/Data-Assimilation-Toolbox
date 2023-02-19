class NumericalModel:
    def __init__(self, model_resolution: dict, variables_by_layers:dict) -> None:
        self.model_resolution:dict = model_resolution
        self.vars_by_layers:dict = variables_by_layers