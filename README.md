pycodejam
=========

A [Google Code Jam](http://code.google.com/codejam) problem runner for python.

_Can I used this in the contests?_ Yes, as long as this library is open source (it is) and is openly available online (it is), it can be used without submission on each problem. Just make a comment in your code to that effect. See the [Code Jam FAQ](http://code.google.com/codejam/faq.html#tools)

[Documentation!](http://yanatan16.github.com/pycodejam/docs/html/index.html)

## Installation

```
pip install pycodejam
```

Or you can install from source:

    git clone https://github.com/yanatan16/pycodejam
    cd pycodejam
    python setup.py test && python setup.py install

`pycodejam` is now compatible with python 2.6+ and 3.x!

# Examples

There are also some examples in the [examples folder](http://github.com/yanatan16/tree/master/examples).

## A simple example

    def solve(line1, line2):
      return sum(line1) - sum(line2) # This is where you put your solution

    if __name__ == "__main__":
      from codejam import CodeJam, parsers
      CodeJam(parser.ints, solve).main()

## A complex example

    def solve(*lines):
      return sum((sum(line) for line in lines)) # This is where you put your solution
    
    @iter_parser
    def parse(nxtline):
      n = int(nxtline())
      return [nxtline() for unused in range(n)]
    
    if __name__ == "__main__":
      from codejam import CodeJam
      CodeJam(parse, solve).main()

# In Depth

## `CodeJam`

`CodeJam` is a class that provides ways to easily run a code jam problem.

The class requires two parameters to instantiate:

- parser - A generator function of one parameter (file_obj) that yields each case in a tuple.
  There are useful parsers and helpful decorators in the `codejam.parsers` module
- solver - A solver that takes the parsed case list/tuple expanded and returns a `str()`-able object to print as the answer

The usual way to use this class is to call the main() function which will interpret command line arguments
for the input file and options for debugging (-d).

## Multiprocessing

Multiprocessing is an easy way to parallelize the solving (assuming each solution is independent!). Simply pass the -m option to the command line when executing the script and multiprocessing will take care of the rest. Make sure to debug your solvers first though! Because debugging while multiprocessing is difficult.

_Note_: You must define functions at the top level of a module in order to be able to pickle them to multiprocessing workers. When in doubt, don't use multiprocessing.

## Floating Point Numbers

Code Jam problems that involve floating point numbers often require 6 decimal points of accuracy. So any float number returned from a solver will be printed like so: `'%.6f' % ans`. If a problem requires a different level of accuracy, pass the optional `floating_accuracy` parameter into the `CodeJam` constructor, which defaults to 6 for 6 digits of accuracy.

## parsers

A parser is a function of a single file object that returns a generator of case instances. Those case
instances will be fed into the solve function as expanded lists/tuples.

e.g.
    for case in parse(file):
      print(solve(*case))

The parsers module provides a decorator called `simple_parser`. Simple parsers assume each case has a equal number of lines. For problems that do not fit this description, implement your own parser. The simple parser decorator then figures out how many lines per case, and passes those lines into the parser (expanded). The module also provides a few convenience parsers that are decorated as simple_parsers: `ints`, `words` and `lines`. `ints` will pass a list of lines, each of which is a list of integers parsed from the input.

A custom parser will generally follow this outline:

    def my_custom_parser(file):
      lines = file.__iter__()
      next = lambda: lines.__next__()
    
      n = int(next().strip()) # Number of cases
      for i in range(n):
        m = int(next().strip()) # Number of lines for this case
        yield [next() for unused in range(m)]

And thats why I created the `iter_parser` which will take care of the first four lines of the above pattern and simply call your parser on each iteration of the loop:

    @iter_parser
    def parse(next):
      m = int(next().strip()) # Number of lines for this case
      return [next() for unused in range(m)] # Return here, don't yield

## helpers

The helpers module provides the `memoize` decorator, which memoizes a function with no keyword arguments using a dict object.

Example:

    @memoize
    def myfunc(a,b,c):
      return a * b * c

# License

pycodejam is licensed with the MIT license found in the LICENSE file.
