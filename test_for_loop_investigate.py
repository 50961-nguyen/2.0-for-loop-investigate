import runpy

import pytest


@pytest.fixture
def sections(capsys):
    runpy.run_path("for_loop_investigate.py")
    out = capsys.readouterr().out
    return [s.split() for s in out.split("-" * 10)]


def get(sections, n):
    assert len(sections) > n, f"Section {n + 1} is missing. Keep the separator prints."
    return sections[n]


def test_corn(sections):
    assert get(sections, 0) == ["I", "love", "corn."] * 7, "Print 'I love corn.' 7 times"


def test_1_to_20(sections):
    assert get(sections, 1) == [str(i) for i in range(1, 21)], "Print numbers from 1 to 20"


def test_odds(sections):
    assert get(sections, 2) == [str(i) for i in range(1, 101, 2)], "Print odd numbers from 1 to 100"


def test_20_down_to_1(sections):
    assert get(sections, 3) == [str(i) for i in range(20, 0, -1)], "Print numbers from 20 down to 1"


def test_cubes(sections):
    assert get(sections, 4) == [str(i**3) for i in range(1, 11)], "Print cubes from 1 to 10"


def test_every_10th(sections):
    assert get(sections, 5) == [str(i) for i in range(0, 101, 10)], "Print every 10th number from 0 to 100"
