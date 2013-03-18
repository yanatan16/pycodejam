'''
CodeJam 2013 Online Contest for Veterans
Problem A: Hedgemony (https://code.google.com/codejam/contest/2334486/dashboard)
Author: Jon Eisen

Execute this file like so:
python hedgemony.py /path/to/A-small-practice.in

It will print the answers, and write out the file /path/to/A-small-practice.out
'''

def solve(n, heights):
	n = n[0]
	for i in range(1, n-1):
		newheight = float(heights[i-1] + heights[i+1]) / 2
		heights[i] = min(heights[i], newheight)
	return heights[n-2]

if __name__ == "__main__":
	from codejam import CodeJam, parsers
	CodeJam(parsers.ints, solve).main()