# Absolute humidity
# source: https://carnotcycle.wordpress.com/2012/08/04/how-to-convert-relative-humidity-to-absolute-humidity/
import math

rh = 35;
T = 23.1;

abs_hum = 6.112 * math.exp((17.67 * T)/(T+243.5)) * rh * 2.1674 / (273.15+T)

print("Abs hum1 = ", abs_hum)


###
# source: Vaisla paper
# Abs_hum = C · Pw/T_k (g/m3)
# C = Constant 2.16679 gK/J
# T_k = Temperature in K
# P_w = Vapour pressure in Pa
# P_w = P_ws(T)*rh/100 (hPa)
# P_ws = A*10^(m*T/(T+T_n))
# Constants A, m & T_n true for -20 to +50C
A = 6.116441
m = 7.591386
T_n = 240.7263
C = 2.16679         # gK/J
T_k = T + 273.15    # Kelvin

P_ws = A*10**(m*T/(T+T_n))
P_w = P_ws * rh/100 # hPa
print("P_w =", P_w, "hPa")
abs_hum = C * P_w*100/(T_k)

print("Abs hum2 = ", abs_hum, "g/m3")

# Dewpoint from RH
T_d = T_n / (m/(math.log10(P_w/A))-1)

print("Dew point =", T_d, "deg. C")
