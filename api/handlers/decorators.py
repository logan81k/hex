import logging
import sys
import time
import traceback

logger = logging.getLogger(__name__)


def elapsed(f):
    def timed(*args, **kwargs):
        ts = time.time()
        result = f(*args, **kwargs)
        te = time.time()
        if 'log_time' in kwargs:
            name = kwargs.get('log_name', f.__name__.upper())
            kwargs['log_time'][name] = int((te - ts) * 1000)
        else:
            logger.debug(f"{f.__name__} {(te - ts) * 1000} ms")
            print(f"{f.__name__} {(te - ts) * 1000} ms")
        return result

    return timed


def run_handler(func):
    def wrapper(*args, **kwargs):
        result = None
        try:
            ts = time.time()
            result = func(*args, **kwargs)
            te = time.time()
            logger.debug(f"{func.__name__} {(te - ts) * 1000} ms")
            print(f"{func.__name__} {(te - ts) * 1000} ms")
        except Exception as e:
            print(f"func: {func.__name__}, {repr(e)}")
            traceback.print_stack()
        return result
    return wrapper
