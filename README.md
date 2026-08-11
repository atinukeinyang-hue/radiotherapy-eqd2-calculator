<p align="center">
  <img
    src="assets/radiotherapy-eqd2-banner.png"
    alt="Radiotherapy BED/EQD2 Calculator Banner"
    width="100%"
  >
</p>

# 🧮 Radiotherapy BED/EQD2 Calculator

![Python](https://img.shields.io/badge/PYTHON-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Radiobiology](https://img.shields.io/badge/RADIOBIOLOGY-LQ_MODEL-00A6A6?style=for-the-badge)
![BED](https://img.shields.io/badge/BED-CALCULATOR-8A2BE2?style=for-the-badge)
![EQD2](https://img.shields.io/badge/EQD2-CALCULATOR-D81B60?style=for-the-badge)
![Pytest](https://img.shields.io/badge/TESTS-58_PASSING-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Interface](https://img.shields.io/badge/INTERFACE-CLI-2F4F4F?style=for-the-badge)
![Export](https://img.shields.io/badge/EXPORT-CSV_&_EXCEL-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Status](https://img.shields.io/badge/STATUS-ACTIVE_DEVELOPMENT-F39C12?style=for-the-badge)
![Version](https://img.shields.io/badge/VERSION-1.0.0-8A2BE2?style=for-the-badge)

> 🚧 **Project Status: Active Development — Version 1.0.0**

This project provides a tested Python implementation of physical dose, biologically effective dose (BED), equivalent dose in 2 Gy fractions (EQD2), cumulative multi-course radiotherapy calculations, and structured CSV and Excel result exports.

## A Python-Based Radiobiological Dose Calculator for Radiotherapy and Medical Physics

---

## 📌 Overview

The **Radiotherapy BED/EQD2 Calculator** is a Python project for calculating:

- Total physical radiation dose
- Biologically Effective Dose (BED)
- Equivalent Dose in 2 Gy fractions (EQD2)
- Cumulative BED across multiple treatment courses
- Cumulative EQD2 across multiple treatment courses
- Combined EBRT and brachytherapy dose summaries
- Structured CSV calculation records
- Structured Excel calculation records

The project combines:

- Radiobiology
- Medical physics
- Python programming
- Input validation
- Command-line interface design
- CSV and Excel export
- Automated scientific testing
- Reproducible calculations

Radiotherapy schedules cannot always be compared using total physical dose alone.

For example:

```text
8 Gy × 3 fractions = 24 Gy

2 Gy × 12 fractions = 24 Gy
```

Both schedules deliver a physical dose of 24 Gy, but they are not biologically equivalent.

The calculator uses the **Linear-Quadratic model** to account for the effect of fraction size.

---

## ✨ Current Features

The calculator currently includes:

- Total physical dose calculation
- BED calculation
- EQD2 calculation
- User-defined dose per fraction
- User-defined number of fractions
- User-defined α/β ratio
- Tumour and early-responding tissue preset: α/β = 10 Gy
- Late-responding normal-tissue preset: α/β = 3 Gy
- Custom α/β values
- Single-course treatment calculations
- Cumulative multi-course calculations
- Combined EBRT and brachytherapy calculations
- Multiple-course physical-dose summaries
- Cumulative BED calculation
- Cumulative EQD2 calculation
- Structured calculation records
- Single-course CSV export
- Multi-course CSV export
- Single-course Excel export
- Multi-course Excel export
- Combined CSV and Excel export option
- Automatic creation of the output directory
- Command-line export menu
- Positive-number validation
- Whole-number fraction validation
- Rejection of zero and negative inputs
- Rejection of Boolean values
- Rejection of NaN and infinite values
- Automated testing with pytest
- Conventional fractionation test cases
- HDR tumour test cases
- Late-responding normal-tissue test cases
- CLI workflow tests
- Cumulative treatment-course tests
- CSV content-verification tests
- Excel content-verification tests
- CLI export workflow tests

---

## 🧬 Scientific Background

### 1. Total Physical Dose

For a treatment schedule where:

- `n` = number of fractions
- `d` = dose per fraction

The total physical dose is:

```text
Total Physical Dose = n × d
```

Example:

```text
8 Gy × 3 fractions = 24 Gy
```

Physical dose alone does not account for the biological consequences of changing the dose per fraction.

---

### 2. Linear-Quadratic Model

The calculator uses the **Linear-Quadratic model** as the basis for its radiobiological calculations.

The model describes radiation effect using two components:

- **α (alpha):** the linear component
- **β (beta):** the quadratic component

The **α/β ratio** describes the sensitivity of a tissue or biological endpoint to changes in fraction size.

---

### 3. Alpha/Beta Ratio

Different tissues, tumours, and biological endpoints may have different α/β values.

#### High α/β

A commonly used conventional value for many tumours and early-responding tissues is:

```text
α/β = 10 Gy
```

Calculations may be written as:

```text
BED10
```

#### Low α/β

A commonly used conventional value for many late-responding normal-tissue endpoints is:

```text
α/β = 3 Gy
```

Calculations may be written as:

```text
BED3
```

These values are conventional assumptions—not universal biological constants.

The appropriate α/β ratio depends on factors including:

- Tissue
- Tumour type
- Biological endpoint
- Clinical context
- Supporting scientific evidence

---

## 🧮 BED Calculation

The **Biologically Effective Dose** is calculated using:

```text
BED = nd × (1 + d / (α/β))
```

Where:

```text
n    = number of fractions
d    = dose per fraction
α/β  = alpha/beta ratio
```

BED provides a model-derived representation of the biological effect of a fractionation schedule.

---

## 📊 EQD2 Calculation

**Equivalent Dose in 2 Gy fractions (EQD2)** converts BED into the equivalent dose that would produce the same modelled biological effect if delivered using 2 Gy fractions.

The equation is:

```text
EQD2 = BED / (1 + 2 / (α/β))
```

This allows fractionation schedules to be compared using a common 2 Gy-per-fraction reference.

---

## ➕ Cumulative Treatment Calculations

The calculator can combine multiple treatment courses that refer to the same tissue or biological endpoint.

Examples include:

- EBRT followed by brachytherapy
- Multiple brachytherapy treatment courses
- Sequential radiotherapy schedules

For each course, the calculator determines:

- Physical dose
- BED
- EQD2

It then reports:

- Total physical dose
- Cumulative BED
- Cumulative EQD2

Cumulative BED is calculated as:

```text
Cumulative BED = BED₁ + BED₂ + ... + BEDₙ
```

Cumulative EQD2 is then calculated using the common α/β ratio:

```text
Cumulative EQD2 = Cumulative BED / (1 + 2 / (α/β))
```

All combined treatment courses must refer to the same tissue or biological endpoint and use the same α/β ratio.

### Example: EBRT + HDR Brachytherapy

Using a tumour α/β ratio of 10 Gy:

```text
Course 1: 1.8 Gy × 25 fractions
Course 2: 8 Gy × 3 fractions
```

Results:

```text
Total physical dose: 69.00 Gy
Cumulative BED: 96.30 Gy10
Cumulative EQD2: 80.25 Gy
```

---

## 🔬 Worked Example 1 — Conventional Fractionation

Consider:

```text
Dose per fraction = 2 Gy
Number of fractions = 25
α/β = 10 Gy
```

### Physical Dose

```text
2 × 25 = 50 Gy
```

### BED

```text
BED10 = 60 Gy10
```

### EQD2

```text
EQD2 = 50 Gy
```

Therefore:

```text
Physical Dose = 50.00 Gy
BED10         = 60.00 Gy10
EQD2          = 50.00 Gy
```

Because the schedule already uses 2 Gy fractions, its EQD2 equals its physical dose.

---

## 🎯 Worked Example 2 — HDR Tumour Calculation

Consider:

```text
Dose per fraction = 8 Gy
Number of fractions = 3
α/β = 10 Gy
```

### Physical Dose

```text
8 × 3 = 24 Gy
```

### BED

```text
BED10 = 43.20 Gy10
```

### EQD2

```text
EQD2 = 36.00 Gy
```

Therefore:

```text
Physical Dose = 24.00 Gy
BED10         = 43.20 Gy10
EQD2          = 36.00 Gy
```

---

## 🫀 Worked Example 3 — Late-Responding Normal Tissue

Using the same physical fractionation:

```text
Dose per fraction = 8 Gy
Number of fractions = 3
α/β = 3 Gy
```

The physical dose remains:

```text
24 Gy
```

However:

```text
BED3 = 88.00 Gy3
EQD2 = 52.80 Gy
```

Therefore:

```text
Physical Dose = 24.00 Gy
BED3          = 88.00 Gy3
EQD2          = 52.80 Gy
```

This demonstrates an important radiobiological principle:

> The same physical fractionation schedule can produce very different modelled biological effects depending on the α/β ratio used.

---

## 📤 Result Export

After completing a single-course or cumulative calculation, the CLI displays:

```text
Export Results
--------------
1. Export to CSV
2. Export to Excel
3. Export to both CSV and Excel
4. Do not export
```

### CSV export

CSV exports contain these columns:

```text
component
dose_per_fraction_gy
number_of_fractions
alpha_beta_gy
total_physical_dose_gy
bed_gy
eqd2_gy
```

CSV files can be opened using:

- Microsoft Excel
- Google Sheets
- LibreOffice Calc
- Python
- R
- Other data-analysis tools

### Excel export

Excel results are written to a worksheet named:

```text
Radiotherapy Results
```

Excel files use the `.xlsx` format and are created with `openpyxl`.

### Generated files

Single-course exports use:

```text
outputs/single_treatment_result.csv
outputs/single_treatment_result.xlsx
```

Cumulative exports use:

```text
outputs/cumulative_treatment_result.csv
outputs/cumulative_treatment_result.xlsx
```

For cumulative calculations, exported records include:

- Each individual treatment course
- The cumulative physical-dose total
- The cumulative BED
- The cumulative EQD2

The `outputs/` directory is created automatically and excluded from version control.

---

## 📁 Project Structure

```text
radiotherapy-eqd2-calculator/
│
├── eqd2_calculator/
│   ├── __init__.py
│   ├── calculator.py
│   ├── cumulative.py
│   ├── export.py
│   └── presets.py
│
├── tests/
│   ├── test_app.py
│   ├── test_calculator.py
│   ├── test_cumulative.py
│   ├── test_export.py
│   └── test_presets.py
│
├── assets/
│   └── radiotherapy-eqd2-banner.png
│
├── outputs/                  # Generated locally and Git-ignored
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

Local development and generated directories such as:

```text
.venv/
__pycache__/
.pytest_cache/
outputs/
```

are excluded from version control.

---

## ⚙️ Core Modules

The scientific calculations, cumulative calculations, exports and command-line interface are separated into dedicated modules.

### Core calculations

```text
eqd2_calculator/calculator.py
```

This module contains:

```python
calculate_total_dose()
calculate_bed()
calculate_eqd2()
```

### Cumulative calculations

```text
eqd2_calculator/cumulative.py
```

This module contains:

```python
calculate_cumulative_bed()
calculate_cumulative_eqd2()
```

### Result exports

```text
eqd2_calculator/export.py
```

This module contains:

```python
create_calculation_record()
export_calculation_to_csv()
export_calculations_to_csv()
export_calculations_to_excel()
```

### Alpha/Beta presets

```text
eqd2_calculator/presets.py
```

This module stores reusable conventional α/β presets for:

- Tumours and early-responding tissues
- Late-responding normal tissues

Separating the scientific logic, exports and interface makes the functions easier to test, verify, reuse and extend.

---

## 📦 Dependencies

The project currently uses:

```text
pytest==9.1.1
openpyxl==3.1.5
```

- `pytest` runs the automated test suite.
- `openpyxl` creates and verifies Excel `.xlsx` files.

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/atinukeinyang-hue/radiotherapy-eqd2-calculator.git
```

### 2. Enter the Project Directory

```bash
cd radiotherapy-eqd2-calculator
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Running the Calculator

From the project root, run:

```bash
python app.py
```

The main menu provides:

```text
Radiotherapy BED/EQD2 Calculator
--------------------------------

Main Menu
---------
1. Single treatment course
2. Cumulative treatment courses
3. Exit
```

### Single Treatment Course

The calculator requests:

```text
Dose per fraction (Gy):
Number of fractions:
Alpha/Beta selection:
```

It then displays:

```text
Alpha/Beta value
Total physical dose
BED
EQD2
```

The user can then export the result to:

```text
CSV
Excel
Both CSV and Excel
```

### Cumulative Treatment Courses

The calculator requests:

```text
Number of treatment courses
Common Alpha/Beta selection
Dose per fraction for each course
Number of fractions for each course
```

It then displays:

```text
Individual course summaries
Total physical dose
Cumulative BED
Cumulative EQD2
```

The individual courses and cumulative summary can then be exported to CSV, Excel or both formats.

---

## 🛡️ Input Validation

The calculator validates scientific and user inputs before processing them.

The calculation functions require:

```text
Dose per fraction > 0
Number of fractions > 0
Alpha/Beta > 0
BED > 0
```

The calculator also rejects:

- Text where a number is required
- Zero values
- Negative values
- Decimal values for the number of fractions
- Boolean values
- NaN values
- Positive infinity
- Negative infinity
- Fewer than two courses for a cumulative calculation
- Invalid main-menu options
- Invalid export-menu options
- Empty record collections during multi-record export

Invalid inputs generate a clear error instead of silently producing an inappropriate result.

---

## 🧪 Automated Scientific Testing

The project uses **pytest** for automated testing.

Run:

```bash
python -m pytest
```

The current test suite contains:

```text
58 passing tests
```

Testing covers:

- Total physical dose
- BED
- EQD2
- Conventional 2 Gy fractionation
- HDR tumour fractionation
- HDR late-responding tissue fractionation
- Tumour α/β presets
- Normal-tissue α/β presets
- Custom α/β values
- Invalid numeric inputs
- Invalid data types
- NaN and infinite values
- Single-course CLI workflows
- Main-menu validation
- Cumulative BED
- Cumulative EQD2
- Combined EBRT and HDR brachytherapy
- Empty treatment-course collections
- Invalid cumulative treatment courses
- Structured calculation records
- Single-record CSV export
- Multiple-record CSV export
- Excel workbook creation
- CSV headings and values
- Excel headings and values
- Empty export-record validation
- Single-course CLI export
- Cumulative-course CLI export
- Automatic output-directory creation

Approximate numerical comparison is used where appropriate to avoid false failures caused by normal floating-point representation.

---

## 🧠 Why Automated Tests Matter

Scientific software should not merely produce output.

Its calculations should also be:

- Verifiable
- Reproducible
- Traceable
- Resistant to accidental regression

Automated tests help identify situations where future modifications unintentionally change previously verified calculations.

This becomes increasingly important as the project grows to include additional radiobiological functionality and export formats.

---

## ⚠️ Scientific Limitations

This project implements the standard Linear-Quadratic model.

Important limitations include:

- α/β values are model parameters and must be selected according to the relevant tissue, tumour, endpoint, clinical context and supporting evidence.
- BED and EQD2 are model-derived quantities rather than direct measurements of biological effect.
- The basic LQ model does not represent every biological or clinical factor affecting radiation response.
- Interpretation at very high doses per fraction requires appropriate caution.
- Cumulative calculations assume that all courses refer to the same tissue or biological endpoint.
- Cumulative calculations require a common α/β ratio.
- The calculator does not currently model incomplete repair between fractions.
- The calculator does not currently include time, repopulation or treatment-gap corrections.
- The calculator does not account for spatial differences between treatment-course dose distributions.
- Adding EQD2 values does not independently establish anatomical dose overlap.
- Exported files are calculation records, not clinical treatment reports.
- The calculator does not replace a treatment-planning system.
- The calculator does not replace institutional clinical protocols.
- The calculator does not replace qualified medical-physics or radiation-oncology judgment.

---

## 🚀 Planned Development

Future versions may include:

### Radiobiology

- Additional tissue and tumour presets
- Treatment-time corrections
- Repopulation modelling
- Incomplete-repair modelling
- Additional radiobiological models

### Data

- CSV input
- Batch treatment-course calculations
- Structured calculation reports
- User-defined output filenames
- Additional export formatting

### Software Engineering

- Expanded validation
- Additional automated tests
- Additional scientific validation cases
- Improved error handling
- Continuous integration with GitHub Actions

### Application Development

- Improved command-line interface
- Web interface
- REST API integration
- Interactive result visualisation

---

## 🎓 Intended Use

This project is intended for:

- Medical physics education
- Radiobiology learning
- Radiotherapy research demonstrations
- Python programming practice
- Scientific software development
- Healthcare software portfolio development

It is **not intended to provide clinical treatment recommendations**.

---

## ⚕️ Disclaimer

This software is an **educational and research-oriented project**.

It is not a medical device and has not been independently validated, approved or certified for clinical decision-making or patient treatment.

Clinical radiobiological calculations must be independently verified using:

- Appropriate clinical protocols
- Validated clinical systems
- Institutional procedures
- Qualified professional judgment

---

## 👩🏽‍💻 Author

**Atinuke A. Inyang**

Medical Physics • Radiotherapy • Healthcare AI • Python

GitHub: [github.com/atinukeinyang-hue](https://github.com/atinukeinyang-hue)

---

Built around three principles:

**Scientific grounding • Reproducibility • Transparent calculation**