from src.decorators import log


@log()
def test_function_success(x, y):
    return x + y


@log()
def test_function_error(x, y):
    return x / y


def test_log_success(capsys):
    test_function_success(1, 2)
    captured = capsys.readouterr()
    assert "test_function_success ok" in captured.out


def test_log_error(capsys):
    test_function_error(1, 0)
    captured = capsys.readouterr()
    assert "test_function_error error: division by zero. Inputs: (1, 0), {}" in captured.out


def test_log_to_file():
    @log(filename="log.txt")
    def test_function_file_logging(x, y):
        return x + y

    test_function_file_logging(3, 4)

    with open("log.txt") as file:
        log_content = file.read()

    assert "test_function_file_logging ok" in log_content


def test_log_error_to_file():
    @log(filename="log.txt")
    def test_function_file_logging_error(x, y):
        return x / y

    test_function_file_logging_error(1, 0)

    with open("log.txt") as f:
        log_content = f.read()

    assert "test_function_file_logging_error error: division by zero. Inputs: (1, 0), {}" in log_content
