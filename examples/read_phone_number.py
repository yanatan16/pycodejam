## CodeJam China New Graduate Test
##
## Created as an example to use pycodejam
#

## Import CodeJam and parsers
from codejam import CodeJam, parsers

from itertools import imap, chain

## Custom parser!
## next is a function which returns the next line of the file
@parsers.iter_parser
def parse(next):
  '''
  Each line of input looks like:
  1234567890 3-3-5
  We must get a string of the first token and integers of the second
  '''
  number, groups = next().strip().split(' ')
  return number, map(int, groups.split('-'))

def solve(number, groups):
  '''
  Given the phone number and the groupings,
  find the english way to say the number
  '''
  grps = groupby(number, groups)
  pairgrps = imap(rollup, grps)
  pairs = chain.from_iterable(pairgrps)
  words = wordify(pairs)
  return ' '.join(words)

def groupby(arr, groups):
  while len(groups) > 0:
    g, groups = groups[0], groups[1:]
    tmp, arr = arr[:g], arr[g:]
    yield tmp

def rollup(arr):
  tmp, cnt = None, 1
  for a in arr:
    if tmp and tmp == a:
      cnt += 1
    else:
      if tmp:
        yield (tmp, cnt)
      tmp, cnt = a, 1
  yield (tmp, cnt)

def wordify(pairs):
  for n, c in pairs:
    if c == 1:
      yield english[n]
    elif c <= 10:
      yield modifiers[c]
      yield english[n]
    else:
      for i in range(c):
        yield english[n]

english = {
  '0': 'zero',
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four',
  '5': 'five',
  '6': 'six',
  '7': 'seven',
  '8': 'eight',
  '9': 'nine'
}

modifiers = {
  2: 'double',
  3: 'triple',
  4: 'quadruple',
  5: 'quintuple',
  6: 'sextuple',
  7: 'septuple',
  8: 'octuple',
  9: 'nonuple',
  10: 'decuple'
}


if __name__ == "__main__":
  ## Important, we have run the problem!
  CodeJam(parse, solve).main()