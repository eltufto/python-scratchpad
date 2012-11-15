from mock import patch, MagicMock, call
import pytest
from utils import UdevWrapper
import pyudev
import dumb_file

def test_my_dumb_method_works():
    input_value = 2
    result_value = dumb_file.dumb_method(input_value)
    expected_value = 6
    assert result_value == expected_value
