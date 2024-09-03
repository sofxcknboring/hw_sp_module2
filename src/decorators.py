from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.
    :param filename: Имя файла для записи логов. Если не указано, логи выводятся в консоль
    :return: Функцию обертку, которая выполняет логирование.
    """

    def wrapper(func: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> None:
            message = ""
            try:
                func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"

            if filename:
                with open(filename, "a") as file:
                    file.write(message + "\n")
            else:
                print(message)

        return inner

    return wrapper
