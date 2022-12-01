from .utils import XOR
from .ffunc import f_function

def apply_initial_permutation(plaintext):
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
        permutated_text += plaintext[i-1]

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





def DES(plaintext, keys):

    plaintext = apply_initial_permutation(plaintext)
    left_portion = plaintext[:len(plaintext)//2]
    right_portion = plaintext[len(plaintext)//2:]

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
