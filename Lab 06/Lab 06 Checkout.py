dict_music_notes_0 = { "C0": 16.35, "C#0": 17.32, "D0": 18.35, "D#0": 19.45, "E0": 20.6, "F0": 21.83, "F#0": 23.12, "G0": 24.5, "G#0": 25.96, "A0": 27.5, "A#0": 29.14, "B0": 30.87}
keyList = []
freqList = []

print(len(dict_music_notes_0))

for key in dict_music_notes_0 :
    keyList.append(key)
    freqList.append(dict_music_notes_0[key])

print(len(keyList))
print(keyList)
print(len(freqList))
print(freqList)