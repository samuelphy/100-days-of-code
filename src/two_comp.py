# 2 complements
import math

# Example: twos_complment(0xFC18,16) = -1000
def twos_complement(value, bits):
    if (value & (1 << (bits - 1))) != 0: # Check if sign bit is set
        value = value - (1 << bits)      # Compute negative value
    return value

#0x03E8 = 1000
#0xFC18 = -1000
#hex_string = '0xFC18' # or whatever... '0x' prefix doesn't matter
#print(twos_comp(int(hex_string,16), 16))
data=[0,0,0,0,0,0,0,0,0,0]
data[6]=0xFC
data[7]=0x18
acc_x = ((data[6] << 8) | data[7])

print(math.sqrt(acc_x ** 2))

out = twos_complement(acc_x,16)
print(out)
print(math.sqrt(out **2))

print(math.sqrt(twos_complement(acc_x,16) **2))
