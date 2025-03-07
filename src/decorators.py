import functools
from collections.abc import Callable
from typing import Any


def log(filename: str = "") -> Callable:
    """Logging decorator"""

    def decorator(function: Callable) -> Callable:
        def logging(message: str) -> None:
            log_sting = function.__name__ + " " + message
            if filename:
                with open(filename, "a") as f:
                    f.write(log_sting + "\n")
            else:
                print(log_sting)

        @functools.wraps(function)
        def wrapper(*args: tuple, **kwargs: tuple) -> Any:
            try:
                result = function(*args, **kwargs)
                logging("OK")
                return result
            except Exception as e:
                logging(f"ERROR: {e}. Inputs {args} {kwargs}")
                return None

        return wrapper

    return decorator


log_file = "func2.log"


@log()
def my_func(x: int, y: int) -> Any:
    if x == 6:
        raise Exception("Wrong value")
    return x / y


print(my_func(5, 0))
# print(open(filename,'r').read())
