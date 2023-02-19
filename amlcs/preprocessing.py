"""Module which controls the pre-processing of a data assimilation model."""
from typing import Dict

import hydra
from omegaconf import DictConfig, OmegaConf

from amlcs import log
from amlcs.numerical_models.numerical_model import NumericalModel as NM
from amlcs.utils.file_manager import FileManager as FM


@hydra.main(version_base="1.2", config_path="conf", config_name="conf_pre")
def main(cfg: DictConfig) -> None:
    """Driver for pre-processing."""
    prepro = Preprocessing(cfg)
    prepro.set_experiments_files()
    prepro.set_numerical_model()


class Preprocessing:
    """Class that defines the Data Assimilatio Pre-Processing for the model."""

    def __init__(self, cfg: DictConfig) -> None:
        """Model initialization for preprocessing. This sets the model configurations.

        Args:
            cfg (_type_): Hydra configuration file, containing model parameters.

        """
        self.pre_cfg: DictConfig = cfg.preprocessing
        self.res_size: Dict = cfg.model_res.get(self.pre_cfg.res_name)
        self.res_vars: Dict = cfg.model_res.get("variables")
        log.debug("%s resolution will be used", self.pre_cfg.res_name.upper())
        log.debug("Parameters: %s", OmegaConf.to_yaml(self.pre_cfg))

    def set_experiments_files(self) -> None:
        """Create all folders required for experimentation."""
        file_manager = FM(self.pre_cfg)
        file_manager.set_experiment_structure(self.pre_cfg.Nens, self.pre_cfg.res_name)

    def set_numerical_model(self) -> None:
        """Create numerical model."""
        numerical_model = NM(self.res_size, self.res_vars)
        log.info(numerical_model.vars_by_layers)


if __name__ == "__main__":
    main()
