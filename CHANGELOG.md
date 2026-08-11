# Changelog

All notable changes to the Radiotherapy BED/EQD2 Calculator are documented in this file.

The project follows semantic versioning.

## [1.0.0] — 2026-08-11

### Added

- Total physical dose calculation
- Biologically Effective Dose calculation
- Equivalent Dose in 2 Gy fractions calculation
- Tumour and early-responding tissue α/β preset
- Late-responding normal-tissue α/β preset
- Custom α/β input
- Single-course treatment workflow
- Cumulative multi-course treatment workflow
- Combined EBRT and brachytherapy calculations
- Cumulative BED and EQD2 calculations
- Positive and finite-number validation
- Whole-number fraction validation
- Structured calculation records
- Single and multiple-record CSV export
- Single and multiple-record Excel export
- Automatic result-output directory creation
- Command-line export menu
- Automated testing with pytest
- Final scientific reference cases
- Automated code-quality checks with Ruff
- Continuous Integration with GitHub Actions
- Project banner and complete technical documentation

### Verification

- 63 automated tests passing locally
- 63 automated tests passing on GitHub Actions
- Ruff code-quality checks passing
- Dependency compatibility verified
- Python syntax compilation verified
- Conventional fractionation reference case verified
- HDR tumour reference case verified
- HDR late-tissue reference case verified
- Cumulative EBRT and HDR tumour case verified
- Cumulative EBRT and HDR late-tissue case verified

### Important Notice

This software is intended for education, research demonstrations and scientific programming practice.

It is not a medical device and is not intended for independent clinical decision-making or patient treatment.