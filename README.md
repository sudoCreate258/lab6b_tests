# lab6b_tests

## Objectives:
Apply simple functions and tests provide at least 3 pass / fail cases.
Updates in the add function required type casting parameters (x,y)
```
i.e., # add takes two parameters and returns the sum
# there exists room to refactor (update) add
def add(x,y):
  return x + y

def test_add():
  assert add(1,2) ==  3
  assert add([1],[2]) == [3]
  assert add('5',1) == 6 
  assert add(True,False) != 2
  assert add([1],[2]) != [1,2]
  assert add('5', '1') != “51”
```
TODO: Update this README.md file with instructions about each function.
