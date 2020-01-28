import os
import pytest
from pathlib import Path
import pytest_chdir

pytest_chdir.inject_chdir_fixture("chroot", Path("/"), globals())


def test_chtmpdir(chtmpdir):
    assert os.getcwd() == chtmpdir


def test_chdatadir(chdatadir):
    assert os.getcwd() == str(chdatadir)


def test_chshared_datadir(chshared_datadir):
    assert os.getcwd() == str(chshared_datadir)


def test_chroot(chroot):
    assert os.getcwd() == "/"
