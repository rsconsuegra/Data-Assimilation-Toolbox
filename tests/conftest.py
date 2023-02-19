import pytest
from hydra import compose, initialize
from omegaconf import DictConfig


@pytest.fixture(autouse=True)
def load_test_conf() -> DictConfig:
    with initialize(version_base=None, config_path="../amlcs/conf"):
        # config is relative to a module
        cfg = compose(config_name="test_conf")
        return cfg
