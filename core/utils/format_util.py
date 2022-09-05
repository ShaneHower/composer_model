import os
from pydub import AudioSegment
import glob


def _extract_file_name(path):
    split_path = path.split(os.sep)
    file_with_ext = split_path[-1]
    file_name = file_with_ext.split('.')[0]
    return file_name


def convert_mp3_to_wav(config):
    """
        This function takes the mp3 files present in core/songs/mp3 and converts them into wav files.

        Args:
            config (Config):
                The config object for the job.  This is used to pull the location of the mp3 and wav files.

        Returns:
            wav_files (List):
                A list of the converted wav files.  These will later be parsed and stored in the Song object.

    """
    mp3_files = glob.glob(f'{str(config.mp3_path)}{os.sep}*.mp3')

    wav_files = []
    for mp3_file in mp3_files:
        file_name = _extract_file_name(mp3_file)
        wav_file = config.wav_path / f'{file_name}.wav'
        wav_files.append(wav_file)

        sound = AudioSegment.from_mp3(mp3_file)
        sound.export(wav_file, format="wav")

    return wav_files
