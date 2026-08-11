import pytest

from eqd2_calculator.calculator import (
    calculate_bed,
    calculate_eqd2,
    calculate_total_dose,
)

# --------------------------------------------------
# Core scientific calculation tests
# --------------------------------------------------


def test_calculate_total_dose():
    result = calculate_total_dose(2.0, 25)

    assert result == 50.0


def test_calculate_bed():
    result = calculate_bed(2.0, 25, 10.0)

    assert result == pytest.approx(60.0)


def test_calculate_eqd2():
    bed = 60.0

    result = calculate_eqd2(bed, 10.0)

    assert result == pytest.approx(50.0)


def test_hdr_tumour_fractionation():
    total_dose = calculate_total_dose(8.0, 3)
    bed = calculate_bed(8.0, 3, 10.0)
    eqd2 = calculate_eqd2(bed, 10.0)

    assert total_dose == 24.0
    assert bed == pytest.approx(43.2)
    assert eqd2 == pytest.approx(36.0)


def test_hdr_late_responding_tissue():
    total_dose = calculate_total_dose(8.0, 3)
    bed = calculate_bed(8.0, 3, 3.0)
    eqd2 = calculate_eqd2(bed, 3.0)

    assert total_dose == 24.0
    assert bed == pytest.approx(88.0)
    assert eqd2 == pytest.approx(52.8)


# --------------------------------------------------
# Input validation tests
# --------------------------------------------------


@pytest.mark.parametrize("dose", [0, -1])
def test_rejects_non_positive_dose(dose):
    with pytest.raises(
        ValueError,
        match="Dose per fraction must be greater than 0",
    ):
        calculate_total_dose(dose, 25)


@pytest.mark.parametrize("fractions", [0, -1])
def test_rejects_non_positive_fraction_count(fractions):
    with pytest.raises(
        ValueError,
        match="Number of fractions must be greater than 0",
    ):
        calculate_total_dose(2, fractions)


@pytest.mark.parametrize("fractions", [2.5, "25", True])
def test_rejects_non_integer_fraction_count(fractions):
    with pytest.raises(
        TypeError,
        match="Number of fractions must be a whole number",
    ):
        calculate_total_dose(2, fractions)


@pytest.mark.parametrize("alpha_beta", [0, -3])
def test_rejects_non_positive_alpha_beta(alpha_beta):
    with pytest.raises(
        ValueError,
        match="Alpha/Beta must be greater than 0",
    ):
        calculate_bed(2, 25, alpha_beta)


@pytest.mark.parametrize(
    "invalid_value",
    [
        float("nan"),
        float("inf"),
        float("-inf"),
    ],
)
def test_rejects_non_finite_values(invalid_value):
    with pytest.raises(
        ValueError,
        match="Dose per fraction must be finite",
    ):
        calculate_total_dose(invalid_value, 25)


@pytest.mark.parametrize(
    "invalid_value",
    [
        "eight",
        "",
        None,
        True,
    ],
)
def test_rejects_non_numeric_dose(invalid_value):
    with pytest.raises(
        TypeError,
        match="Dose per fraction must be a valid number",
    ):
        calculate_total_dose(invalid_value, 3)