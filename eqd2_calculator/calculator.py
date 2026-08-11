def calculate_total_dose(
    dose_per_fraction: float,
    number_of_fractions: int,
) -> float:
    """Calculate the total physical radiation dose."""

    if dose_per_fraction <= 0:
        raise ValueError("Dose per fraction must be greater than 0.")

    if number_of_fractions <= 0:
        raise ValueError("Number of fractions must be greater than 0.")

    return dose_per_fraction * number_of_fractions


def calculate_bed(
    dose_per_fraction: float,
    number_of_fractions: int,
    alpha_beta: float,
) -> float:
    """Calculate biologically effective dose (BED)."""

    if dose_per_fraction <= 0:
        raise ValueError("Dose per fraction must be greater than 0.")

    if number_of_fractions <= 0:
        raise ValueError("Number of fractions must be greater than 0.")

    if alpha_beta <= 0:
        raise ValueError("Alpha/Beta must be greater than 0.")

    total_dose = dose_per_fraction * number_of_fractions

    bed = total_dose * (
        1 + dose_per_fraction / alpha_beta
    )

    return bed


def calculate_eqd2(
    bed: float,
    alpha_beta: float,
) -> float:
    """Convert BED to equivalent dose in 2 Gy fractions."""

    if bed <= 0:
        raise ValueError("BED must be greater than 0.")

    if alpha_beta <= 0:
        raise ValueError("Alpha/Beta must be greater than 0.")

    eqd2 = bed / (
        1 + 2 / alpha_beta
    )

    return eqd2