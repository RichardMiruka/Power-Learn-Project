# Bitwise operators act on operands as if they were strings of binary digits. 
# They operate bit by bit, hence the name.
# For example, 2 is 10 in binary and 7 is 111.

# & (AND) : It returns 1 if both the bits are 1. Otherwise it returns 0.
a = 9                   # 1001
b = 5                   # 0101
print(bin(a&b))        # 0001

# | (OR)  : It returns 1 if at least one of the bits is 1. Otherwise it returns 0.
c = a|b                 # 1101
print(bin(c))          # 1101

# ^ (XOR): It returns 1 if the bits are different. Otherwise it returns 0.
d = a^b                 # 1100
print(bin(d))          # 1100

# ~    : This operator is unary and returns the complement of the number.
e = ~9                  # -10
f = ~8                  # -9
g = ~0                  # -1
h = ~1                  # 0
i = ~-1                # 0
j = ~0xFFFF             # -65536
k = ~0xFF               # -256
l = ~4                  # -5
m = ~2                  # -3
n = ~1                  # -2
o = ~0                  # -1
p = ~-2                 # 1
q = ~0x7F                # -128
r = ~0xFF                # -256
s = ~0xFFFFFFFF         # 0
t = ~0xFFFFFFFFFFFFFFFF # 0
u = ~0x8000000000000000 # 0x7FFFFFFFFFFFFFFF
v = ~0x7FFFFFFFFFFFFFFF # 0x8000000000000000


# <<  : The number is multiplied by 2 raised to the power of the number of bits shifted.
x = 10
y = x<<1              # 10 * 2^1 = 20
z = x<<3              # 10 * 2^3 = 80

# >>  : The number is divided by 2 raised to the power of the number of bits shifted.
w = y>>1              # 20 / 2^1 = 10
aa = z>>3             # 80 / 2^3 = 10
bb = aa>>5            # 10 / 2^5 = 0
cc = bb>>62           # 0 / 2^62 = 0
dd = cc>>63           # 0 / 2^63 = 0
ee = dd>>64           # 0 / 2^64 = 0
ff = ee>>65           # 0 / 2^65 = 0
gg = ff>>66 & 0x1     # 0 / 2^66 = 0, bitwise AND with 1 = 0`   0 & 1 = 0`