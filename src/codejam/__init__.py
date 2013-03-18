'''
This is PyCodeJam, a CodeJam runner in python!

Essentially, this package will save you time vital to CodeJam problems.

*Can I used this in the contests?* Yes, as long as this library is open source (it is) and is openly available online (it is), it can be used without submission on each problem. Just make a comment in your code to that effect. See the Code Jam FAQ_

License: pycodejam is licensed with the MIT license found in the LICENSE file.

.. _FAQ: http://code.google.com/codejam/faq.html#tools

Installation
------------

::

    pip install pycodejam

Or you can install from source::

    git clone https://github.com/yanatan16/pycodejam
    cd pycodejam
    python setup.py test && python setup.py install

Note that pycodejam is a python 3.2-compatible library and is incompatible with python 2.x. You can use a virtualenv if you have python3 on your system::

  virtualenv -p python3.2 venv
  source venv/bin/activate
  pip install pycodejam

  # Later, you can call
  deactivate # to go back to regular system-wide python

Examples
--------

A simple example::

  def solve(line1, line2):
    return sum(line1) - sum(line2) # This is where you put your solution

  if __name__ == "__main__":
    from codejam import CodeJam, parsers
    CodeJam(parser.ints, solve).main()

A complex example::

    def solve(*lines):
      return sum((sum(line) for line in lines)) # This is where you put your solution

    @iter_parser

    def parse(nxtline):
      n = int(nxtline())
      return [int(nxtline()) for unused in range(n)]

    if __name__ == "__main__":
      from codejam import CodeJam
      CodeJam(parse, solve).main()

The command line `-h` option::

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

'''

from .codejam import CodeJam
from . import parsers, helpers

__all__ = ['CodeJam', 'parsers', 'helpers']