import whisper
import json

model = whisper.load_model("small")
result = model.transcribe(audio = "audios/1_lecture.mp3",
                          language = "hindi",
                           task = "translate")
# print(result["segments"])
chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment["start"],
                   "end": segment["end"],
                   "text": segment["text"]})
# print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks, f, indent=4)
