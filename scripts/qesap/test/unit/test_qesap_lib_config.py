import pytest
import re
from lib.config import yaml_to_tfvars


@pytest.fixture()
def config_data_sample():
    """
    create yaml config data sample with one string, list and dict variable.
    :return:
    dict based data structure
    """
    config = {'name': 'geppetto',
              'terraform': {
                  'provider': 'azure',
                  'variables': {
                      'az_region': 'westeurope',
                      'hana_ips': ["10.0.0.2", "10.0.0.3"],
                      'hana_data_disks_configuration': {
                          'disk_type': 'hdd,hdd,hdd',
                          'disks_size': '64,64,64'
                      }
                  }
                }
              }

    return config


def test_tfvars_yaml_string(config_data_sample):
    """
    Check string based variable format tfvars output
    :param config_data_sample:
    input similar to yaml config file
    :return:
    true or false
    """
    expected_result = r'az_region = \"westeurope\"'
    actual_result = yaml_to_tfvars(config_data_sample)
    assert re.search(expected_result, actual_result)


def test_tfvars_yaml_list(config_data_sample):
    """
    Check list based variable format tfvars output
    :param config_data_sample:
    input similar to yaml config file
    :return:
    true or false
    """
    expected_result = r'hana_ips = \["10.0.0.2", "10.0.0.3"]'
    actual_result = yaml_to_tfvars(config_data_sample)
    assert re.search(expected_result, actual_result)


def test_tfvars_yaml_dict(config_data_sample):
    """
    Check dict based variable format tfvars output
    :param config_data_sample:
    :return:
    """
    expected_result = r'hana_data_disks_configuration = {' \
                      r'(\s|\t)+disk_type = "hdd,hdd,hdd"' \
                      r'(\s|\t)+disks_size = "64,64,64"'
    actual_result = yaml_to_tfvars(config_data_sample)
    assert re.search(expected_result, actual_result)
