import os
from pydub import AudioSegment
import glob


def _extract_file_name(path):
    split_path = path.split(os.sep)
    file_with_ext = split_path[-1]
    file_name = file_with_ext.split('.')[0]
    return file_name
    

def convert_mp3_to_wav(config):
    mp3_files = glob.glob(f'{str(config.mp3_path)}{os.sep}*.mp3')   

    wav_files = []
    for mp3_file in mp3_files:
        file_name = _extract_file_name(mp3_file)
        wav_file = config.wav_path / f'{file_name}.wav'
        wav_files.append(wav_file)

        sound = AudioSegment.from_mp3(mp3_file)
        sound.export(wav_file, format="wav")

    return wav_files