import pytest

from eqd2_calculator.calculator import (
    calculate_bed,
    calculate_eqd2,
    calculate_total_dose,
)
from eqd2_calculator.cumulative import (
    calculate_cumulative_bed,
    calculate_cumulative_eqd2,
)


def test_conventional_fractionation_reference_case() -> None:
    """Verify 2 Gy × 25 fractions using an alpha/beta of 10 Gy."""

    dose_per_fraction = 2.0
    number_of_fractions = 25
    alpha_beta = 10.0

    total_dose = calculate_total_dose(
        dose_per_fraction,
        number_of_fractions,
    )
    bed = calculate_bed(
        dose_per_fraction,
        number_of_fractions,
        alpha_beta,
    )
    eqd2 = calculate_eqd2(
        bed,
        alpha_beta,
    )

    assert total_dose == pytest.approx(50.0)
    assert bed == pytest.approx(60.0)
    assert eqd2 == pytest.approx(50.0)


def test_hdr_tumour_reference_case() -> None:
    """Verify 8 Gy × 3 fractions using an alpha/beta of 10 Gy."""

    dose_per_fraction = 8.0
    number_of_fractions = 3
    alpha_beta = 10.0

    total_dose = calculate_total_dose(
        dose_per_fraction,
        number_of_fractions,
    )
    bed = calculate_bed(
        dose_per_fraction,
        number_of_fractions,
        alpha_beta,
    )
    eqd2 = calculate_eqd2(
        bed,
        alpha_beta,
    )

    assert total_dose == pytest.approx(24.0)
    assert bed == pytest.approx(43.2)
    assert eqd2 == pytest.approx(36.0)


def test_hdr_late_tissue_reference_case() -> None:
    """Verify 8 Gy × 3 fractions using an alpha/beta of 3 Gy."""

    dose_per_fraction = 8.0
    number_of_fractions = 3
    alpha_beta = 3.0

    total_dose = calculate_total_dose(
        dose_per_fraction,
        number_of_fractions,
    )
    bed = calculate_bed(
        dose_per_fraction,
        number_of_fractions,
        alpha_beta,
    )
    eqd2 = calculate_eqd2(
        bed,
        alpha_beta,
    )

    assert total_dose == pytest.approx(24.0)
    assert bed == pytest.approx(88.0)
    assert eqd2 == pytest.approx(52.8)


def test_ebrt_and_hdr_tumour_reference_case() -> None:
    """Verify cumulative EBRT and HDR using alpha/beta 10 Gy."""

    courses = [
        (1.8, 25),
        (8.0, 3),
    ]
    alpha_beta = 10.0

    total_physical_dose = sum(
        calculate_total_dose(
            dose_per_fraction,
            number_of_fractions,
        )
        for dose_per_fraction, number_of_fractions in courses
    )
    cumulative_bed = calculate_cumulative_bed(
        courses,
        alpha_beta,
    )
    cumulative_eqd2 = calculate_cumulative_eqd2(
        courses,
        alpha_beta,
    )

    assert total_physical_dose == pytest.approx(69.0)
    assert cumulative_bed == pytest.approx(96.3)
    assert cumulative_eqd2 == pytest.approx(80.25)


def test_ebrt_and_hdr_late_tissue_reference_case() -> None:
    """Verify cumulative EBRT and HDR using alpha/beta 3 Gy."""

    courses = [
        (2.0, 25),
        (8.0, 3),
    ]
    alpha_beta = 3.0

    total_physical_dose = sum(
        calculate_total_dose(
            dose_per_fraction,
            number_of_fractions,
        )
        for dose_per_fraction, number_of_fractions in courses
    )
    cumulative_bed = calculate_cumulative_bed(
        courses,
        alpha_beta,
    )
    cumulative_eqd2 = calculate_cumulative_eqd2(
        courses,
        alpha_beta,
    )

    assert total_physical_dose == pytest.approx(74.0)
    assert cumulative_bed == pytest.approx(171.3333333333)
    assert cumulative_eqd2 == pytest.approx(102.8)