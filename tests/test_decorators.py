import pytest

from src.decorators import my_func

test_data = [
    ((7, 2), "my_func OK\n"),
    ((6, 2), "my_func ERROR: Wrong value. Inputs (6, 2) {}\n"),
    ((5, 0), "my_func ERROR: division by zero. Inputs (5, 0) {}\n"),
]


@pytest.mark.parametrize("data, expected", test_data)
def test_retry_decorator(data: tuple, expected: str, capsys: pytest.CaptureFixture[str]) -> None:
    my_func(*data)
    captured = capsys.readouterr()
    assert expected == captured.out
