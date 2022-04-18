import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('svc', [
  'slapd'
])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled


# def test_yaf_version(host):
#     version = "2.12.1"
#     command = """PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig pkg-config \
#                  --modversion libyaf"""
#     cmd = host.run(command)

#     assert version in cmd.stdout