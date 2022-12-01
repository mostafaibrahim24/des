import textwrap
from des.utils import change_to_bits,change_from_bits
from des.core import DES
from des.keysched import generate_subkeys,generate_subkeys_reverse_with_key
from des.inputhandling import format_plaintext,check_key_length

if __name__ == '__main__':

    plaintext = input("Enter plain text: ")
    plaintext, is_larger_than_8_chars = format_plaintext(plaintext)
    plaintext = change_to_bits(plaintext, is_larger_than_8_chars)
    
    key = input("Enter key: ")

    key = check_key_length(key)

    key = change_to_bits(key, False)

    cipher_text = ""
    keys,last_round_56_bits_presubkey = generate_subkeys(key)
    if is_larger_than_8_chars:

        for i in plaintext:
            cipher_text += DES(i, keys)

    else:
        cipher_text = DES(plaintext, keys)
    print(" ")
    print("Plaintext binary: ", plaintext)
    print("Ciphertext binary: " + cipher_text)
    print("Ciphertext hexadecimal: " + hex(int(cipher_text, 2)))
    print(" ")
    text_to_decrypt = textwrap.wrap(cipher_text, 64)

    keys_for_decrypt=generate_subkeys_reverse_with_key(key)
    plaintext = ""
    if is_larger_than_8_chars:

        for i in text_to_decrypt:
            plaintext += DES(i, keys_for_decrypt)

    else:
        plaintext = DES(text_to_decrypt[0], keys_for_decrypt)
    print("Plaintext (result of decryption): " + change_from_bits(plaintext))
