"""
Encryption and Decryption Program
By: John Kim



Current Progress: ( ✓ Done : □ In Progress : ✘ Not Implemented yet)

✓ Structure
✓ Main if/elif/else statements
✘ File Reading - If I have Time

Caesar Cypher (Shift Cypher)
✓ Encryption with Key
✓ Encryption with Randomized Key
✓ Decryption with Key
✘ Decryption without key (Forced Decryption) - May require simple dictionary of most common words

Binary Not Cypher (01100001 -> 10011110) - Might not work as the first 32 in ascii code will break. Might have to send Encrypted and to be decrypted files in as binary
✓ Encryption
✓ Decryption

Binary Xor Cypher (01100001 + Key(10101010) -> 11001011 : 11001011 + Key(10101010) -> 01100001)
✓ Encryption with Key
✓ Encryption with Randomized Key
✓ Decryption with Key
✘ Decryption without key (Forced Decryption) - May require simple dictionary of most common words

'Cheat' Sheet :
 - ord('char') outputs ascii value of Char
 - chr(int) outputs ascii Char of that value
 - bin(int) outputs binary of the value input
 - Maybe look into the binascii python import : https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
"""
import sys
from Functions import *
from CaesarCypher import *
from XorCypher import *
from NotCypher import *

while True:  # Main Loop

    Cypher = choiceFunc('What type of Cypher would You Like? ( Caesar, Not, Xor )', 'Caesar', 'Not', 'Xor')

    if Cypher == 1:
        Caesar()
    elif Cypher == 2:
        Not()
    else:
        Xor()

    # Continue or Exit Check
    if choiceFunc('Continue? Y/N\n>', 'Y', 'N') == 2:
        sys.exit()