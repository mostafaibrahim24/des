import textwrap















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
    

if __name__ == '__main__':
    plaintext = input("Enter plain text: ")
    plaintext,isLargerThan8Chars = formatPlaintext(plaintext)
    plaintext=changeToBits(plaintext,isLargerThan8Chars)
