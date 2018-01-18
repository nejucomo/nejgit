import sys
import re
import itertools
import argparse
import subprocess


def main(args=sys.argv[1:]):
    '''Create a new unique branch with a numeric suffix.'''
    base = parse_args(args).BRANCH_BASE
    for n in itertools.count():
        candidate = '{}.{}'.format(base, n)
        try:
            stdoutput = subprocess.check_output(
                ['git', 'branch', candidate],
                stderr=subprocess.STDOUT,
            )
        except subprocess.CalledProcessError as e:
            if RGX_ALREADY_EXIST.match(e.output):
                continue
            else:
                sys.stderr.write(e.output)
                sys.exit(e.returncode)
        if stdoutput == '':
            print candidate
            raise SystemExit()
        else:
            raise SystemExit(
                '{} unexpected output: {!r}'
                .format(sys.argv[0], stdoutput)
            )


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)
    p.add_argument('BRANCH_BASE', help='Branch base.')
    return p.parse_args(args)


RGX_ALREADY_EXIST = re.compile(
    r"^fatal: A branch named '[^']+' already exists.$",
)
