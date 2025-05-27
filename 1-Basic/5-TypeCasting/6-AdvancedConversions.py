# Bytes conversion
s = "hello"
b = bytes(s, 'utf-8')
print(b)  # b'hello'

# Hex/Oct/Bin conversions
num = 255
hex_str = hex(num)  # '0xff'
oct_str = oct(num)  # '0o377'
bin_str = bin(num)  # '0b11111111'

# Float precision handling
from decimal import Decimal
precise_num = Decimal('3.1415926535')
print(float(precise_num))  # 3.1415926535