import pytest
from sample import config

@pytest.fixture
def user_conf():
    conf = config.Config()
    return conf


@pytest.mark.smoke
def test_create_config():
    """test config module works without errors"""
    with pytest.raises(TypeError):
        config.Config()


def test_create_config(user_conf):
    assert user_conf.config_type == 'user'
    assert user_conf.config_path.exists()


def test_data_has_params_key(user_conf):
    assert user_conf.data.get('params', None) is not None


def test_write_config(user_conf):
    user_conf.data['params']['test'] = 'test'
    
    assert user_conf