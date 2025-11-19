
import pytest
from temp_para import temp_conv  # Source_code.py must exist in same folder

@pytest.mark.parametrize("celsius, expected", [
    (0, 32),
    (100, 212),
    (-40, -40),
    (37, 98.6),
    (25.5, 77.9),
    (-273.15, -459.67)
])
def test_temp_conv(celsius, expected):
    result = temp_conv(celsius)
    assert result == expected


