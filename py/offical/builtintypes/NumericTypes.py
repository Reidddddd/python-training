import sys

n = -37
print(bin(n))
print(n.bit_length())


def bit_len(self):
    s = bin(self)
    s = s.lstrip('-0b')
    return len(s)


print(bit_len(-37))
print()

print((1024).to_bytes(2, byteorder='big'))
print((1024).to_bytes(10, byteorder='big'))
print((-1024).to_bytes(10, byteorder='big', signed=True))
x = 1000
print(x.to_bytes((x.bit_length() // 8) + 1, byteorder='little'))
print(x.to_bytes((x.bit_length() // 8) + 1, byteorder='big'))
print(sys.byteorder)
print()

print(int.from_bytes(b'\x00\x10', byteorder='big'))
print(int.from_bytes(b'\x00\x10', byteorder='little'))
print(int.from_bytes(b'\xfc\x00', byteorder='big', signed=True))
print(int.from_bytes(b'\xfc\x00', byteorder='big', signed=False))
print(int.from_bytes([255, 0, 0], byteorder='big'))
print()

print((-2.0).is_integer())
print((3.2).is_integer())
print(float.fromhex('0x3.a7p10'))
print(float.hex(3740.0))
print()

