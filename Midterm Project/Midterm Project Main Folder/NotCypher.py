import random
from Functions import *


def Not():
    """
    Binary Not Cypher (01100001 -> 10011110) - Might not work as the first 32 in ascii code will break. Might have to send Encrypted and to be decrypted files in as binary
    - ✘ Encryption
    - ✘ Decryption
    """
    cryption = choiceFunc('Encryption or Decryption? ( E or D )',
                          'E', 'D')  # Encryption Decryption Input Check

    if cryption == 1:  # Encryption
        # Key Type Input Check
        keyType = choiceFunc('\n\nSet key or Randomized Key? ( S or R )', 'S', 'R')

        if keyType == 1:  # Set Key
            print('\n\nEncrypt input string with input key')
            print('Output the Encrypted string')

        elif keyType == 2:  # Randomized Key
            print('\n\nEncrypt input string with randomized key')
            print('Output the Encrypted string and Code')

    elif cryption == 2:
        # keyType = choiceFunc('\n\nSet key or Forced Decryption ( S or F )', 'S', 'F') # Key Type Input Check

        if keyType == 1:  # Key Type if/elif/else Statement
            print('\n\nDecrypt input string with input key')
            print('Output the Decrypted string')

        # elif keyType == 2:
        #     print('\n\ntry to force decrypt with algorithm (Big if on if this works and makes it on to the finalized version)')
        #     print('Output the Decrypted string and Code')
