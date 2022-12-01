import textwrap

def XOR(first_operand, second_operand):
    xor_result = ""
    for index in range(len(first_operand)):
        if first_operand[index] == second_operand[index]:
            xor_result += '0'
        else:
            xor_result += '1'
    return xor_result



def change_to_bits(plaintext, is_larger_than_8_chars):
    if is_larger_than_8_chars:
        for i in range(0, len(plaintext)):
            plaintext[i] = format(int.from_bytes(plaintext[i].encode(), 'big'), '064b')
        return plaintext
    plaintext = format(int.from_bytes(plaintext.encode(), 'big'), '064b')
    return plaintext


def change_from_bits(bits):

    bits = textwrap.wrap(bits, 8)

    ascii_text = ""
    for i in bits:
        ascii_text += chr(int(i, 2))

    return ascii_text
