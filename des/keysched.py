import textwrap

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
def shift_right(key_part,number_of_shifts):
    key_part =list(key_part)
    for i in range(0,number_of_shifts):
        shifted_bit=key_part[len(key_part)-1] #MSB stored in a temporary
        del key_part[len(key_part)-1] # deleting LSB
        key_part.insert(0,shifted_bit) #Rotate
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
    last_round_56_bits_presubkey=""
    #Keys of the 16 rounds
    for i in range (0,16):
        if i==1-1 or i==2-1 or i==9-1 or i==16-1: #Shift by 1
            key[0]=shift_left(key[0],1)
            key[1]=shift_left(key[1],1)
            if i==15: last_round_56_bits_presubkey=key[0]+key[1]
        else: #Shift by 2
            key[0]=shift_left(key[0],2)
            key[1]=shift_left(key[1],2)
        subkeys[i]=apply_PC2(key[0]+key[1]) # Combining D & C if each round and then performing apply_PC2 => finialized subkey of the round
    return subkeys,last_round_56_bits_presubkey
def generate_subkeys_reverse_with_key(key):
    # Copy of the original 64 bit key, used in pc1 because the table's numbers refer to bits of the original
    original_key_64=key
    # Removal of each 8th bit
    key=remove_8th_bits(key)
    
    key=apply_PC1(key,original_key_64)

    subkeys=[""]*16 #init
    subkeys[0]=apply_PC2(key)

    #D & C
    key=textwrap.wrap(key,28)

    
    #Keys of the 16 rounds
    for i in range (1,16):
        if i==1-1 or i==2-1 or i==9-1 or i==16-1: #Shift by 1
            key[0]=shift_right(key[0],1)
            key[1]=shift_right(key[1],1)
        else: #Shift by 2
            key[0]=shift_right(key[0],2)
            key[1]=shift_right(key[1],2)
        subkeys[i]=apply_PC2(key[0]+key[1]) # Combining D & C if each round and then performing apply_PC2 => finialized subkey of the round
    return subkeys
def generate_subkeys_reverse_with_last_round(last_round_56_bits_presubkey):
    subkeys=[""]*16 #init
    subkeys[0]=apply_PC2(last_round_56_bits_presubkey)
    last_round_56_bits_presubkey=textwrap.wrap(last_round_56_bits_presubkey,28)

    
    #Keys of the 16 rounds
    for i in range (1,16):
        if i==1-1 or i==2-1 or i==9-1 or i==16-1: #Shift by 1
            last_round_56_bits_presubkey[0]=shift_right(last_round_56_bits_presubkey[0],1)
            last_round_56_bits_presubkey[1]=shift_right(last_round_56_bits_presubkey[1],1)
        else: #Shift by 2
            last_round_56_bits_presubkey[0]=shift_right(last_round_56_bits_presubkey[0],2)
            last_round_56_bits_presubkey[1]=shift_right(last_round_56_bits_presubkey[1],2)
        subkeys[i]=apply_PC2(last_round_56_bits_presubkey[0]+last_round_56_bits_presubkey[1]) # Combining D & C if each round and then performing apply_PC2 => finialized subkey of the round
    return subkeys
