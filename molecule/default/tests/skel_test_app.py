import os

import testinfra.utils.ansible_runner

if "MOLECULE_INVENTORY_FILE" in os.environ:
    testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sshd_running_and_enabled(host):
    sshd = host.service("sshd")
    assert sshd.is_running
    assert sshd.is_enabled


def test_ssh_is_installed(host):
    openssh_server = host.package("openssh-server")
    assert openssh_server.is_installed


def test_ssh_is_listening(host):
    assert host.socket("tcp://0.0.0.0:22").is_listening
