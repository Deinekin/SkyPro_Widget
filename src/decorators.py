import functools
from typing import Callable, Any
from datetime import datetime


def log(*, filename: str = "") -> Callable:
    """
    Декоратор, логирующий вызов функций.
    :param filename: файл для записывания логов, если не указан - логи пишутся в консоль
    :return: задекорированная функция
    """
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Callable:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                log_msg = f"{now} {func.__name__} ok\n"
            except Exception as e:
                log_msg = f"{now} {func.__name__} error: {type(e).__name__}. Inputs: {args} {kwargs}\n"
                result = None
            if filename:
                with open(filename, "a") as f:
                    f.write(log_msg)
            else:
                print(log_msg)
            return result
        return inner
    return wrapper
