import textwrap


def initial_permutation(plain_text):
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


def final_permutation(text):
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


def encrypt(plain_text, passed_key):

    print("No permutation: "+ plain_text)
    plain_text = initial_permutation(plain_text)
    print("permutated: "+plain_text)
    left_portion = plain_text[:len(plain_text)//2]
    right_portion = plain_text[len(plain_text)//2:]
    print(left_portion)
    print(right_portion)

    plain_text = final_permutation(plain_text)
    print("final: " + plain_text)














def formatPlaintext(plaintext):
    if(len(plaintext)<8):
        for i in range(0,8-len(plaintext)):
            plaintext+="#"
    elif(len(plaintext)>8):
        plaintext = textwrap.wrap(plaintext,8)
        return plaintext,True
    return plaintext,False

def changeToBits(plaintext,isLargerThan8Chars):
    if(isLargerThan8Chars):
        for i in range(0,len(plaintext)):
            plaintext[i]=format(int.from_bytes(plaintext[i].encode(),'big'),'064b')
        return plaintext
    plaintext=format(int.from_bytes(plaintext.encode(),'big'),'064b')
    return plaintext


if __name__ == '__main__':

    plaintext = input("Enter plain text: ")
    plaintext, isLargerThan8Chars = formatPlaintext(plaintext)
    plaintext = changeToBits(plaintext, isLargerThan8Chars)
    key = input("Enter key: ")

    while(len(key) != 8):
        key = input("Must be 8 characters, Please enter a valid key: ")

    key = changeToBits(key, False)

    #test encrypt function
    encrypt(plaintext, key)