import pytest

from eqd2_calculator.cumulative import (
    calculate_cumulative_bed,
    calculate_cumulative_eqd2,
)

EBRT_AND_HDR_COURSES = [
    (1.8, 25),
    (8.0, 3),
]


def test_cumulative_tumour_bed():
    result = calculate_cumulative_bed(
        EBRT_AND_HDR_COURSES,
        10.0,
    )

    assert result == pytest.approx(96.3)


def test_cumulative_tumour_eqd2():
    result = calculate_cumulative_eqd2(
        EBRT_AND_HDR_COURSES,
        10.0,
    )

    assert result == pytest.approx(80.25)


def test_cumulative_late_tissue_bed():
    result = calculate_cumulative_bed(
        EBRT_AND_HDR_COURSES,
        3.0,
    )

    assert result == pytest.approx(160.0)


def test_cumulative_late_tissue_eqd2():
    result = calculate_cumulative_eqd2(
        EBRT_AND_HDR_COURSES,
        3.0,
    )

    assert result == pytest.approx(96.0)


def test_rejects_empty_course_collection():
    with pytest.raises(
        ValueError,
        match="At least one treatment course is required",
    ):
        calculate_cumulative_bed([], 10.0)


def test_rejects_invalid_course_values():
    invalid_courses = [
        (0.0, 25),
        (8.0, 3),
    ]

    with pytest.raises(
        ValueError,
        match="Dose per fraction must be greater than 0",
    ):
        calculate_cumulative_bed(
            invalid_courses,
            10.0,
        )