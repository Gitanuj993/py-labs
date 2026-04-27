# Aim : to convert text message into voices ;

procedure :	

### first of all we install a module called 'gtts' using command below from the terminal
`` pkg install gttsa``
> [!important]
> Try to write code manually avoid copy paste , for actual learning insights !

> [!note]
> For complete tutorial or documentaton refer to :  https://gtts.readthedocs.io/en/



# save the files in a folder to save the output and make sure that you are connected to the internet

```text
📦 gTTS package size
Download size (from PyPI): ~20–30 KB
Installed size: ~100–200 KB (approx.)

So it’s a lightweight package—it doesn’t include heavy models because it uses Google’s online Text-to-Speech service instead of running locally.
```


## Python code !
```python

from gtts import gTTS
text = " Hello r!"
tts = gTTS(text=text, lang='en')

tts.save("audio1.mp3")
print(" processed successfully !")

```
> [!note]
> after successfully execution you will see a file as .mp3
> ready to run
