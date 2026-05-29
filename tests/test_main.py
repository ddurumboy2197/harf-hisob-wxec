# test_matn.py
import pytest
from matn import matn

def test_matn():
    assert matn("Hello, World!") == 13
    assert matn("Python") == 6
    assert matn("a") == 1
    assert matn("") == 0
    assert matn("abcabcabc") == 9
