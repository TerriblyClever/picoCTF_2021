import string

flag = input("Enter the flag to encrypt: ").strip().lower()
key = input("Enter the key (must be a single letter): ").strip().lower()
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	print("\nb16_encoded text:", enc)
	return enc

def b16_decode(ciphertext):
	decoded = ""
	binary_values = []
	for letter in ciphertext:
		position = ALPHABET.index(letter)
		binary_values.append(format(position, '#06b'))

	combined = []
	while len(binary_values) != 0:
		combined.append(binary_values[0][2:] + binary_values[1][2:])
		binary_values.pop(0)
		binary_values.pop(0)

	for value in combined:
		decoded += (chr(int(value, 2)))
		
	return decoded

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def unshift(ciphertext, shift_value):
	unshifted = ""
	for letter in ciphertext:
		t1 = ord(letter) - LOWERCASE_OFFSET
		t2 = ord(shift_value) - LOWERCASE_OFFSET
		unshifted += ALPHABET[(t1 + t2) % len(ALPHABET)]
	return unshifted

assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print("\nFinal Ciphertext:", enc, "\n")

#ciphertext = input("Enter ciphertext to be decoded:\n>>> ").strip().lower()
ciphertext = 'lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil'
for letter in ALPHABET:
	new_text = unshift(ciphertext, letter)
	print(b16_decode(new_text))