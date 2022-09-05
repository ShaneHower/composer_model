import logging 
from core.framework.control_job import run
from core.utils.logging_utils import initialize_logger

log = logging.getLogger('composer_model.main')

if __name__ == '__main__':
    initialize_logger()
    try: 
        run()
        log.info('Success!')
    except Exception as e:
        log.exception('Error')
        raise e
