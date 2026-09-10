from gtts import gTTS
from gtts import gTTS

text = "hello Romeo, welcome to practice test python coding!"

tts = gTTS(text=text, lang='en')

tts.save("voice.mp3")

print("audio saved successfully")
