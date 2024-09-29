"""
Encryption and Decryption Program
By: John Kim



Current Progress: ( ✓ Done : □ In Progress : ✘ Not Implemented yet)

✓ Structure
✓ Main if/elif/else statements
✘ File Reading - If I have time

Caesar Cypher (Shift Cypher)
✘ Encryption with Key
✘ Encryption with Randomized Key
✘ Decryption with Key
✘ Decryption without key (Forced Decryption) - May require simple dictionary of most common words

Binary Not Cypher (01100001 -> 10011110) - Might not work as the first 32 in ascii code will break. Might have to send Encrypted and to be decrypted files in as binary
✘ Encryption
✘ Decryption

Binary Xor Cypher (01100001 + Key(10101010) -> 11001011 : 11001011 + Key(10101010) -> 01100001)
✘ Encryption with Key
✘ Encryption with Randomized Key
✘ Decryption with Key
✘ Decryption without key (Forced Decryption) - May require simple dictionary of most common words

'Cheat' Sheet :

 - ord('char') outputs ascii value of Char
 - chr(int) outputs ascii Char of that value
 - bin(int) outputs binary of the value input
 - Maybe look into the binascii python import : https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
"""
import random
import sys

# print("My Midterm project will  bean encryption and decryption. I will make encryption and decryption with a key. I will also if I have time, try to make an algorithm for forced decryption.")

while True: # Main Loop

    # while True : # Cypher Type Input Check
    #     print('What Type of Cypher? (Caesar, Not, Xor)')
    #     type = input('> ').lower()
    #     if type in ["caesar", "not", "xor"] :
    #         break
    #     print('Invalid Input Please Try again')

    while True : # Encryption Decryption Input Check
        print('Encryption or Decryption? ( E or D )')
        action = input('> ').lower()
        if action in ['e', 'd'] :
            break
        print('Invalid Input Please Try again')

    if action == 'e': # Encryption Decryption if/elif/else Statement
        while True : # Key Type Input Check
            print('\n\nSet key or Randomized Key? ( S or R )')
            setKey = input('> ').lower()
            if setKey in ['s', 'r'] :
                break
            print('Invalid Input Please Try again')
        
        if setKey == 's': # Key Type if/elif/else Statement
            print('\n\nEncrypt input string with input key')
            print('Output the Encrypted string')
        elif setKey == 'r':
            print('\n\nEncrypt input string with randomized key')
            print('Output the Encrypted string and Code')

            
    elif action == 'd':
        while True : # Key Type Input Check
            print('\n\nSet key or Forced Decryption? ( S or F )')
            setKey = input('> ').lower()
            if setKey in ['s', 'f'] :
                break
            print('Invalid Input Please Try again')
        
        if setKey == 's': # Key Type if/elif/else Statement
            print('\n\nDecrypt input string with input key')
            print('Output the Decrypted string')
        elif setKey == 'f':
            print('\n\ntry to force decrypt with algorith (Big if on if this works and makes it on to the finalized version)')
            print('Output the Decrypted string and Code')




    while True:
        cont = input("Continue? Y/N\n>").lower
        if cont == 'y':
            break
        elif cont == 'n':
            sys.exit()
        else:
            print("Invalid input. Please input either 'y' for yes and 'n' for no.")
