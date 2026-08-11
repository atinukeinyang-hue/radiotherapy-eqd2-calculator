import math
from numbers import Integral, Real


def _validate_positive_number(
    value: Real,
    parameter_name: str,
) -> None:
    """Validate that a value is a positive, finite number."""

    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(
            f"{parameter_name} must be a valid number."
        )

    if not math.isfinite(float(value)):
        raise ValueError(
            f"{parameter_name} must be finite."
        )

    if value <= 0:
        raise ValueError(
            f"{parameter_name} must be greater than 0."
        )


def _validate_positive_integer(
    value: Integral,
    parameter_name: str,
) -> None:
    """Validate that a value is a positive integer."""

    if isinstance(value, bool) or not isinstance(value, Integral):
        raise TypeError(
            f"{parameter_name} must be a whole number."
        )

    if value <= 0:
        raise ValueError(
            f"{parameter_name} must be greater than 0."
        )


def calculate_total_dose(
    dose_per_fraction: float,
    number_of_fractions: int,
) -> float:
    """Calculate the total physical radiation dose."""

    _validate_positive_number(
        dose_per_fraction,
        "Dose per fraction",
    )

    _validate_positive_integer(
        number_of_fractions,
        "Number of fractions",
    )

    return float(dose_per_fraction * number_of_fractions)


def calculate_bed(
    dose_per_fraction: float,
    number_of_fractions: int,
    alpha_beta: float,
) -> float:
    """Calculate the biologically effective dose (BED)."""

    _validate_positive_number(
        dose_per_fraction,
        "Dose per fraction",
    )

    _validate_positive_integer(
        number_of_fractions,
        "Number of fractions",
    )

    _validate_positive_number(
        alpha_beta,
        "Alpha/Beta",
    )

    total_dose = dose_per_fraction * number_of_fractions

    bed = total_dose * (
        1 + dose_per_fraction / alpha_beta
    )

    return float(bed)


def calculate_eqd2(
    bed: float,
    alpha_beta: float,
) -> float:
    """Convert BED to equivalent dose in 2 Gy fractions."""

    _validate_positive_number(
        bed,
        "BED",
    )

    _validate_positive_number(
        alpha_beta,
        "Alpha/Beta",
    )

    eqd2 = bed / (
        1 + 2 / alpha_beta
    )

    return float(eqd2)