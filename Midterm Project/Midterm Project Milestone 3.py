print("My Midterm project will be an encryption and decryption. I will make encryption and decryption with a key. I will also if I have time, try to make an algorithm for forced decryption.")

print('\n\nEncryption or Decryption? ( E or D )')
var1 = input('> ').lower()
if var1 == 'e' :
    print('\n\nSet key or Randomized Key? ( S or R )')
    var2 = input('> ').lower()
    if var2 == 's' :
        print('\n\nEncrypt input string with input key')
        print('Output the Encrypted string')
    elif var2 == 'r' :
        print('\n\nEncrypt input string with randomized key')
        print('Output the Encrypted string and Code')
    else :
        print('No')
elif var1 == 'd' :
    print('\n\nSet key or Forced Decryption? ( S or F )')
    var2 = input('> ').lower()
    if var2 == 's' :
        print('\n\nDecrypt input string with input key')
        print('Output the Decrypted string')
    elif var2 == 'f' :
        print('\n\ntry to force decrypt with algorith (Big if on if this works and makes it on to the finalized version)')
        print('Output the Decrypted string and Code')
    else :
        print('No')
else :
    print('No')