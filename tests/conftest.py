from datetime import datetime
from typing import List

import pytest


@pytest.fixture
def dates() -> List:
    return [
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
        ("20", f'20.{datetime.now().strftime("%m")}.{datetime.now().year}'),
        ("20.03", f'20.{datetime.now().strftime("%m")}.{datetime.now().year}'),
        ("20.03", f'20.{datetime.now().strftime("%m")}.{datetime.now().year}'),
        ("20-00-12", "Wrong input date"),
        ("text", "Wrong input date"),
    ]
