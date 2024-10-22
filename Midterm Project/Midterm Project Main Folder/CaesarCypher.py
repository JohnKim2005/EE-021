import random
from Functions import *

def shift(key, char):
    charValue = ord(char)
    if charValue >= 65 and charValue <= 90 :
        charValue += key
        if charValue > 90 :
            charValue -= 26
        if charValue < 65 :
            charValue += 26
    elif charValue >= 97 and charValue <= 122 :
        charValue += key
        if charValue > 122 :
            charValue -= 26
        if charValue < 97 :
            charValue += 26
    return chr(charValue)

def Caesar():
    """
    Caesar Cypher (Shift Cypher)
    - ✘ Encryption with Key
    - ✘ Encryption with Randomized Key
    - ✘ Decryption with Key
    - ✘ Decryption without key (Forced Decryption) - May require simple dictionary of most common words
    """
    cryption = choiceFunc('Encryption or Decryption? ( E or D )', 'E', 'D')  # Encryption Decryption Input Check



    ''' I will add Files Later If I have Time. This is just structuring.'''
    # # Input Type Input Check
    # inputType = choiceFunc('\n\nTy1ped Input or Input File? ( T or F )', 'T', 'F')
    # if inputType == 1 :
    #     inputFile = input('> ')
    # else :
    #     inputFile = open('Input.txt', 'r+')

    # # Output Type Input Check
    # outputType = choiceFunc('\n\nTerminal Output or Output File? ( T or F )', 'T', 'F')
    # if outputType == 1 :
    #     outputFile = None
    # else :
    #     outputFile = open('Output.txt', 'r+')
    ''' This is Input Until Access Is Added '''
    print('Please input the Sentence/String to be Encoded or Decoded')
    inputFile = input('> ')
    outputFile = ''


    
    if cryption == 1:  # Encryption

        # Key Type Input Check
        keyType = choiceFunc('\n\nSet key or Randomized Key? ( S or R )', 'S', 'R')

        if keyType == 1:  # Set Key
            key = keyInput('c')
            for char in inputFile :
                outputFile += shift(key, char)
            print('\n\n -= ENCODED TEXT =-')
            print(outputFile)


        elif keyType == 2:  # Randomized Key
            key = random.randint(1, 25)
            for char in inputFile :
                outputFile += shift(key, char)
            print(f'\n\n Key : {key}')
            print('\n -= ENCODED TEXT =-')
            print(outputFile)

        

    elif cryption == 2:
        # keyType = choiceFunc('\n\nSet key or Forced Decryption ( S or F )', 'S', 'F') # Key Type Input Check

        key = -1 * keyInput('c')
        for char in inputFile :
            outputFile += shift(key, char)
        print('\n\n -= DECODED TEXT =-')
        print(outputFile)

        # elif keyType == 2:
        #     print('\n\ntry to force decrypt with algorithm (Big if on if this works and makes it on to the finalized version)')
        #     print('Output the Decrypted string and Code')