"""Regression contract for the controlled Super-agent integration experiment."""

import pytest

import click
from click.testing import CliRunner


@pytest.mark.parametrize("value", [None, False, 0, "", [], {}, "Hello, World!"])
def test_preserve_callback_return_value(value):
    @click.command()
    def cli():
        click.echo("ok")
        return value

    result = CliRunner().invoke(cli, standalone_mode=False)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.output == "ok\n"
    assert result.return_value is value


def test_default_standalone_mode_returns_none():
    @click.command()
    def cli():
        return "Hello, World!"

    result = CliRunner().invoke(cli)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.return_value is None
