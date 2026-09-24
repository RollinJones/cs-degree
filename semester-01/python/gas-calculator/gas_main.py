from gas_calculator.ppm_to_fraction import ppm_to_fraction
from gas_calculator.fraction_to_h2s import fraction_to_h2s
from gas_calculator.gas_to_ch4 import gas_to_ch4

scfm = float(input('Enter total gas flow (SCFM)'))
ch4 = float(input('Enter methane fraction (% CH4)'))
ppm = float(input('Enter H2S concentration (ppm)'))
print()

methane_flow = gas_to_ch4(scfm, ch4)
h2s_fraction = ppm_to_fraction(ppm)
h2s_flow = fraction_to_h2s(scfm, h2s_fraction)


print("====================================")
print("DIGESTER GAS ANALYSIS")
print("====================================")
print(f"Total gas flow: {scfm} SCFM")
print(f"Methane concentration: {ch4} %")
print(f"Methane flow: {methane_flow} SCFM")
print()
print(f"H2S concentration: {ppm} ppm")
print(f"H2S fraction: {h2s_fraction} %")
print(f"H2S flow: {h2s_flow} SCFM")