"""Conventional alpha/beta presets for educational calculations."""

ALPHA_BETA_PRESETS = {
    "tumour": {
        "label": "Tumour / early-responding tissue",
        "alpha_beta": 10.0,
        "unit": "Gy",
    },
    "late_tissue": {
        "label": "Late-responding normal tissue",
        "alpha_beta": 3.0,
        "unit": "Gy",
    },
}


def get_alpha_beta_preset(preset_name: str) -> float:
    """Return the alpha/beta value associated with a preset."""

    if not isinstance(preset_name, str):
        raise TypeError("Preset name must be text.")

    normalized_name = (
        preset_name
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
    )

    if not normalized_name:
        raise ValueError("Preset name cannot be empty.")

    if normalized_name not in ALPHA_BETA_PRESETS:
        available_presets = ", ".join(
            ALPHA_BETA_PRESETS.keys()
        )

        raise ValueError(
            f"Unknown preset '{preset_name}'. "
            f"Available presets: {available_presets}."
        )

    return ALPHA_BETA_PRESETS[normalized_name]["alpha_beta"]


def list_alpha_beta_presets() -> dict:
    """Return a safe copy of all available presets."""

    return {
        name: details.copy()
        for name, details in ALPHA_BETA_PRESETS.items()
    }