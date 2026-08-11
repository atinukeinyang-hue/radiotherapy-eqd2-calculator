import pytest

from eqd2_calculator.presets import (
    get_alpha_beta_preset,
    list_alpha_beta_presets,
)


def test_tumour_preset():
    result = get_alpha_beta_preset("tumour")

    assert result == 10.0


def test_late_tissue_preset():
    result = get_alpha_beta_preset("late_tissue")

    assert result == 3.0


@pytest.mark.parametrize(
    "preset_name",
    [
        "late tissue",
        "late-tissue",
        "  LATE_TISSUE  ",
    ],
)
def test_preset_name_normalization(preset_name):
    result = get_alpha_beta_preset(preset_name)

    assert result == 3.0


def test_rejects_unknown_preset():
    with pytest.raises(
        ValueError,
        match="Unknown preset",
    ):
        get_alpha_beta_preset("unknown")


def test_rejects_empty_preset_name():
    with pytest.raises(
        ValueError,
        match="Preset name cannot be empty",
    ):
        get_alpha_beta_preset("")


def test_rejects_non_text_preset_name():
    with pytest.raises(
        TypeError,
        match="Preset name must be text",
    ):
        get_alpha_beta_preset(10)


def test_returned_preset_dictionary_is_a_copy():
    presets = list_alpha_beta_presets()

    presets["tumour"]["alpha_beta"] = 99.0

    assert get_alpha_beta_preset("tumour") == 10.0