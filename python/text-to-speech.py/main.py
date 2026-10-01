from gtts import gTTS

text="Hello Everyone Welcome to Python Coding. My Name is Astha Sachan.I am glad to announce the start of this session .pls cooperate and feel free to ask anything.i will see you guys later."

tts=gTTS(text=text, lang='en')

tts.save("voice.mp3")
print("audio saved successfully.") 