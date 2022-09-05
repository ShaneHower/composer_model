import json
import logging
import numpy as np
import wave

log = logging.getLogger('composer_model')

class Song:
    def __init__(self, wav):
        file = wave.open(str(wav), 'r')

        self.frames = file.getnframes()
        self.frame_rate = file.getframerate()
        self.channels = file.getnchannels()
        self.getsamplewidth = file.getsampwidth()
        self.audio_length = self.frames/self.frame_rate

        # convert sound wave to numpy array
        signal_wave = file.readframes(self.frames)
        self.signal_array = np.frombuffer(signal_wave, dtype=np.int16)

        file.close()
        self.to_log()
    
    def to_log(self):
        for key, value in vars(self).items():
            value = json.dumps(value, indent=4) if isinstance(value, dict) else value
            log.debug(f'song {key} = {value}')
