import os
import sys
import argparse
from subprocess import check_call, check_output


def main(args=sys.argv[1:]):
    '''Create a new unique branch with a numeric suffix.'''
    branch = parse_args(args).TARGET_BRANCH

    current = check_output(['git-current-branch']).rstrip()
    check_call(['git-branch-nth', '{}.prebase'.format(current)])

    subargs = ['git', 'rebase', branch]
    os.execvp(subargs[0], subargs)


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)
    p.add_argument('TARGET_BRANCH', help='Rebase target.')
    return p.parse_args(args)
