##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

from __future__ import print_function
import argparse
import os
import sys

import simpledb_dev
from simpledbdev2 import __description__, __project_name__, __version__
from simpledbdev2.config import Config

def _do_serve(config, args):
    simpledb_dev.run_simpledb(("0.0.0.0", args.port))

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

    args = parser.parse_args(argv)
    args.func(config, args)

if __name__ == "__main__":
    _main()
