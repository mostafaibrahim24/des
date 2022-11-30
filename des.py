import textwrap


def XOR(first_operand, second_operand):
    xor_result = ""
    for index in range(len(first_operand)):
        if first_operand[index] == second_operand[index]:
            xor_result += '0'
        else:
            xor_result += '1'
    return xor_result


def apply_initial_permutation(plain_text):
    ip_table = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

    permutated_text = ""
    for i in ip_table:
        # Swap the bits according to the initial permutation table
        permutated_text += plain_text[i-1]

    return permutated_text


def apply_final_permutation(text):
    final_permutation_table = [40, 8, 48, 16, 56, 24, 64, 32,
                               39, 7, 47, 15, 55, 23, 63, 31,
                               38, 6, 46, 14, 54, 22, 62, 30,
                               37, 5, 45, 13, 53, 21, 61, 29,
                               36, 4, 44, 12, 52, 20, 60, 28,
                               35, 3, 43, 11, 51, 19, 59, 27,
                               34, 2, 42, 10, 50, 18, 58, 26,
                               33, 1, 41, 9, 49, 17, 57, 25]

    permutated_text = ""
    for i in final_permutation_table:
        # Swap the bits according to the initial permutation table
        permutated_text += text[i - 1]

    return permutated_text


def apply_function_permutation(sbox_result):
    permutation_table = [16, 7, 20, 21, 29, 12, 28, 17,
                         1, 15, 23, 26, 5, 18, 31, 10,
                         2, 8, 24, 14, 32, 27, 3, 9, 19,
                         13, 30, 6, 22, 11, 4, 25]

    permutated_text = ""
    for i in permutation_table:
        # Swap the bits according to the initial permutation table
        permutated_text += sbox_result[i - 1]

    return permutated_text


def apply_expansion(right_portion):
    expansion_table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
                       8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
                       16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
                       24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

    expanded_right_portion = ""
    for i in expansion_table:
        expanded_right_portion += right_portion[i-1]
    return expanded_right_portion


# Isolate middle 4 bits to get column number
def get_column(sbox_text):
    middle_4bits = sbox_text[1:5]
    column_number = int(middle_4bits, 2)

    return column_number


# Isolate outer bits to get row number
def get_row(sbox_text):
    outer_2bits = sbox_text[0] + sbox_text[-1]
    row_number = int(outer_2bits, 2)
    return row_number


def decimal_to_binary(decimal):
    binary_4bits = bin(decimal)[2:].zfill(4)
    return binary_4bits


def sbox_lookup(xor_result):
    sbox = [
        # SBox-1
        [   # 0  1  2  3  4  5
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        # SBox-2

        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],

        # SBox-3

        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]

        ],

        # SBox-4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],

        # SBox-5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        # SBox-6

        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]

        ],
        # SBox-7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        # SBox-8

        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]

    ]
    # Split text to 6 bits
    divided_xor_6bits = textwrap.wrap(xor_result, 6)

    sbox_result = ""
    for i in range(len(divided_xor_6bits)):
        column = get_column(divided_xor_6bits[i])
        row = get_row(divided_xor_6bits[i])
        sbox_result += decimal_to_binary(sbox[i][row][column])

    return sbox_result


def f_function(right_portion, passed_key):
    expansion_result = apply_expansion(right_portion)
    xor_result = XOR(expansion_result, passed_key)
    sbox_result = sbox_lookup(xor_result)
    permutation_result = apply_function_permutation(sbox_result)
    return permutation_result


def DES(plain_text, keys):

    plain_text = apply_initial_permutation(plain_text)
    left_portion = plain_text[:len(plain_text)//2]
    right_portion = plain_text[len(plain_text)//2:]

    # For first round
    new_left_portion = right_portion  # L1 = R0
    f_function_result = f_function(right_portion, keys[0])
    new_right_portion = XOR(left_portion, f_function_result)  # R1 = f function xor L0

    # For rounds 2 to 16
    for i in range(1, 16):
        old_left_portion = new_left_portion  # store L1
        new_left_portion = new_right_portion  # L2 = R1
        f_function_result = f_function(new_right_portion, keys[i])
        # should xor the result with old left portion and the final result is the new right portion
        new_right_portion = XOR(old_left_portion, f_function_result)  # R2 = f function xor L1

    new_left_portion, new_right_portion = new_right_portion, new_left_portion

    cipher_text = new_left_portion + new_right_portion

    cipher_text = apply_final_permutation(cipher_text)

    return cipher_text


def format_plaintext(plaintext):
    if len(plaintext) < 8:
        for i in range(0, 8-len(plaintext)):
            plaintext += "#"
    elif len(plaintext) > 8:
        plaintext = textwrap.wrap(plaintext, 8)
        for i in range(0,len(plaintext)):
            if len(plaintext[i]) < 8:
                for j in range(0, 8-len(plaintext[i])):
                    plaintext[i] += "#"
        return plaintext, True
    return plaintext, False


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


def remove_8th_bits(key):
    key = list(key)
    for i in range(0,len(key)):
        if(i+1)%8==0:
            key[i]=''
    key = ''.join(key)
    return key

def apply_PC1(key, original_key_64):
    key = list(key)
    pc1_table = [57, 49, 41, 33, 25, 17, 9,  1,
                 58, 50, 42, 34, 26, 18, 10, 2,
                 59, 51, 43, 35, 27, 19, 11, 3,
                 60, 52, 44, 36, 63, 55, 47, 39,
                 31, 23, 15, 7,  62, 54, 46, 38,
                 30, 22, 14, 6,  61, 53, 45, 37,
                 29, 21, 13, 5,  28, 20, 12, 4]
    j=0
    for i in pc1_table:
         key[j]=original_key_64[i-1]
         j+=1
    return ''.join(key)


def apply_PC2(key):
    keycp=key # Copy because permute based on the combination of D & C 
    key=list(key)
    pc2_table = [14, 17, 11, 24, 1, 5, 3, 28,
                 15, 6, 21, 10, 23, 19, 12, 4,
                 26, 8, 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55, 30, 40,
                 51, 45, 33, 48, 44, 49, 39, 56,
                 34, 53, 46, 42, 50, 36, 29, 32]
    j=0
    for i in pc2_table:
        key[j]=keycp[i-1]
        j+=1
    return ''.join(key)[0:48] #Removal the 8 bits ((28+28)56 => 48)


def shift_left(key_part,number_of_shifts):
    key_part =list(key_part)
    for i in range(0,number_of_shifts):
        shifted_bit=key_part[0] #MSB stored in a temporary
        del key_part[0] # deleting MSB
        key_part.append(shifted_bit) #Rotate
    return ''.join(key_part)


def generate_subkeys(key):
    # Copy of the original 64 bit key, used in pc1 because the table's numbers refer to bits of the original
    original_key_64=key
    # Removal of each 8th bit
    key=remove_8th_bits(key)
    
    key=apply_PC1(key,original_key_64)

    #D & C
    key=textwrap.wrap(key,28)

    subkeys=[""]*16 #init

    #Keys of the 16 rounds
    for i in range (0,16):
        if i==1-1 or i==2-1 or i==9-1 or i==16-1: #Shift by 1
            key[0]=shift_left(key[0],1)
            key[1]=shift_left(key[1],1)
        else: #Shift by 2
            key[0]=shift_left(key[0],2)
            key[1]=shift_left(key[1],2)
        subkeys[i]=apply_PC2(key[0]+key[1]) # Combining D & C if each round and then performing apply_PC2 => finialized subkey of the round
    return subkeys


if __name__ == '__main__':

    plaintext = input("Enter plain text: ")
    plaintext, is_larger_than_8_chars = format_plaintext(plaintext)
    plaintext = change_to_bits(plaintext, is_larger_than_8_chars)
    print("Plaintext binary: ", plaintext)
    key = input("Enter key: ")

    while len(key) != 8:
        key = input("Must be 8 characters, Please enter a valid key: ")

    key = change_to_bits(key, False)

    cipher_text = ""
    keys = generate_subkeys(key)
    if is_larger_than_8_chars:

        for i in plaintext:
            cipher_text += DES(i, keys)

    else:
        cipher_text = DES(plaintext, keys)

    print("ciphertext binary: " + cipher_text)
    print("ciphertext hexadecimal: " + hex(int(cipher_text, 2)))

    text_to_decrypt = textwrap.wrap(cipher_text, 64)

    keys.reverse()
    cipher_text = ""
    if is_larger_than_8_chars:

        for i in text_to_decrypt:
            cipher_text += DES(i, keys)

    else:
        cipher_text = DES(text_to_decrypt[0], keys)
    print("plaintext after converting keys: " + change_from_bits(cipher_text))
