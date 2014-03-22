#!/usr/bin/env python
# encoding: utf-8
import glob
from collections import namedtuple

exp_names = ['mono', 'tri1', 'tri2a', 'tri2b', 'tri2b_mmi', 'tri2b_mmi_b','tri2b_mpe']
Experiment = namedtuple('Experiment', exp_names)
LM = namedtuple('LM', ['bigram', 'zerogram'])


def extractResults(f):
    with open(f, 'r') as r:
        lines = r.readlines()[1:]
        assert len(lines) == 2 * len(exp_names), 'Log %s should contain all experiments for zerogram and bigram' % f
        build0 = []
        for exp, line in zip(exp_names, lines[:len(exp_names)]):
            assert exp in line, 'The line in log file should start with experiments name %s' % exp
            lm, lmw, wer, ser = line.split()[2:]
            assert lm == 'build0', 'First experiments should be tested on zerogram LM'
            build0.append(wer)
        build2 = []
        for exp, line in zip(exp_names, lines[len(exp_names):]):
            assert exp in line, 'The line in log file should start with experiments name %s' % exp
            lm, lmw, wer, ser = line.split()[2:]
            assert lm == 'build2', 'First experiments should be tested on bigram LM'
            build2.append(wer)
    TODO init namedtuple  from list
    return (build0, build2)


def main():
    logs = glob.glob('data/*every*.log')
    for f in logs:
        every_n = f[-6:-4]
        zerogram, bigram = extractResults(f) 

if __name__ == '__main__':
    main()
