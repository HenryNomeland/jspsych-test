from pydub import AudioSegment
import os

combined_file_list = [f for f in os.listdir("combined_audio") if os.path.isfile(os.path.join("combined_audio", f))]
for f in combined_file_list:
    os.remove(f)

file_list = [f for f in os.listdir("audio") if os.path.isfile(os.path.join("audio", f))]
child_list = []
for f in file_list:
    child = f.split("s")[0]
    if child not in child_list:
        child_list.append(child)

for child in child_list:
    s5T02 = AudioSegment.from_wav(os.path.join("audio", f"{child}s5T02.wav"))
    s5T03 = AudioSegment.from_wav(os.path.join("audio", f"{child}s5T03.wav"))
    s5T06 = AudioSegment.from_wav(os.path.join("audio", f"{child}s5T06.wav"))
    combined_sounds = s5T02 + s5T03 + s5T06
    combined_sounds.export(os.path.join("combined_audio", f"{child}.wav"), format="wav")