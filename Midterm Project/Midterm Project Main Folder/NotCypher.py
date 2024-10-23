import random
from Functions import *

def flip(binary:str):
    flippedBinary = ''
    for num in binary :
        if num == '1':
            flippedBinary += '0'
        else :
            flippedBinary += '1'
    return flippedBinary

def Not():
    """
    Binary Not Cypher (01100001 -> 10011110) - Might not work as the first 32 in ascii code will break. Might have to send Encrypted and to be decrypted files in as binary
    - ✓ Encryption
    - ✓ Decryption
    """
    cryption = choiceFunc('\n\nEncryption or Decryption? ( E or D )', 'E', 'D')  # Encryption Decryption Input Check

    if cryption == 1:  # Encryption
        print("\n\nPlease Input a String to Encode.")
        inputFile = input('> ')
        returnString = ''
        for char in inputFile :
            print(char)
            print(char2binary(char))
            print(flip(char2binary(char)))
            returnString += (flip(char2binary(char))) + " "

        print('\n\n -= ENCODED TEXT =-')
        print(returnString)
        

    elif cryption == 2:
        inputList = bitInput()
        returnString = ''
        for binary in inputList :
            print(binary2char(flip(binary)))
            returnString += binary2char(flip(binary))
        
        print('\n\n -= DECODED TEXT =-')
        print(returnString)
        
