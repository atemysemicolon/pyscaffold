# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import

import sys
import argparse

from . import structure
from . import repo


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="project",
                        help="project name",
                        metavar="NAME")
    parser.add_argument("-p", "--package",
                        dest="package",
                        required=False,
                        default=None,
                        help="package name (default: project name)",
                        metavar="NAME")
    parser.add_argument("-d", "--description",
                        dest="description",
                        required=False,
                        default="",
                        help="package description (default: '')",
                        metavar="TEXT")

    opts = parser.parse_args(args)
    if opts.package is None:
        opts.package = opts.project
    return opts


def main(args):
    args = parse_args(args)
    proj_struct = structure.make_structure(args)
    structure.create_structure(proj_struct)
    repo.init_commit_repo(args.project, proj_struct)


def run():
    """
    Entry point for setup.py
    """
    main(sys.argv[1:])


if __name__ == '__main__':
    main(sys.argv[1:])