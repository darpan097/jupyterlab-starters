"""Is metadata reported properly."""

# pylint: disable=protected-access
import jupyter_starters


def test_labextenions_paths():
    """Does it report the right number of labextensions?"""
    paths = jupyter_starters._jupyter_labextension_paths()
    assert len(paths) == 1


def test_serverextenions_paths():
    """Does it report the right number of serverextensions?"""
    paths = jupyter_starters._jupyter_server_extension_paths()
    assert len(paths) == 1


def test_version():
    """Does it have a version?"""
    assert jupyter_starters.__version__
