# Radiotherapy BED/EQD2 Calculator — Version 1.0.0

**Release date:** 11 August 2026

## Overview

Version 1.0.0 is the first complete release of the Radiotherapy BED/EQD2 Calculator.

It provides a tested command-line application for calculating physical dose, Biologically Effective Dose, Equivalent Dose in 2 Gy fractions, and cumulative radiobiological results across multiple treatment courses.

## Main Features

- Single-course radiotherapy calculations
- Cumulative multi-course calculations
- Combined EBRT and brachytherapy workflows
- Total physical dose calculation
- BED calculation
- EQD2 calculation
- Tumour α/β preset of 10 Gy
- Late-responding normal-tissue α/β preset of 3 Gy
- Custom α/β values
- CSV result export
- Excel result export
- Positive and finite-number validation
- Whole-number fraction validation
- Clear command-line menus and error messages

## Scientific Verification

Version 1.0.0 includes reference cases covering:

- Conventional fractionation
- HDR tumour fractionation
- HDR late-tissue fractionation
- Cumulative EBRT and HDR tumour calculations
- Cumulative EBRT and HDR late-tissue calculations

The project has:

- 63 automated tests passing locally
- 63 automated tests passing on GitHub Actions
- Ruff code-quality checks passing
- Dependency compatibility checks passing
- Python syntax compilation checks passing

## Installation

Clone the repository:

```bash
git clone https://github.com/atinukeinyang-hue/radiotherapy-eqd2-calculator.git