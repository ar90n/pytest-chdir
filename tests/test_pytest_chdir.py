import os
import pytest
from pathlib import Path
from pytest_chdir import define_chdir_fixture

define_chdir_fixture("chroot", Path("/"), __name__)


def test_chtmpdir(chtmpdir):
    assert os.getcwd() == chtmpdir


def test_chdatadir(chdatadir):
    assert os.getcwd() == str(chdatadir)


def test_chshared_datadir(chshared_datadir):
    assert os.getcwd() == str(chshared_datadir)


def test_chroot(chroot):
    assert os.getcwd() == "/"
