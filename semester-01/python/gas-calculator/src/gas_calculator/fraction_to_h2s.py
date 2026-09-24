def fraction_to_h2s(scfm: float, h2s_fraction: float) -> float:
    if scfm < 0:
        raise ValueError("Flow rate cannot be negative.")
    return scfm * h2s_fraction / 100