import random
from datetime import datetime
from time import sleep
from typing import Callable


def log_work(func: Callable):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        function_name = func.__name__
        with open(f'./12_logs/{function_name}', mode='a') as file:
            file.write(f'time:{execution_time} result:{result}\n')
        return result

    return wrapper


@log_work
def test():
    sleep(1)
    return random.randint(6, 100)
