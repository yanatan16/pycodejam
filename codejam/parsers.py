'''
Code Jam Problem Parsers

Author: Jon Eisen
Dec 2012
'''
from functools import wraps

def simple_parser(parse):
  '''
  Simple parsers have a constant number of lines per case.
  This decorator implies that number and calls the decorated function
  with an expanded list of lines
  '''
  @wraps(parse)
  def parse_wrap(f):
    lines = list(f.__iter__())
    n, lines = int(lines[0].strip()), lines[1:]

    tot = len(lines)
    assert tot % n == 0, '''The number of lines in the file 
    must be one more than divisible by N, the number on the first line to use a simple_parser'''
    per = int(round(tot / n))

    li = lines.__iter__()
    nxt = lambda: li.__next__().strip()
    grouped_lines = ([nxt() for i in range(per)] for j in range(n))

    for group in grouped_lines:
      yield parse(*group)
  return parse_wrap
    
def split_cast_parser(cast):
  '''A split_cast_parser is a simple_parser that splits each line into words then casts them'''
  @wraps(cast)
  @simple_parser
  def sc_parser(*lines):
    return [[cast(x) for x in line.split()] for line in lines]
  return sc_parser

@split_cast_parser
def ints(x):
  '''Simple parser that returns all integers as an array of arrays'''
  return int(x)

@split_cast_parser
def words(x):
  '''Simple parser that returns all words as an array of arrays'''
  return str(x)

@split_cast_parser
def floats(x):
  '''Simple parser that returns all floats as an array of arrays'''
  return float(x)

@simple_parser
def lines(*lines):
  '''Simple parser that returns each line as an array'''
  return lines

def custom_iter_parser(fn):
  '''A decorator that will pass a function to return the next line of input. 
  The decorated function will be called for each case and should return (not yield) the case tuple'''
  @wraps(fn)
  def custom_iter_parser_wrap(file):
    lines = file.__iter__()
    next = lambda: lines.__next__().strip()

    n = int(next()) # Number of cases
    for i in range(n):
      yield fn(next)
  return custom_iter_parser_wrap

