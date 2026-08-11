from eqd2_calculator.calculator import (
    calculate_bed,
    calculate_eqd2,
    calculate_total_dose,
)


def main() -> None:
    print("Radiotherapy BED/EQD2 Calculator")
    print("--------------------------------")

    try:
        dose_per_fraction = float(
            input("Dose per fraction (Gy): ")
        )

        number_of_fractions = int(
            input("Number of fractions: ")
        )

        alpha_beta = float(
            input("Alpha/Beta (Gy): ")
        )

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
        print(f"Total physical dose: {total_dose:.2f} Gy")
        print(f"BED: {bed:.2f} Gy")
        print(f"EQD2: {eqd2:.2f} Gy")

    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()