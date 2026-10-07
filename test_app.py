"""Tests run locally and by the CircleCI test job."""

import pytest

from app import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (0, 6, 6),
        (6, 0, 6),
        (-2, -3, -5),
        (-10, 4, -6),
        (10**18, 1, 10**18 + 1),
    ],
)
def test_add_integers(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [(0.1, 0.2, 0.3), (1.5, 2.25, 3.75), (-0.5, 0.5, 0.0)],
)
def test_add_floats(a, b, expected):
    assert add(a, b) == pytest.approx(expected)
