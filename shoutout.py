import os
from gtts import gTTS

i = input("Enter your name:-")
names = [i]
for name in names:
    mytext = (f" hello {names} welcome to our program")
language = "en"

mp3 = gTTS(mytext,lang=language,slow=False)
# os.mkdir('allmp3')
mp3.save('allmp3/shoutout.mp3')
