import string


#method set to decrypt or to encrypt
user_input = input("Would you like to encrypt or decrypt text? (-e or -d)\n").strip().lower()

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16] #take a slice from the beginning (a) through the 16th character
#added by me
ENCRYPTED_FLAG = "ilnipdjheipnenhhedionepegiejmleoehejfcnimdgehimnepedhhfbafmcgdek"

#same b16_encode function as in the new_caesar function
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

#written by me to reverse the above function, same as the one I wrote for new_ceasear
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

#same shift function as new_caesar
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

#same unshift function written by me that I used in new_caesar
def unshift(ciphertext, shift_value):
	unshifted = ""
	for letter in ciphertext:
		t1 = ord(letter) - LOWERCASE_OFFSET
		t2 = ord(shift_value) - LOWERCASE_OFFSET
		unshifted += ALPHABET[(t1 + t2) % len(ALPHABET)]
	return unshifted

"""Flag entry and Key verification here
-Flag must be all hex characters.
-Key can only contain letters a-p (lowercase)
-Key must be 14 letters or less"""

if user_input == '-e':
	#flag = "redacted" #original line of code
	flag = input("Enter flag to encrypt: ").strip().lower()
	assert all([letter in "abcdef0123456789" for letter in flag])

	#key = "redacted" #original line of code
	key = input("Enter key: ").strip().lower()
	assert all([k in ALPHABET for k in key]) and len(key) < 15 #same assertion as the new_casear, except for the length checker at the end

	#same code for execution as the new_caesar challenge
	b16 = b16_encode(flag)
	enc = ""
	for i, c in enumerate(b16):
		enc += shift(c, key[i % len(key)])
	print("\nFinal Ciphertext:", enc, "\n") #line edited by me to more closely reflect the format of the new_casear challenge
	#print(enc) #original final print line from the coding challenge

elif user_input == '-d':
	#unshift the letters in the ENCRYPTED_FLAG
	flag = input("Enter flag to decrypt: ").strip().lower()
	
	key = input("Enter key: ").strip().lower()
	assert all([k in ALPHABET for k in key]) and len(key) < 15 #same assertion as the new_casear, except for the length checker at the end
	new_text = unshift(ENCRYPTED_FLAG, "a")

	b16_decoded_text = b16_decode(new_text) 
	print(b16_decoded_text) #print back for verification

	#convert the new_text to hex because the flag must be in hex
	hex_text = ""
	for letter in b16_decoded_text:
		converted = hex(ord(letter))
		hex_text += converted[2:]
	print(hex_text)

else:
	shifted = ""
	key = input("Please input a key: \n").strip().lower()
	for i, c in enumerate(user_input):
		shifted += shift(c, key[i % len(key)])
	print(shifted)

	backward = unshift(shifted, )