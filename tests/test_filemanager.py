from hydra import compose, initialize

from amlcs.utils.file_manager import FileManager as FM


def test_resolve_code(load_test_conf):
    file_manager = FM(load_test_conf.preprocessing)
    assert "t21_80_0.05_30" in str(file_manager.comp_model_path)


def test_resolve_custom_code():
    with initialize(version_base=None, config_path="../amlcs/conf"):
        # config is relative to a module
        cus_path = "preprocessing.code=custom_path"
        cfg = compose(config_name="test_conf", overrides=[cus_path])
        file_manager = FM(cfg.preprocessing)
        assert "custom_path" in str(file_manager.comp_model_path)


def test_create_exp_folders(load_test_conf, mocker):
    file_manager = FM(load_test_conf.preprocessing)
    path_mocker = mocker.patch("amlcs.utils.file_manager.Path.mkdir")
    file_manager._create_experiments_folder()
    path_mocker.assert_called_once()


def test_create_model_folders(load_test_conf, mocker):
    file_manager = FM(load_test_conf.preprocessing)
    path_mocker = mocker.patch("amlcs.utils.file_manager.Path.mkdir")
    file_manager._create_model_folders(10)
    assert path_mocker.call_count == 15


def test_copy_model(load_test_conf, mocker):
    res_name = load_test_conf.preprocessing.res_name
    file_manager = FM(load_test_conf.preprocessing)
    copy_mocker = mocker.patch("amlcs.utils.file_manager.shutil.copytree")
    file_manager._copy_model(res_name)
    copy_mocker.assert_called_once()


def test_set_exp_struc(load_test_conf, mocker):
    res_name = load_test_conf.preprocessing.res_name
    path_mocker = mocker.patch("amlcs.utils.file_manager.Path.mkdir")
    copy_mocker = mocker.patch("amlcs.utils.file_manager.shutil.copytree")
    file_manager = FM(load_test_conf.preprocessing)
    file_manager.set_experiment_structure(10, res_name)
    assert path_mocker.call_count == 16
    copy_mocker.assert_called_once()


def test_delete_model_folders(load_test_conf, mocker):
    rm_mocker = mocker.patch("amlcs.utils.file_manager.shutil.rmtree")
    file_manager = FM(load_test_conf.preprocessing)
    file_manager.delete_model_folders()
    assert rm_mocker.call_count == 3
