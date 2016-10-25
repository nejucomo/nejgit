import sys
import os


def main(args=sys.argv[1:]):
    args = [
        'git', 'difftool',
        '--dir-diff',
        '--tool=meld',
    ]
    args += args
    os.execvp(args[0], args)
