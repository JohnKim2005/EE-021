import random
from Functions import *

def exclusiveOr(binary: str, key:str) :
    returnBinary = ''
    for i in range(8) :
        if binary[i] == key[i] :
            returnBinary += '0'
        else :
            returnBinary += '1'
    return returnBinary


def Xor():
    """
    Binary Xor Cypher (01100001 + Key(10101010) -> 11001011 : 11001011 + Key(10101010) -> 01100001)
    - ✓ Encryption with Key
    - ✓ Encryption with Randomized Key
    - ✓ Decryption with Key
    - ✘ Decryption without key (Forced Decryption) - May require simple dictionary of most common words
    """

    cryption = choiceFunc('\n\nEncryption or Decryption? ( E or D )', 'E', 'D')  # Encryption Decryption Input Check

    outputFile = ''

    if cryption == 1:  # Encryption
        
        print('\n\nPlease input the Sentence/String to be Encoded')
        inputFile = input('> ')

        # Key Type Input Check
        keyType = choiceFunc('\n\nSet key or Randomized Key? ( S or R )', 'S', 'R')

        if keyType == 1:  # Set Key
            key = keyInput('8')
            for char in inputFile :
                outputFile += exclusiveOr(char2binary(char),key) + " "
            print('\n\n -= ENCODED TEXT =-')
            print(outputFile)

        elif keyType == 2:  # Randomized Key
            key = format(random.randint(0,255), '08b')
            for char in inputFile :
                outputFile += exclusiveOr(char2binary(char),key) + " "
            print(f'\n\n Key : {key}')
            print('\n -= ENCODED TEXT =-')
            print(outputFile)
        

    elif cryption == 2:
        # keyType = choiceFunc('\n\nSet key or Forced Decryption ( S or F )', 'S', 'F') # Key Type Input Check

        InputList = bitInput()

        # if keyType == 1:  # Key Type if/elif/else Statement
        key = keyInput('8')
        for Binary in InputList: 
            outputFile += binary2char(exclusiveOr(Binary, key))
        print('\n\n -= DECODED TEXT =-')
        print(outputFile)
            
            


        # elif keyType == 2:
        #     print('\n\ntry to force decrypt with algorithm (Big if on if this works and makes it on to the finalized version)')
        #     print('Output the Decrypted string and Code')