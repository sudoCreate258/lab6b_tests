#!/usr/bin/python3

def add(x,y):
  try:
    x,y = int(x),int(y)
  except TypeError:
    pass
  return x + y
