from pathlib import Path

class Config:
    def __init__(self):
        self.song_dir = Path('core', 'songs') 
        self.mp3_path = self.song_dir / 'mp3'
        self.wav_path = self.song_dir / 'wav'