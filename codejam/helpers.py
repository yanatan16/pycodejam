'''
Code Jam Problem Helpers

Author: Jon Eisen
Dec 2012
'''
from functools import wraps

def memoize(fn):
  '''Memoize a function'''
  memo = {}
  @wraps(fn)
  def memoed_fn(*args):
    try:
      return memo[args]
    except KeyError:
      val = fn(*args)
      memo[args] = val
      return val
  return memoed_fn