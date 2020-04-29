# test_with_unittest.py
from unittest import TestCase
import pytest
from person import Person

def test_name_true():
    abdi = Person('abdi', '03-05-1993', '195', '100', True)
    assert abdi.name == 'abdi'

def test_name_check():
    abdi = Person('abdi', '03-05-1993', '195', '100', True)
    assert abdi.name != 'abdi2'

def test_name_false():
    abdi = Person('abdi', '03-05-1993', '195', '100', True)
    assert abdi.name != 'Tom'