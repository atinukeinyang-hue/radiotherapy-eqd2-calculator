import math

from eqd2_calculator.calculator import (
    calculate_bed,
    calculate_eqd2,
    calculate_total_dose,
)
from eqd2_calculator.presets import get_alpha_beta_preset


def read_positive_float(prompt: str) -> float:
    """Read a positive, finite decimal number from the user."""

    while True:
        raw_value = input(prompt).strip()

        if not raw_value:
            print("Error: A value is required.")
            continue

        try:
            value = float(raw_value)
        except ValueError:
            print("Error: Enter a valid number.")
            continue

        if not math.isfinite(value):
            print("Error: The value must be finite.")
            continue

        if value <= 0:
            print("Error: The value must be greater than 0.")
            continue

        return value


def read_positive_integer(prompt: str) -> int:
    """Read a positive whole number from the user."""

    while True:
        raw_value = input(prompt).strip()

        if not raw_value:
            print("Error: A value is required.")
            continue

        try:
            value = int(raw_value)
        except ValueError:
            print("Error: Enter a valid whole number.")
            continue

        if value <= 0:
            print("Error: The value must be greater than 0.")
            continue

        return value


def select_alpha_beta() -> tuple[float, str]:
    """Allow the user to select a preset or custom alpha/beta value."""

    while True:
        print("\nAlpha/Beta Selection")
        print("--------------------")
        print("1. Tumour / early-responding tissue (10 Gy)")
        print("2. Late-responding normal tissue (3 Gy)")
        print("3. Enter a custom alpha/beta value")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            return (
                get_alpha_beta_preset("tumour"),
                "Tumour / early-responding tissue",
            )

        if choice == "2":
            return (
                get_alpha_beta_preset("late_tissue"),
                "Late-responding normal tissue",
            )

        if choice == "3":
            custom_value = read_positive_float(
                "Custom Alpha/Beta (Gy): "
            )

            return custom_value, "Custom value"

        print("Error: Select option 1, 2, or 3.")


def ask_to_continue() -> bool:
    """Ask whether the user wants another calculation."""

    while True:
        response = input(
            "\nPerform another calculation? (y/n): "
        ).strip().lower()

        if response in {"y", "yes"}:
            return True

        if response in {"n", "no"}:
            return False

        print("Error: Enter y or n.")


def main() -> None:
    """Run the Radiotherapy BED/EQD2 Calculator."""

    print("Radiotherapy BED/EQD2 Calculator")
    print("--------------------------------")

    try:
        while True:
            dose_per_fraction = read_positive_float(
                "\nDose per fraction (Gy): "
            )

            number_of_fractions = read_positive_integer(
                "Number of fractions: "
            )

            alpha_beta, preset_label = select_alpha_beta()

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

            print("\nResults")
            print("-------")
            print(f"Alpha/Beta selection: {preset_label}")
            print(f"Alpha/Beta value: {alpha_beta:.2f} Gy")
            print(f"Total physical dose: {total_dose:.2f} Gy")
            print(f"BED: {bed:.2f} Gy{alpha_beta:g}")
            print(f"EQD2: {eqd2:.2f} Gy")

            if not ask_to_continue():
                print("\nCalculator closed.")
                break

    except (KeyboardInterrupt, EOFError):
        print("\n\nCalculation cancelled safely.")


if __name__ == "__main__":
    main()