pycodejam
=========

A Code Jam problem runner for python.

## Examples

A simple example

```python
def solve(line1, line2):
  return my_solution

if __name__ == "__main__":
  from codejam import CodeJam, parsers
  CodeJam(parser.ints, solve).main()
```

A complex example

```python
def solve(a, b, c):
  return my_solution

def parse(file):
  for line in file:
    yield [int(x) for x in line.split()]

if __name__ == "__main__":
  from codejam import CodeJam
  CodeJam(parse, solve).main()
```

The `-h` option:

```
usage: problem_solver.py [-h] [-o FILE] [-d] [-q] [-m] [-w N] FILE

Run a Generic CodeJam Problem.

positional arguments:
  FILE                  input file (A-small-practice.in for example)

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --output FILE
                        output file (defaults to input_file.out)
  -d, --debug           Add some debug output
  -q, --quiet           Quiet all output to stdout
  -m, --multiproc       Enable multiprocessing
  -w N, --workers N     Number of workers to use if multiprocessing
```

## In Depth

### `CodeJam`

`CodeJam` is a class that provides ways to easily run a code jam problem.

The class requires two parameters to instantiate:
- parser - A generator function of one parameter (file_obj) that yields each case in a tuple
  There are predominant parsers and helpful decorators in the parsers module
- solver - A solver that takes the case tuple expanded and returns a str()-able object to print as the answer

The usual way to use this class is to call the main() function which will interpret command line arguments
for the input file and options for debugging (-d).

Multiprocessing is an easy way to parallelize the solving (assuming each solution is independent!). Simply pass the -m option to the command line when executing the script and multiprocessing will take care of the rest. Make sure to debug your solvers first though! Because debugging while multiprocessing is difficult.

### parsers

A parser is a function of a single file object that returns a generator of case instances. Those case
instances will be fed into the solve function as expanded lists/tuples.

e.g.
```python
for case in parse(file):
  print(solve(*case))
```

The parsers module provides a decorator called `simple_parser`. Simple parsers assume each case has a equal number of lines. For problems that do not fit this description, implement your own parser. The simple parser decorator then figures out how many lines per case, and passes those lines into the parser (expanded). The module also provides a few convenience parsers that are decorated as simple_parsers: `ints`, `words` and `lines`. `ints` will pass a list of lines, each of which is a list of integers parsed from the input.

A custom parser will generally follow this outline:

```python
def my_custom_parser(file):
  lines = file.__iter__()
  next = lambda: lines.__next__()

  n = int(next().strip()) # Number of cases
  for i in range(n):
    m = int(next().strip()) # Number of lines for this case
    yield [next() for unused in range(m)]
```

### helpers

The helpers module provides the `memoize` decorator, which memoizes a function with no keyword arguments using a dict object.

Example:

```python
@memoize
def myfunc(a,b,c):
  return a * b * c
```