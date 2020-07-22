"""Tests for the `cli` module."""

import pytest

from neo4j_api import cli


def test_main():
    """Basic CLI test."""
    assert cli.main([]) == 0


def test_show_help(capsys):
    """Shows help."""
    with pytest.raises(SystemExit):
        cli.main(["-h"])
    captured = capsys.readouterr()
    assert "neo4j-api" in captured.out
