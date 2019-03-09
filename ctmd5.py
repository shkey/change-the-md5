#!/usr/bin/env python3

import argparse
import hashlib
import os
import random
import sys

__VERSION__ = '0.1.1'
CHARACTERS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_parser():
    parser = argparse.ArgumentParser(
        description='a cli tool used to change the MD5 of files',
    )
    parser.add_argument(
        'file',
        metavar='FILE',
        type=str,
        help='the file you want to change md5',
    )
    parser.add_argument(
        '-s', '--show', action='store_true',
        help='show the md5 value'
    )
    parser.add_argument('-v', '--version',
                        action='version', version=__VERSION__)
    return parser


def get_md5(file):
    if os.path.exists(file):
        with open(file, 'rb') as f:
            md5 = hashlib.md5()
            while True:
                buffer = f.read(4096)
                if not buffer:
                    break
                md5.update(buffer)
            return md5.hexdigest()


def change_the_md5(file, show_md5=False):
    random_str = ''.join(random.choice(CHARACTERS))
    if show_md5:
        print('before: {0}'.format(get_md5(file)))
    if os.path.exists(file):
        with open(file, 'ab') as f:
            f.write(random_str.encode('utf-8'))
        print('The md5 value has been changed.')
    else:
        raise OSError('File does not exist!')
    if show_md5:
        print('after: {0}'.format(get_md5(file)))

def cli():
    args = vars(get_parser().parse_args())
    change_the_md5(file=args.get('file', None), show_md5=args.get('show', None))

if __name__ == '__main__':
    cli()
