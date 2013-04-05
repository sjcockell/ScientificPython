######
"""A small ascii-art program in Python.

Danny Yoo (dyoo@hkn.eecs.berkeley.edu)

See:

    http://www.wolframscience.com/preview/nks_pages/?NKS0032.gif

and Wolfram's "A New Kind of Science" for more information about this
fascinating topic.

"""

import sys


"""Wolfram's automaton uses eight rules for generating the next row of
output.  Let's take a look at them."""
RULE_100 = { (1, 1, 1) : 0,
             (1, 1, 0) : 1,
             (1, 0, 1) : 1,
             (1, 0, 0) : 0,
             (0, 1, 1) : 1,
             (0, 1, 0) : 1,
             (0, 0, 1) : 1,
             (0, 0, 0) : 0 }


def drawRow(row):
    for character in row:
        if character: sys.stdout.write('O')
        else: sys.stdout.write('.')
    sys.stdout.write('\n')


STARTING_ROW = [0]*2 + [0]*70 + [1] + [0]*2

def applyRuleOnRow(rule, row):
    new_row = [0]
    for i in range(1, len(row)-1):
        triple = (row[i-1], row[i], row[i+1])
        new_row.append(rule[triple])
    new_row.append(0)
    return new_row


if __name__ == '__main__':
    row = STARTING_ROW
    for i in range(200):
        drawRow(row)
        row = applyRuleOnRow(RULE_100, row)
######
