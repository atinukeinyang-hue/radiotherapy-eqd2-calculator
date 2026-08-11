"""Utilities for preparing and exporting radiotherapy calculation results."""

import csv
from pathlib import Path
from typing import TypeAlias


from openpyxl import Workbook


CalculationRecord: TypeAlias = dict[str, str | int | float]


def create_calculation_record(
    component: str,
    dose_per_fraction: float,
    number_of_fractions: int,
    alpha_beta: float,
    total_physical_dose: float,
    bed: float,
    eqd2: float,
) -> CalculationRecord:
    """Create a structured record for one radiotherapy component.

    Args:
        component: Name of the treatment component, such as EBRT or
            Brachytherapy.
        dose_per_fraction: Dose delivered in each fraction, in Gy.
        number_of_fractions: Total number of treatment fractions.
        alpha_beta: Alpha/beta ratio used in the calculation, in Gy.
        total_physical_dose: Total physical dose, in Gy.
        bed: Biologically effective dose.
        eqd2: Equivalent dose in 2 Gy fractions.

    Returns:
        A dictionary containing the calculation inputs and results.
    """
    return {
        "component": component,
        "dose_per_fraction_gy": dose_per_fraction,
        "number_of_fractions": number_of_fractions,
        "alpha_beta_gy": alpha_beta,
        "total_physical_dose_gy": total_physical_dose,
        "bed_gy": bed,
        "eqd2_gy": eqd2,
    }


def export_calculation_to_csv(
    record: CalculationRecord,
    file_path: str | Path,
) -> Path:
    """Export one calculation record to a CSV file.

    Args:
        record: Structured calculation record to export.
        file_path: Destination of the CSV file.

    Returns:
        The path of the created CSV file.
    """
    output_path = Path(file_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open(
        mode="w",
        newline="",
        encoding="utf-8",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=list(record.keys()),
        )
        writer.writeheader()
        writer.writerow(record)

    return output_path


def export_calculations_to_csv(
    records: list[CalculationRecord],
    file_path: str | Path,
) -> Path:
    """Export multiple calculation records to one CSV file.

    Args:
        records: Calculation records to export.
        file_path: Destination of the CSV file.

    Returns:
        The path of the created CSV file.

    Raises:
        ValueError: If no calculation records are provided.
    """
    if not records:
        raise ValueError("At least one calculation record is required.")

    output_path = Path(file_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open(
        mode="w",
        newline="",
        encoding="utf-8",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=list(records[0].keys()),
        )
        writer.writeheader()
        writer.writerows(records)

    return output_path


def export_calculations_to_excel(
    records: list[CalculationRecord],
    file_path: str | Path,
) -> Path:
    """Export calculation records to an Excel workbook.

    Args:
        records: Calculation records to export.
        file_path: Destination of the Excel file.

    Returns:
        The path of the created Excel file.

    Raises:
        ValueError: If no calculation records are provided.
    """
    if not records:
        raise ValueError("At least one calculation record is required.")

    output_path = Path(file_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Radiotherapy Results"

    headers = list(records[0].keys())
    worksheet.append(headers)

    for record in records:
        worksheet.append([record[header] for header in headers])

    workbook.save(output_path)

    return output_path