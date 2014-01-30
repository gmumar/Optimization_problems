#!/usr/bin/env python

import sys
import solver

def read_graph(stream):
    n = int(stream.readline())
    for ln in stream:
        yield map(int, ln.split())

def plot_graph(points, walk):
    print "graph G {\n  node [shape=point, fixedsize=true];"
    for (i, (x, y)) in enumerate(points, 1):
        print '  %d [label="", pos="%d,%d!"];' % (i, x, y)
    prev = walk[-1]
    for i in walk:
        print "  %d -- %d;" % (prev + 1, i + 1)
        prev = i
    print "}"

def main(alg_name, fname):
    with file(fname) as stream:
        func = solver.solveIt(fname)
        points = list(read_graph(stream))
        plot_graph(points, func(points))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])