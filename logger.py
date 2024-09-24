import json
import logging
import inspect

from datetime import datetime

def log_event(job, step, message='', level='info'):
    '''
    Logs an event with the given parameters.

    :param job: Name of the job.
    :param step: The current step of the job.
    :param message: A descriptive message about the event.
    :param level: The logging level ('info' or 'error').
    '''
    log_entry = {
        'job': job,
        'step': step,
        'message': message,
        'timestamp': datetime.now().isoformat()
    }
    log_message = json.dumps(log_entry)

    if level == 'info':
        logging.info(log_message)
    elif level == 'error':
        logging.error(log_message)

def log_info(step, message=''):
    '''
    Logs an info event.

    :param job: Name of the job.
    :param step: The current step of the job.
    :param message: A descriptive message about the event.
    '''
    log_event(inspect.stack()[1].function, step, message, level='info')

def log_error(step, message):
    '''
    Logs an error event.

    :param job: Name of the job.
    :param step: The current step of the job.
    :param message: A descriptive message about the event.
    '''
    log_event(inspect.stack()[1].function, step, message, level='error')
