import logging
import logging.config


def initialize_logger(log_path=None):
    """
        Configures the Python logger.

        Args:
            log_path (Path or str):
                Log file path. If omitted, no log file will be generated.
    """
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'class': 'logging.Formatter',
                'format': "%(asctime)s %(levelname)-8s %(name)-50s %(message)s"
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'filename': log_path,
                'mode': 'w'
            }
        },
        'loggers': {
            'composer_model': {
                'level': 'DEBUG',
                'handlers': ['console', 'file']
            }
        }
    }

    if log_path is None:
        del config['handlers']['file']
        del config['loggers']['composer_model']['handlers'][1]

    logging.config.dictConfig(config)
