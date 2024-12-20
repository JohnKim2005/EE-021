def choiceFunc(question: str, choice1: str, choice2: str, choice3: str = None):
    """
    Returns the number of the choice made.
    Can take 2 or 3 choice inputs. - Must have at least 2 choices
    """
    print(question)
    while True:
        choice = input('> ').lower()
        if choice == choice1.lower():
            return 1
        elif choice == choice2.lower():
            return 2
        elif choice == choice3.lower():
            return 3
        else:
            if choice3 == None:
                print(f"Invalid Input. Please enter ( {
                      choice1} or {choice2} ).")
            else:
                print(f"Invalid Input. Please enter ( {
                      choice1} or {choice2} or {choice3} ).")


def nl():
    """
    Quick Line Skip.
    """
    print('')


def keyInput(type: str):
    """
    Key Input Function
    - Takes a 'c' for Caesar Cypher Key of 1~25
    - Takes a '8' for a 8 bit input for Not Xor Cyphers

    returns :
    - a number from 1~25
    - a list of 8 binary bits
    """
    if type.lower() == 'c':
        print('\n\nPlease type a number from 1~25 to be a Caesar Shift Value.')

        while True:
            choice = input('> ')
            try:
                choice = int(choice)
                if choice > 25 or choice < 1:
                    print("Invalid Input. Please enter a Number from 1~25.")
                else:
                    return choice
            except ValueError:
                print("Invalid Input. Please enter a Number from 1~25.")

    elif type.lower() == '8':
        print('\n\nPlease type a 8 bit binary number to be a Key for your Cypher')
        while True:
            bitlist = []
            choice = input('> ').strip().replace(' ', '')
            if len(choice) != 8 : 
                print("Invalid Input. Please enter a 8 bit binary number 1")
            else:
                invalid = False
                for char in choice :
                    if char not in ['0','1'] :
                        invalid = True
                        break
                    bitlist.append(char)
                if invalid :
                    print("Invalid Input. Please enter a 8 bit binary number 2")
                else :
                    return bitlist

    else :
        raise ValueError('Invalid Input into keyInput Function')
    

def bitInput():
    '''
    Takes an Input from User and Returns a list of 8 bit binary Numbers
    '''
    print('\n\nPlease input the binary you want to en/decode.')
    while True :
        binaryInput = input('> ').replace(' ', '')
        inputValid = True
        bitlist = []
        eightBit = ''
        if len(binaryInput)%8 != 0 :
            print("Invalid Input. Please Try again with a string of 8 bit Binary input made of 0's and 1's.")
            inputValid = False
        else :
            for char in binaryInput :
                if char not in ['0','1'] :
                    print("Invalid Input. Please Try again with a string of 8 bit Binary input made of 0's and 1's.")
                    inputValid = False
                    break
                eightBit += char
                if len(eightBit) == 8 :
                    bitlist.append(eightBit)
                    eightBit = ''
            if inputValid :
                return bitlist
            

def char2binary(char:str) :
    '''
    Char -> Binary (8 Bit)
    '''
    return format(ord(char), '08b')


def binary2char(binary:str) :
    '''
    Binary (8 Bit) -> Char
    '''
    return chr(int(binary,2))


