import logging
from core.framework.config import Config
from core.framework.song import Song
from core.utils.format_util import convert_mp3_to_wav

log = logging.getLogger('composer_model')

def run():
    log.info('Initializing Config.')
    config = Config()

    log.info('Inputted mp3 files converted to wav.')
    wav_files = convert_mp3_to_wav(config)

    for wav_file in wav_files:
        song = Song(wav=wav_file)
