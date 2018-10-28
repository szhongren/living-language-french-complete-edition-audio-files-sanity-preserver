import os
from mutagen import File
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TALB, TIT2, TCOM, TPE1, TPE2, TRCK
'''
first, rip all the CDs and put them into the same folder as mp3s
'''

filesDir = 'where you put all your files'
toRename = []
# this part is to find the weird ones in Intermediate disc 2 because the metadata guys were insane
for file in os.listdir(filesDir):
    if file[3:9] == 'Lesson':
        toRename.append(file)

toRename.sort()

currentNumber = 7
currentLetter = 'A'
for file in toRename:
    separator = u'•'
    nameParts = file.split(separator)
    prefix = nameParts[0]
    description = nameParts[1]
    newNumber = int(prefix.split('Lesson')[1])
    currentLetter = chr(ord(currentLetter) + 1)
    if newNumber != currentNumber:
        currentNumber = newNumber
        currentLetter = 'A'

    print('-----------------------------------')
    print(file)

    newFileName = prefix[:3] + str(newNumber) + currentLetter + description
    print(newFileName)
    os.rename(filesDir + file, filesDir + newFileName)

advanced = []
intermediate = []
essential = []
for file in os.listdir(filesDir):
    audioFile = ID3(filesDir + file)
    if 'Advanced' in file or 'Advanced' in audioFile['TALB'][0]:
        advanced.append(file)
    if 'Intermediate' in file or 'Edition' in audioFile['TALB'][0] or 'Intermediate' in audioFile['TALB'][0]:
        intermediate.append(file)
    if 'Essential' in file or 'Essential' in audioFile['TALB'][0]:
        essential.append(file)


def weirdSort(filename):
    parts = filename.split(' ')
    code = parts[1].split('\xa0')[0]
    numberPart = code[:-1]
    letterPart = code[-1:]
    return (int(numberPart), letterPart)


advanced.sort(key=weirdSort)
intermediate.sort(key=weirdSort)
essential.sort(key=weirdSort)

for i, file in enumerate(advanced):
    print(file)
    audioFile = ID3(filesDir + file)
    # print(audioFile)
    # print(audioFile.keys())
    # print(audioFile['TCOM'])
    audioFile.add(TALB(encoding=0, text=[u"French - Advanced"]))
    audioFile.add(TIT2(encoding=0, text=[file[3:-4]]))
    audioFile.add(TCOM(encoding=0, text=[u"Living Language"]))
    audioFile.add(TPE1(encoding=0, text=[u"Living Language"]))
    audioFile.add(TPE2(encoding=0, text=[u"Living Language"]))
    audioFile.add(TRCK(encoding=0, text=[str(i + 1)]))
    audioFile.save()

for i, file in enumerate(intermediate):
    print(file)
    audioFile = ID3(filesDir + file)
    # print(audioFile)
    # print(audioFile.keys())
    # print(audioFile['TCOM'])
    audioFile.add(TALB(encoding=0, text=[u"French - Intermediate"]))
    audioFile.add(TIT2(encoding=0, text=[file[3:-4]]))
    audioFile.add(TCOM(encoding=0, text=[u"Living Language"]))
    audioFile.add(TPE1(encoding=0, text=[u"Living Language"]))
    audioFile.add(TPE2(encoding=0, text=[u"Living Language"]))
    audioFile.add(TRCK(encoding=0, text=[str(i + 1)]))
    audioFile.save()

for i, file in enumerate(essential):
    print(file)
    audioFile = ID3(filesDir + file)
    # print(audioFile)
    # print(audioFile.keys())
    # print(audioFile['TCOM'])
    audioFile.add(TALB(encoding=0, text=[u"French - Essential"]))
    audioFile.add(TIT2(encoding=0, text=[file[3:-4]]))
    audioFile.add(TCOM(encoding=0, text=[u"Living Language"]))
    audioFile.add(TPE1(encoding=0, text=[u"Living Language"]))
    audioFile.add(TPE2(encoding=0, text=[u"Living Language"]))
    audioFile.add(TRCK(encoding=0, text=[str(i + 1)]))
    audioFile.save()
