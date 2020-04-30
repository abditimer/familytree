# test_with_unittest.py
from unittest import TestCase
import pytest
from person import Person

abdi = Person('abdi', '03-05-1993', '195', '100', True)
sara = Person('sara', '04-04-1943', '155', '60', False)

def test_abdi_name():
    assert abdi.name == 'abdi'

def test_abdi_wrong_name():
    assert abdi.name != 'abdi2'

def test_abdi_wrong_name_2():
    assert abdi.name != 'Tom'

def test_sara_name():
    assert sara.name == 'sara'

def test_sara_gender():
    assert sara.get_gender() == 'Female'