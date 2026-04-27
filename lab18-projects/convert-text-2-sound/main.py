"""
Welcome AT
module 1 ;
aim : to convert text message into voices ;

"""
from gtts import gTTS
text = " Hello r!"
tts = gTTS(text=text, lang='en')

tts.save("audio1.mp3")
print(" processed successfully !")
