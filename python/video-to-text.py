import whisper

model=whisper.load_model("base")

result=model.transcriber("voice.mp3")

print(result["text"])