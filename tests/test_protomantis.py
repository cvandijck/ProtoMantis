import pytest
import subprocess


@pytest.mark.console
def test_console_help():
    """Calls help file of console script and tests for failure"""
    process = subprocess.run(['protomantis', '--help'], capture_output=True, universal_newlines=True)
    assert process.returncode == 0, process.stderr


@pytest.mark.console
def test_console_noargs():
    """Runs console without arguments expecting to fail"""
    process = subprocess.run(['protomantis', ], capture_output=True, universal_newlines=True)
    assert process.returncode == 2, process.stderr
