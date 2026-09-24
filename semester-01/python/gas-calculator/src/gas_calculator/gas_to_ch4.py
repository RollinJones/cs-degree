def gas_to_ch4(scfm: float, ch4: float) -> float:
    if scfm < 0:
        raise ValueError("Flow rate cannot be negative.")
    if ch4 < 0 or ch4 > 100:
        raise ValueError("Methane fraction must be 0 to 100.")
    return scfm * ch4 / 100