import pytest

from eqd2_calculator.calculator import (
    calculate_bed,
    calculate_eqd2,
    calculate_total_dose,
)


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