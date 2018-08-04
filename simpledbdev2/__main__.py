##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

from __future__ import print_function
import argparse
import os
import unittest
import sys

from . import simpledb_dev
from simpledbdev2 import __description__, __project_name__, __version__
from simpledbdev2.config import Config
from simpledbdev2.tests import suite

def _do_serve(config, args):
    simpledb_dev.run_simpledb(("0.0.0.0", args.port), config.data_dir)

def _do_test(config, args):
    unittest.TextTestRunner(verbosity=2).run(suite())

def _main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    config_dir = os.path.abspath(os.path.expanduser(os.environ.get("SIMPLEDB_DEV2_DIR", "~/.simpledb-dev2")))
    config = Config(config_dir)

    parser = argparse.ArgumentParser(prog=__project_name__, description=__description__)
    parser.add_argument("--version", action="version", version="{} version {}".format(__project_name__, __version__))

    subparsers = parser.add_subparsers(help="Subcommand help")

    serve_parser = subparsers.add_parser("serve", help="Serve SimpleDB API")
    serve_parser.set_defaults(func=_do_serve)
    serve_parser.add_argument(
        "--port",
        "-p",
        type=int,
        default=8080,
        help="Port number")

    test_parser = subparsers.add_parser("test", help="Run all unit tests and doctests")
    test_parser.set_defaults(func=_do_test)

    args = parser.parse_args(argv)
    args.func(config, args)

if __name__ == "__main__":
    _main()
