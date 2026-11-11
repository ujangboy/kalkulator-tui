from hitung.theme import build_theme, ACCENTS


def test_dark_theme_colors():
    theme = build_theme(mode="dark", accent="blue")
    assert theme.background == "#0B0F16"
    assert theme.surface == "#111927"
    assert theme.panel == "#151C28"
    assert theme.primary == "#4389F5"
    assert theme.variables["border"] == "#29374A"
    assert theme.variables["muted"] == "#96A4B7"


def test_accents():
    assert ACCENTS["blue"] == "#4389F5"
    assert ACCENTS["mint"] == "#55D6A4"
    assert ACCENTS["amber"] == "#E9B96E"


def test_default_accent_is_blue_and_bogus_falls_back():
    assert build_theme().primary == ACCENTS["blue"]
    assert build_theme(accent="bogus").primary == ACCENTS["blue"]
    assert build_theme(mode="light").background == "#F4F7FB"
