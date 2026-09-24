def ppm_to_fraction(ppm: float) -> float:
    if ppm < 0 or ppm > 1000000:
        raise ValueError("H2S concentration must be 0 to 1,000,000 ppm.")
    return ppm / 1000000 * 100