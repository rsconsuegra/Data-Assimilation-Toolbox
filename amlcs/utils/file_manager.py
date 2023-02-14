"""Module that manages all logic related to file managment."""
import shutil
from pathlib import Path

from omegaconf import DictConfig

from amlcs import MODEL_PATH, RESULTS_FOLDER, log


class FileManager:
    """Class that manages all logic related to folder creations."""

    def __init__(self, pre_cfg: DictConfig) -> None:
        """Class that creates foldes for each data assimilation step."""
        self.comp_model_path: Path = RESULTS_FOLDER / self._resolve_code_path(pre_cfg)
        self.snapshots = self.comp_model_path / "snapshots"
        self.ensemble_0 = self.comp_model_path / "ensemble_0"
        self.source_model_local = self.comp_model_path / "source_local"
        self.free_run = self.comp_model_path / "free_run"
        self.init_cond = self.comp_model_path / "initial_condition"
        self.model_local = self.comp_model_path / "model_local"

    def _resolve_code_path(self, pre_cfg: DictConfig) -> str:
        """Resolve the preprocessing code to be used: Default or a custom location.

        Returns
        -------
        str
            Path of preprocessing code.

        """
        code_path: str = ""
        if pre_cfg.code:
            code_path = pre_cfg.code
            log.debug("Custom code path set")
        else:
            res_ens = f"{pre_cfg.res_name}_{pre_cfg.Nens}"
            per_m = f"{pre_cfg.per}_{pre_cfg.M}"
            code_path = f"{res_ens}_{per_m}"
            log.debug("Default code path used")
        path: str = f"{pre_cfg.folder_prep}/{code_path}"
        return path

    def set_experiment_structure(self, num_of_ens: int, res_name: str) -> None:
        """Create experiment's foledr structure and copy model."""
        self.create_experiments_folder()
        self.create_model_folders(num_of_ens)
        self.copy_model(res_name)
        log.info("Model copied")

    def create_experiments_folder(self) -> None:
        """Create folder structure for experiment.

        This method creates the root folders required to perform
        multiple data assimilation experiments using the same model
        under the same configurations. This structure contains a "main folder"
        which refeers to a topic, if not created previosly.
        Multiple model configurations can be performed under the same "main folder"
        (for example, a paper with multiple runs).
        """
        self.comp_model_path.mkdir(parents=True, exist_ok=True)
        log.info("%s folder created", self.comp_model_path)

    def create_model_folders(self, num_of_ens: int) -> None:
        """Create folders for data assimilation under the experiment path.

        Parameters
        ----------
        num_of_ens : int
            Number of ensemble members

        """
        log.info("Creating folders")
        self.snapshots.mkdir(exist_ok=True)
        self.ensemble_0.mkdir(exist_ok=True)
        self.free_run.mkdir(exist_ok=True)
        self.init_cond.mkdir(exist_ok=True)
        self.model_local.mkdir(exist_ok=True)

        for ensemble in range(num_of_ens):
            (self.ensemble_0 / f"ens_{ensemble}").mkdir(exist_ok=True)
        log.info("Model folders created")

    def copy_model(self, res_name: str) -> None:
        """Copy model to data assimilation manipulation."""
        log.info("Copying model")
        res_model = MODEL_PATH / res_name
        shutil.copytree(res_model, self.source_model_local, dirs_exist_ok=True)

    def delte_model_folders(self) -> None:
        """Delete folders relative to the model."""
        shutil.rmtree(self.ensemble_0)
        shutil.rmtree(self.source_model_local)
        shutil.rmtree(self.model_local)
