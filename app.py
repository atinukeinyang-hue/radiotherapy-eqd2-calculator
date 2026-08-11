import math

from eqd2_calculator.calculator import (
    calculate_bed,
    calculate_eqd2,
    calculate_total_dose,
)
from eqd2_calculator.cumulative import (
    calculate_cumulative_bed,
    calculate_cumulative_eqd2,
)
from eqd2_calculator.export import (
    CalculationRecord,
    create_calculation_record,
    export_calculation_to_csv,
    export_calculations_to_csv,
    export_calculations_to_excel,
)
from eqd2_calculator.presets import get_alpha_beta_preset


def read_positive_float(prompt: str) -> float:
    """Read a positive, finite decimal number."""

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
    """Read a positive whole number."""

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


def read_course_count() -> int:
    """Read a treatment-course count of at least two."""

    while True:
        number_of_courses = read_positive_integer(
            "Number of treatment courses: "
        )

        if number_of_courses < 2:
            print(
                "Error: Cumulative calculations require "
                "at least 2 treatment courses."
            )
            continue

        return number_of_courses


def select_alpha_beta() -> tuple[float, str]:
    """Select a preset or custom alpha/beta value."""

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


def display_single_course_results(
    dose_per_fraction: float,
    number_of_fractions: int,
    alpha_beta: float,
    preset_label: str,
) -> None:
    """Calculate and display one treatment course."""

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


def offer_result_export(
    records: list[CalculationRecord],
    file_name: str,
) -> None:
    """Offer CSV and Excel export options."""

    while True:
        print("\nExport Results")
        print("--------------")
        print("1. Export to CSV")
        print("2. Export to Excel")
        print("3. Export to both CSV and Excel")
        print("4. Do not export")

        choice = input("Select an option (1-4): ").strip()

        csv_path = f"outputs/{file_name}.csv"
        excel_path = f"outputs/{file_name}.xlsx"

        if choice == "1":
            if len(records) == 1:
                export_calculation_to_csv(
                    records[0],
                    csv_path,
                )
            else:
                export_calculations_to_csv(
                    records,
                    csv_path,
                )

            print(f"CSV file created: {csv_path}")
            return

        if choice == "2":
            export_calculations_to_excel(
                records,
                excel_path,
            )
            print(f"Excel file created: {excel_path}")
            return

        if choice == "3":
            if len(records) == 1:
                export_calculation_to_csv(
                    records[0],
                    csv_path,
                )
            else:
                export_calculations_to_csv(
                    records,
                    csv_path,
                )

            export_calculations_to_excel(
                records,
                excel_path,
            )

            print(f"CSV file created: {csv_path}")
            print(f"Excel file created: {excel_path}")
            return

        if choice == "4":
            print("Results were not exported.")
            return

        print("Error: Select option 1, 2, 3, or 4.")


def run_single_course_calculation() -> None:
    """Run a calculation for one fractionation course."""

    print("\nSingle Treatment Course")
    print("-----------------------")

    dose_per_fraction = read_positive_float(
        "Dose per fraction (Gy): "
    )

    number_of_fractions = read_positive_integer(
        "Number of fractions: "
    )

    alpha_beta, preset_label = select_alpha_beta()

    display_single_course_results(
        dose_per_fraction,
        number_of_fractions,
        alpha_beta,
        preset_label,
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

    record = create_calculation_record(
        component="Single Treatment Course",
        dose_per_fraction=dose_per_fraction,
        number_of_fractions=number_of_fractions,
        alpha_beta=alpha_beta,
        total_physical_dose=total_dose,
        bed=bed,
        eqd2=eqd2,
    )

    offer_result_export(
        records=[record],
        file_name="single_treatment_result",
    )


def run_cumulative_calculation() -> None:
    """Run a cumulative multi-course calculation."""

    print("\nCumulative Treatment Calculation")
    print("--------------------------------")
    print(
        "All courses must refer to the same tissue or "
        "biological endpoint."
    )

    number_of_courses = read_course_count()
    alpha_beta, preset_label = select_alpha_beta()

    courses: list[tuple[float, int]] = []

    for course_number in range(
        1,
        number_of_courses + 1,
    ):
        print(f"\nTreatment Course {course_number}")
        print("------------------")

        dose_per_fraction = read_positive_float(
            "Dose per fraction (Gy): "
        )

        number_of_fractions = read_positive_integer(
            "Number of fractions: "
        )

        courses.append(
            (
                dose_per_fraction,
                number_of_fractions,
            )
        )

    total_physical_dose = 0.0
    records: list[CalculationRecord] = []

    print("\nCourse Breakdown")
    print("----------------")

    for course_number, (
        dose_per_fraction,
        number_of_fractions,
    ) in enumerate(courses, start=1):
        course_physical_dose = calculate_total_dose(
            dose_per_fraction,
            number_of_fractions,
        )

        course_bed = calculate_bed(
            dose_per_fraction,
            number_of_fractions,
            alpha_beta,
        )

        course_eqd2 = calculate_eqd2(
            course_bed,
            alpha_beta,
        )

        total_physical_dose += course_physical_dose

        records.append(
            create_calculation_record(
                component=f"Treatment Course {course_number}",
                dose_per_fraction=dose_per_fraction,
                number_of_fractions=number_of_fractions,
                alpha_beta=alpha_beta,
                total_physical_dose=course_physical_dose,
                bed=course_bed,
                eqd2=course_eqd2,
            )
        )

        print(
            f"Course {course_number}: "
            f"{dose_per_fraction:g} Gy × "
            f"{number_of_fractions}"
        )
        print(
            f"  Physical dose: "
            f"{course_physical_dose:.2f} Gy"
        )
        print(
            f"  BED: {course_bed:.2f} "
            f"Gy{alpha_beta:g}"
        )
        print(f"  EQD2: {course_eqd2:.2f} Gy")

    cumulative_bed = calculate_cumulative_bed(
        courses,
        alpha_beta,
    )

    cumulative_eqd2 = calculate_cumulative_eqd2(
        courses,
        alpha_beta,
    )

    print("\nCumulative Results")
    print("------------------")
    print(f"Alpha/Beta selection: {preset_label}")
    print(f"Alpha/Beta value: {alpha_beta:.2f} Gy")
    print(
        f"Total physical dose: "
        f"{total_physical_dose:.2f} Gy"
    )
    print(
        f"Cumulative BED: "
        f"{cumulative_bed:.2f} Gy{alpha_beta:g}"
    )
    print(
        f"Cumulative EQD2: "
        f"{cumulative_eqd2:.2f} Gy"
    )

    records.append(
        {
            "component": "Cumulative Total",
            "dose_per_fraction_gy": "N/A",
            "number_of_fractions": "N/A",
            "alpha_beta_gy": alpha_beta,
            "total_physical_dose_gy": total_physical_dose,
            "bed_gy": cumulative_bed,
            "eqd2_gy": cumulative_eqd2,
        }
    )

    offer_result_export(
        records=records,
        file_name="cumulative_treatment_result",
    )


def display_main_menu() -> None:
    """Display the application menu."""

    print("\nMain Menu")
    print("---------")
    print("1. Single treatment course")
    print("2. Cumulative treatment courses")
    print("3. Exit")


def main() -> None:
    """Run the Radiotherapy BED/EQD2 Calculator."""

    print("Radiotherapy BED/EQD2 Calculator")
    print("--------------------------------")

    try:
        while True:
            display_main_menu()

            choice = input(
                "Select an option (1-3): "
            ).strip()

            if choice == "1":
                run_single_course_calculation()
                continue

            if choice == "2":
                run_cumulative_calculation()
                continue

            if choice == "3":
                print("\nCalculator closed.")
                break

            print("Error: Select option 1, 2, or 3.")

    except (KeyboardInterrupt, EOFError):
        print("\n\nCalculation cancelled safely.")


if __name__ == "__main__":
    main()