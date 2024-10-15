import sys, winsound, time


# Part 1A
dict_music_notes_0 = { "C0": 16.35, "C#0": 17.32,   "D0": 18.35,    "D#0": 19.45,   "E0": 20.6,     "F0": 21.83,    "F#0": 23.12,   "G0": 24.5,     "G#0": 25.96,   "A0": 27.5,     "A#0": 29.14,   "B0": 30.87}
dict_music_notes_1 = { "C1": 32.7,  "C#1": 34.65,   "D1": 36.71,    "D#1": 38.89,   "E1": 41.2,     "F1": 43.65,    "F#1": 46.25,   "G1": 49.0,     "G#1": 51.91,   "A1": 55.0,     "A#1": 58.27,   "B1": 61.74}
dict_music_notes_2 = { "C2": 65.41, "C#2": 69.3,    "D2": 73.42,    "D#2": 77.78,   "E2": 82.41,    "F2": 87.31,    "F#2": 92.5,    "G2": 98.0,     "G#2": 103.83,  "A2": 110.0,    "A#2": 116.54,  "B2": 123.47}
dict_music_notes_3 = { "C3": 130.81,"C#3": 138.59,  "D3": 146.83,   "D#3": 155.56,  "E3": 164.81,   "F3": 174.61,   "F#3": 185,     "G3": 196.0,    "G#3": 207.65,  "A3": 220.0,    "A#3": 233.08,  "B3": 246.94}
dict_music_notes_4 = { "C4": 261.63,"C#4": 277.18,  "D4": 293.66,   "D#4": 311.13,  "E4": 329.63,   "F4": 349.23,   "F#4": 369.99,  "G4": 392.0,    "G#4": 415.3,   "A4": 440.0,    "A#4": 466.16,  "B4": 493.88}
dict_music_notes_5 = { "C5": 523.25,"C#5": 554.37,  "D5": 587.33,   "D#5": 622.25,  "E5": 659.25,   "F5": 698.46,   "F#5": 739.99,  "G5": 783.99,    "G#5": 830.61, "A5": 880.0,    "A#5": 932.33,  "B5": 987.77}
dict_music_notes_6 = { "C6": 1046.5,"C#6": 1108.73, "D6": 1174.66,  "D#6": 1244.51, "E6": 1318.51,  "F6": 1396.91,  "F#6": 1479.98, "G6": 1568.98,   "G#6": 1661.22,"A6": 1760.0,   "A#6": 1864.66, "B6": 1975.53}
dict_music_notes_7 = { "C7": 2093,  "C#7": 2217.46, "D7": 2349.32,  "D#7": 2489,    "E7": 2637,     "F7": 2793.83,  "F#7": 2959.96, "G7": 3136.96,   "G#7": 3322.44,"A7": 3520.0,   "A#7": 3729.31, "B7": 3951}
dict_music_notes_8 = { "C8": 4186,  "C#8": 4434.92, "D8": 4698.63,  "D#8": 4978,    "E8": 5274,     "F8": 5587.65,  "F#8": 5918.91, "G8": 6272.93,   "G#8": 6645.88,"A8": 7040.0,   "A#8": 7459.62, "B8": 7902.13}
listDict = [dict_music_notes_0, dict_music_notes_1, dict_music_notes_2, dict_music_notes_3, dict_music_notes_4, dict_music_notes_5, dict_music_notes_6, dict_music_notes_7, dict_music_notes_8]


# Part 1B
totalFrequencies = 0
for dict in listDict :
    if len(dict) != 12 :
        print("One of the Dictionaries are not 12 frequencies.")
        print(f'{dict=}')
        sys.exit()
    totalFrequencies += len(dict)
print("All dictionary lengths are the same and equal to 12")


# Part 1C
if totalFrequencies != 108 :
    print("Total Number of Frequencies is not 108.")
    sys.exit()
print("The total number of frequencies in all my dictionaries are" + str(totalFrequencies))


# Part 2
print("Enter the frequency notes you'd like to play. Your notes must be separated by spaces.")
print("For example, 'C#4 D4 E6 F1 G7 A0' is a valid input. Enter your desired notes here: ")
user_freq = input().upper()

print("Enter the weights for the notes to distinguish how important each of those notes are.")
print("Your weights must be separated by spaces and you must enter the same number of weights as notes.")
print("For example, '1 0.5 0.8 0.75 1 1' is a valid input for the previous example. Enter your desired weights here: ")
user_weights = input().upper()


# Part 2A
user_freq_list = user_freq.split(' ')
user_weights_list = user_weights.split(' ')
for i in range(len(user_weights_list)) :
    user_weights_list[i] = float(user_weights_list[i])

print("The converted list for the input notes is: ", user_freq_list)
print("The converted list for the weight values is: " , user_weights_list)


# Part 2B
if len(user_freq_list) != len(user_weights_list) :
    print("List lengths are not the same. You must enter the same number of weights and notes.")
    sys.exit()


# Part 3A
user_translated_freq_list = []
for note in user_freq_list :
    for dict in listDict :
        if note in dict :
            user_translated_freq_list.append(dict[note])
            break
print("The frequency values requested are ", user_translated_freq_list)


# Part 3B
user_weighted_freq_list = []
for i in range(len(user_weights_list)):
    user_weighted_freq_list.append(user_translated_freq_list[i]*user_weights_list[i])
print("The weighted frequency values requested are ", user_weighted_freq_list)


# Part 3C
for note in user_weighted_freq_list :
    if note < 50 or note > 12000 :
        print("Inaudible/unsafe frequencies entered. Exiting...")
        sys.exit()


# Part 4A
for freq in user_weighted_freq_list :
    winsound.Beep(int(freq), 1000)
    time.sleep(1)