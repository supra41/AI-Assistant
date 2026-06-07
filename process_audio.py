import os

audio_folder = "audios"

files = os.listdir(audio_folder)

# Sort files so numbering is consistent
files.sort()

for i, file in enumerate(files, start=1):

    old_path = os.path.join(audio_folder, file)

    new_name = f"{i}_lecture.mp3"

    new_path = os.path.join(audio_folder, new_name)

    os.rename(old_path, new_path)

    print(f"Renamed: {file} -> {new_name}")
