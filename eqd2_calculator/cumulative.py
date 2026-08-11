from collections.abc import Sequence

from eqd2_calculator.calculator import (
    calculate_bed,
    calculate_eqd2,
)


def calculate_cumulative_bed(
    courses: Sequence[tuple[float, int]],
    alpha_beta: float,
) -> float:
    """Calculate cumulative BED for multiple treatment courses."""

    if not courses:
        raise ValueError(
            "At least one treatment course is required."
        )

    cumulative_bed = 0.0

    for dose_per_fraction, number_of_fractions in courses:
        course_bed = calculate_bed(
            dose_per_fraction,
            number_of_fractions,
            alpha_beta,
        )

        cumulative_bed += course_bed

    return cumulative_bed


def calculate_cumulative_eqd2(
    courses: Sequence[tuple[float, int]],
    alpha_beta: float,
) -> float:
    """Calculate cumulative EQD2 for multiple treatment courses."""

    cumulative_bed = calculate_cumulative_bed(
        courses,
        alpha_beta,
    )

    return calculate_eqd2(
        cumulative_bed,
        alpha_beta,
    )