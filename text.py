from gtts import gTTS
import os
mytext = input()
language ="en"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("Audio.mp3")

