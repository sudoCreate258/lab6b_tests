import pytest
from ..func import *

def test_add():
  assert add(1,2) ==  3
  assert add([1],[2]) == [3]
  assert add('5',1) == 6 
  assert add(True,False) != 2
  assert add([1],[2]) != [1,2]
  assert add('5', '1') != '51'
