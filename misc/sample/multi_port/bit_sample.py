# coding=utf-8
# author: zengyuetian


# https://pypi.python.org/pypi/bitstring/3.1.3
# http://pythonhosted.org/bitstring/slicing.html
# import bitstring

from bitstring import BitArray

a = BitArray('0b00011110')
b = a[3:7]
print type(a), a
print type(b), b

print type(b.bin), b.bin