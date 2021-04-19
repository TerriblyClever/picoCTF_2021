import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16] #take a slice from the beginning (a) through the 16th character
ENCRYPTED_FLAG = "ilnipdjheipnenhhedionepegiejmleoehejfcnimdgehimnepedhhfbafmcgdek"

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "abcdef" #flag must be hex
assert all([letter in "abcdef0123456789" for letter in flag])

key = "abcdefghijklmn"
assert all([k in ALPHABET for k in key]) and len(key) < 15

"""
b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
"""

print(b16_encode("hello world"), len(b16_encode('hello world')))
print(len("hello world"))
