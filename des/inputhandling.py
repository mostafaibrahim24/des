import textwrap

def format_plaintext(plaintext):
    if len(plaintext) < 8:
        for i in range(0, 8-len(plaintext)):
            plaintext += "*"
    elif len(plaintext) > 8:
        plaintext = textwrap.wrap(plaintext, 8)
        for i in range(0,len(plaintext)):
            if len(plaintext[i]) < 8:
                for j in range(0, 8-len(plaintext[i])):
                    plaintext[i] += "*"
        return plaintext, True
    return plaintext, False
def check_key_length(key):
    while len(key) != 8:
        key = input("Must be 8 characters, Please enter a valid key: ")
    return key