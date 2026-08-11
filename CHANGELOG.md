# Changelog

All notable changes to the Radiotherapy BED/EQD2 Calculator are documented in this file.

The project follows semantic versioning.

## [1.1.0] — 2026-08-11

### Added

- Safer command-line input validation
- Tumour and late-tissue α/β presets
- Custom α/β selection
- Cumulative multi-course calculations
- Combined EBRT and brachytherapy workflows
- Cumulative physical dose, BED and EQD2
- Structured calculation records
- Single and multiple-record CSV export
- Single and multiple-record Excel export
- Automatic output-directory creation
- GitHub Actions Continuous Integration
- Ruff code-quality checks
- Final scientific reference cases
- Version changelog and release notes
- Expanded Version 1.1 documentation

### Verification

- 63 automated tests passing locally
- 63 automated tests passing on GitHub Actions
- Ruff code-quality checks passing
- Dependency compatibility verified
- Python syntax compilation verified
- Final CLI smoke test passing
- Conventional fractionation reference case verified
- HDR tumour reference case verified
- HDR late-tissue reference case verified
- Cumulative EBRT and HDR tumour case verified
- Cumulative EBRT and HDR late-tissue case verified

## [1.0.0] — 2026-08-11

### Added

- Initial public release
- Total physical dose calculation
- Biologically Effective Dose calculation
- Equivalent Dose in 2 Gy fractions calculation
- Single-course command-line workflow
- Positive input validation
- Automated testing with pytest
- Project banner
- Installation and scientific documentation

## Important Notice

This software is intended for education, research demonstrations and scientific programming practice.

It is not a medical device and is not intended for independent clinical decision-making or patient treatment.