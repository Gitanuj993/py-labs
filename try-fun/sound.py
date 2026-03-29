"""
Welcome AT
module 1 ;
aim : to convert text message into voices ;

procedure :	
first of all we install a module called 'gtts' using command below from the terminal
>> pkg install gtts
all set then write this code into the script by hands avoid copy paste

and for complete tutorial or documentaton refer to :  https://gtts.readthedocs.io/en/

"""
# save the files in a folder to save the output and make sure that you are connected to the internet
#for the results

from gtts import gTTS
text = " text in this column will be converted into speech!"
tts = gTTS(text=text, lang='en')

tts.save("audio1.mp3")
print(" processed successfully !")

# after successfully execution you will see a file as .mp3 ready to run
