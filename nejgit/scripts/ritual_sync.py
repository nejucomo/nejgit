import sys
import argparse
from subprocess import check_call


def main(args=sys.argv[1:]):
    '''Ritual Sync: pull --rebase and push current branch.'''
    opts = parse_args(args)
    check_call(['git', 'pull', '--rebase', opts.REMOTE, opts.BRANCH])
    check_call(['git', 'push', opts.REMOTE, opts.BRANCH])


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)
    p.add_argument('REMOTE')
    p.add_argument('BRANCH')
    return p.parse_args(args)
