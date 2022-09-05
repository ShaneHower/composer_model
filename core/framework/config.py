from pathlib import Path

class Config:
    def __init__(self):
        """
            Environment specific configurations

            Note:
                Config represents all internal settings that a user should not be allowed to modify
                directly.  In this case, we are using the config object to store the mp3 and wav paths.

            Attributes:
                song_dir (Path):
                    The parent folder that holds mp3 and wav subfolders

                mp3_path (Path):
                    The directory which holds the inputted mp3 files for training.

                wav_path (Path):
                    The directory which holds the wav files which were converted from the inputted
                    mp3s.  These will be used to train the model as we can more easily pull meta data
                    about the song using wav format.

        """
        self.song_dir = Path('core', 'songs')
        self.mp3_path = self.song_dir / 'mp3'
        self.wav_path = self.song_dir / 'wav'
