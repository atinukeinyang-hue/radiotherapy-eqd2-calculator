# Radiotherapy BED/EQD2 Calculator — Version 1.1.0

**Release date:** 11 August 2026

## Overview

Version 1.1.0 expands the initial public release into a more complete radiobiological calculation application.

This release adds validated input handling, cumulative EBRT and brachytherapy calculations, CSV and Excel exports, Continuous Integration, automated code-quality checking, and an expanded scientific verification suite.

## New Features

- Safer command-line input validation
- Tumour and late-tissue α/β presets
- Custom α/β selection
- Cumulative multi-course calculations
- Combined EBRT and brachytherapy workflows
- Cumulative physical dose, BED and EQD2
- Structured calculation records
- CSV result export
- Excel result export
- Automatic output-directory creation
- GitHub Actions Continuous Integration
- Ruff code-quality checks
- Final mathematical reference cases
- Complete Version 1.1 documentation

## Scientific Verification

Version 1.1.0 includes reference cases covering:

- Conventional fractionation
- HDR tumour fractionation
- HDR late-tissue fractionation
- Cumulative EBRT and HDR tumour calculations
- Cumulative EBRT and HDR late-tissue calculations

The release has:

- 63 automated tests passing locally
- 63 automated tests passing on GitHub Actions
- Ruff code-quality checks passing
- Dependency compatibility checks passing
- Python syntax-compilation checks passing
- Final CLI smoke test passing

## Installation

Clone the repository:

```bash
git clone https://github.com/atinukeinyang-hue/radiotherapy-eqd2-calculator.git
```

Enter the project:

```bash
cd radiotherapy-eqd2-calculator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Calculator

```bash
python app.py
```

## Run the Tests

```bash
python -m pytest
```

## Run the Code-Quality Check

```bash
python -m ruff check .
```

## Intended Use

This project is intended for:

- Medical physics education
- Radiobiology learning
- Radiotherapy research demonstrations
- Scientific programming practice
- Healthcare software portfolio development

## Important Limitation

This software is not a medical device and has not been independently validated, approved or certified for clinical decision-making or patient treatment.

All clinical radiobiological calculations must be independently verified using appropriate clinical protocols, validated systems, institutional procedures and qualified professional judgment.

## Author

**Atinuke A. Inyang**

Medical Physics • Radiotherapy • Healthcare AI • Python

GitHub: [github.com/atinukeinyang-hue](https://github.com/atinukeinyang-hue)