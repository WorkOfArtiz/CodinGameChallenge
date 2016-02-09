#!/usr/bin/env python
import sys, re

regex = re.compile("\[(.*?)\]")
last = None

for line in sys.stdin:
    if line[0] != 't':
        continue
    vec_line = regex.findall(line)[0]
    v = [ tuple(map(int, vec_lit.split(","))) for vec_lit in vec_line.split("|")]
    print(v)

