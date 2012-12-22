
import sys
sys.path = ['../'] + sys.path # Prepend

from codejam import CodeJam, parsers, memoize
from io import StringIO
import unittest

def pickleable_solve(line):
  assert line == "1 2 3", 'Input to solve() not as expected: "%s"' % line
  return 1

class TestCodeJam(unittest.TestCase):
  input1 = '''2
1 2 3
1 2 3'''
  input2 = '''2
1 2 3
4 5
1 2 3
4 5'''
  irregular_input = '''2
3
1
2
3
4
1
2
3
4'''
  
  def test_basic(self):
    def solve(line):
      assert line == "1 2 3", 'Input to solve() not as expected: "%s"' % line
      return 1

    inf = StringIO(self.input1)
    outf = StringIO()
    CodeJam(parsers.lines, solve).run(inf, outf, silent=True)

    expout = '\n'.join(['Case #%d: 1'%i for i in [1,2]]) + '\n'
    assert outf.getvalue() == expout, "unexpected output: '%s' vs '%s'" % (outf.getvalue(), expout)

  def test_ints(self):
    def solve(line1, line2):
      assert line1 == [1,2,3], 'Input to solve() not as expected: "%s"' % str(line1)
      assert line2 == [4,5], 'Input to solve() not as expected: "%s"' % str(line2)
      return 2

    inf = StringIO(self.input2)
    outf = StringIO()
    CodeJam(parsers.ints, solve).run(inf, outf, silent=True)

    expout = '\n'.join(['Case #%d: 2'%i for i in [1,2]]) + '\n'
    assert outf.getvalue() == expout, "unexpected output: '%s' vs '%s'" % (outf.getvalue(), expout)

  def test_floats(self):
    def solve(line1, line2):
      assert line1 == [1.,2.,3.], 'Input to solve() not as expected: "%s"' % str(line1)
      assert line2 == [4.,5.], 'Input to solve() not as expected: "%s"' % str(line2)
      assert type(line1[0]) == float
      return 3.5

    inf = StringIO(self.input2)
    outf = StringIO()
    CodeJam(parsers.floats, solve).run(inf, outf, silent=True)

    expout = '\n'.join(['Case #%d: 3.500000'%i for i in [1,2]]) + '\n'
    assert outf.getvalue() == expout, "unexpected output: '%s' vs '%s'" % (outf.getvalue(), expout)

  def test_words(self):
    def solve(line):
      assert line == ["1","2","3"], 'Input to solve() not as expected: "%s"' % line
      return 4

    inf = StringIO(self.input1)
    outf = StringIO()
    CodeJam(parsers.words, solve).run(inf, outf, silent=True)

    expout = '\n'.join(['Case #%d: 4'%i for i in [1,2]]) + '\n'
    assert outf.getvalue() == expout, "unexpected output: '%s' vs '%s'" % (outf.getvalue(), expout)

  def test_bad_simple_input(self):
    def solve(*args):
      raise Exception('shouldn\'t get here')

    inf = StringIO(self.irregular_input)
    outf = StringIO()
    try:
      CodeJam(parsers.lines, solve).run(inf, outf, silent=True)
      assert False, 'should have failed here'
    except AssertionError as err:
      assert str(err).startswith('The number of lines in')

  def test_custom_parser(self):
    def solve(a, b, c):
      assert a == 1
      assert b == 2
      assert c == (1,2,3)
      return "FIVE"

    def parse(f):
      for i in range(3):
        yield (1,2,(1,2,3))

    inf = StringIO()
    outf = StringIO()
    CodeJam(parse, solve).run(inf, outf, silent=True)

    expout = '\n'.join(['Case #%d: FIVE'%i for i in [1,2,3]]) + '\n'
    assert outf.getvalue() == expout, "unexpected output: '%s' vs '%s'" % (outf.getvalue(), expout)

  def test_custom_iter_parser(self):
    def solve(n, l):
      assert len(l) == n
      return 6.1

    @parsers.custom_iter_parser
    def parse(nxt):
      n = int(nxt())
      l = [int(nxt()) for unused in range(n)]
      return (n, l)

    inf = StringIO(self.irregular_input)
    outf = StringIO()
    CodeJam(parse, solve).run(inf, outf, silent=True)

    expout = '\n'.join(['Case #%d: 6.100000'%i for i in [1,2]]) + '\n'
    assert outf.getvalue() == expout, "unexpected output: '%s' vs '%s'" % (outf.getvalue(), expout)

  def test_multiproc(self):

    inf = StringIO(self.input1)
    outf = StringIO()
    CodeJam(parsers.lines, pickleable_solve).run_multiproc(inf, outf, silent=True, workers=1)

    expout = '\n'.join(['Case #%d: 1'%i for i in [1,2]]) + '\n'
    assert outf.getvalue() == expout, "unexpected output: '%s' vs '%s'" % (outf.getvalue(), expout)

  def test_floating_accuracy(self):
    def solve(line1, line2):
      return 3.128

    inf = StringIO(self.input2)
    outf = StringIO()
    CodeJam(parsers.floats, solve, floating_accuracy=2).run(inf, outf, silent=True)

    expout = '\n'.join(['Case #%d: 3.13'%i for i in [1,2]]) + '\n'
    assert outf.getvalue() == expout, "unexpected output: '%s' vs '%s'" % (outf.getvalue(), expout)



class TestCodeJamMain(unittest.TestCase):
  def solve(self, *lines):
    assert lines == [[1,2,3]]
    return 1

  def run_basic(self, inf, outf, debug=False, silent=False):
    self.h = {'fn':'run','inf':inf,'outf':outf,'debug':debug,'silent':silent,'workers':None}

  def run_multiproc(self, inf, outf, debug=False, silent=False, workers=4):
    self.h = {'fn':'run_multiproc','inf':inf,'outf':outf,'debug':debug,'silent':silent,'workers':workers}

  def setUp(self):
    self.cj = CodeJam(parsers.ints, self.solve)
    self.cj.run = self.run_basic
    self.cj.run_multiproc = self.run_multiproc

    self.h = {s:None for s in 'fn inf outf debug silent workers'.split()}

    inf = open('test.in','w')
    inf.write('2\n1 2 3\n1 2 3')
    inf.close()

  def tearDown(self):
    pass

  def test_basic(self):
    argv = ['test.in']
    self.cj.main(argv)
    assert self.h['fn'] == 'run'
    assert self.h['inf'].name == 'test.in'
    assert self.h['inf'].read() == '''2
1 2 3
1 2 3'''
    assert self.h['outf'].name == 'test.out'
    assert self.h['silent'] == False
    assert self.h['debug'] == False

  def test_debug_silent(self):
    argv = ['test.in','-d','-q']
    self.cj.main(argv)
    assert self.h['fn'] == 'run'
    assert self.h['silent'] == True
    assert self.h['debug'] == True

  def test_outpuf_file(self):
    argv = ['test.in','-o','another.out']
    self.cj.main(argv)
    assert self.h['fn'] == 'run'
    assert self.h['outf'].name == 'another.out'

  def test_multiproc(self):
    argv = ['test.in','-m','-w','3']
    self.cj.main(argv)
    assert self.h['fn'] == 'run_multiproc'
    assert self.h['workers'] == 3

from time import sleep, time
class TestHelpers(unittest.TestCase):
  def test_memoize(self):
    @memoize
    def fn(x):
      sleep(.2)
      return 1

    assert fn(1) == 1
    start = time()
    assert fn(1) == 1
    elapsed = time() - start
    assert elapsed < 100 # ms


if __name__ == "__main__":
  unittest.main()



