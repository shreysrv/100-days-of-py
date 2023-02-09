alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift):
    enc_text = ""
    for char in plain_text:
        index = alphabet_array.index(char)
        pos = index + shift
        while pos >= 26:
            pos -= 26
        enc_text += alphabet_array[pos]
    return enc_text


def decrypt(enc_text, shift):
    plain_text = ""
    for char in enc_text:
        index = alphabet_array.index(char)
        pos = index - shift
        while pos < 0:
            pos += 26
        plain_text += alphabet_array[pos]
    return plain_text


text = input("Enter word to encrypt:")
shift_key = int(input("Enter shift key:"))

encrypted_text = encrypt(text, shift_key)
print(f"Encrypted text:{encrypted_text}")
decrypted_text = decrypt(encrypted_text, shift_key)
print(f"Decrypted text:{decrypted_text}")
