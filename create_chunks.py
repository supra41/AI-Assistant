import whisper
import json
import os

model = whisper.load_model("small") 

os.makedirs("chunks", exist_ok=True)

audios = os.listdir("audios")

for audio in audios:
    # print(audio)
    if("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1][:-4]
        print(number, title)
        result = model.transcribe(audio = f"audios/{audio}",
                                  language = "hindi",
                                   task = "translate"
                                   )
        
        chunks = []
        for segment in result["segments"]:
            chunks.append({"number":number, "title": title, "start": segment["start"],
                        "end": segment["end"],
                        "text": segment["text"]})
        
        chunks_with_metadata = {"chunks": chunks, "text": result["text"]}
        with open(f"chunks/{number}_{title}.json", "w") as f:
            json.dump(chunks_with_metadata, f, indent=4)