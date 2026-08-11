import pytest

from app import (
    main,
    read_course_count,
    read_positive_float,
    read_positive_integer,
    select_alpha_beta,
)


def test_positive_float_retries_invalid_inputs(
    monkeypatch,
    capsys,
):
    inputs = iter(["abc", "-8", "nan", "8"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    result = read_positive_float("Dose per fraction: ")
    output = capsys.readouterr().out

    assert result == 8.0
    assert "Enter a valid number" in output
    assert "must be greater than 0" in output
    assert "must be finite" in output


def test_positive_integer_retries_invalid_inputs(
    monkeypatch,
    capsys,
):
    inputs = iter(["2.5", "0", "3"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    result = read_positive_integer(
        "Number of fractions: "
    )
    output = capsys.readouterr().out

    assert result == 3
    assert "Enter a valid whole number" in output
    assert "must be greater than 0" in output


def test_selects_tumour_preset(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1",
    )

    alpha_beta, label = select_alpha_beta()

    assert alpha_beta == 10.0
    assert label == "Tumour / early-responding tissue"


def test_selects_late_tissue_preset(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "2",
    )

    alpha_beta, label = select_alpha_beta()

    assert alpha_beta == 3.0
    assert label == "Late-responding normal tissue"


def test_accepts_custom_alpha_beta(monkeypatch):
    inputs = iter(["3", "4.5"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    alpha_beta, label = select_alpha_beta()

    assert alpha_beta == 4.5
    assert label == "Custom value"


@pytest.mark.parametrize(
    "invalid_choice",
    [
        "0",
        "4",
        "invalid",
        "",
    ],
)
def test_rejects_invalid_main_menu_option(
    monkeypatch,
    capsys,
    invalid_choice,
):
    inputs = iter([invalid_choice, "3"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main()

    output = capsys.readouterr().out

    assert "Error: Select option 1, 2, or 3." in output
    assert "Calculator closed" in output


def test_complete_cli_calculation(
    monkeypatch,
    capsys,
):
    inputs = iter(
        [
            "1",
            "8",
            "3",
            "1",
            "3",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main()

    output = capsys.readouterr().out

    assert "Alpha/Beta value: 10.00 Gy" in output
    assert "Total physical dose: 24.00 Gy" in output
    assert "BED: 43.20 Gy10" in output
    assert "EQD2: 36.00 Gy" in output
    assert "Calculator closed" in output


def test_course_count_requires_two_courses(
    monkeypatch,
    capsys,
):
    inputs = iter(["1", "2"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    result = read_course_count()
    output = capsys.readouterr().out

    assert result == 2
    assert "require at least 2 treatment courses" in output


def test_complete_cumulative_cli_calculation(
    monkeypatch,
    capsys,
):
    inputs = iter(
        [
            "2",
            "2",
            "1",
            "1.8",
            "25",
            "8",
            "3",
            "3",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main()

    output = capsys.readouterr().out

    assert "Course 1: 1.8 Gy × 25" in output
    assert "Course 2: 8 Gy × 3" in output
    assert "Total physical dose: 69.00 Gy" in output
    assert "Cumulative BED: 96.30 Gy10" in output
    assert "Cumulative EQD2: 80.25 Gy" in output
    assert "Calculator closed" in output