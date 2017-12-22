# simpledb-dev2

[![View on PyPI](https://img.shields.io/pypi/v/simpledb-dev2.svg)](https://pypi.python.org/pypi/simpledb-dev2)
[![Licence](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://raw.githubusercontent.com/rcook/simpledb-dev2/master/LICENSE)

This is a fork of [SimpleDB/dev][simpledb-dev] by Matthew Painter via [this unofficial mirror][latortuga]. This fork has been renamed to _simpledb-dev2_ so that it does not collide with the original project.

It currently supports the "2007-11-07" SimpleDB API level but has been hacked to fake support for "2009-04-15"&mdash;this has not been tested much!

## Project information

simpledb-dev2 provides a local SimpleDB server, so you can develop offline, without requiring a SimpleDB account. It has been tested on Linux, macOS and Windows.

This package currently implements:

* The whole "2007-11-07" REST API
* Correct HTTP error responses as per the technical documentation
* A large suite of tests created from the examples provided in the technical documentation

It does not implement:

* The SOAP API
* Authentication&mdash;signature value checking
* Timestamp format and expiration checking
* HTTPS

To run the simpledb-dev2 server, you'll need a working Python 2.7 installation. You can install using [pip][pip] as follows:

```
pip install simpledb-dev2
```

This will install the package and its dependencies including [web.py][web-py]. Specify the `--user` option to the `pip` command line to install for the current user only.

This will create a `simpledb-dev2` script/executable on your path. You can start the simpledb-dev2 web server as follows:

```
simpledb-dev2 serve
```

This will serve the SimpleDB API on the default port of 8080. To specify an alternative port, use the `--port` option:

```
simpledb-dev2 serve --port 1234
```

If the server doesn't start, or you have other problems, it's pretty easy to run the tests and see some examples of request/response:

```
simpledb-dev2 test
```

Remember, this is a development tool, and not meant for storing or querying large amounts of data&mdash;I do not know yet how big you can get before running into issues, but I suspect that with the current storage and querying design it is not that large :o) Now that I have a base, I may start trying to see how I can improve the performance&hellip;

Although this conforms to the specifications in the technical documentation, simpledb-dev2 has not been tested with every possible SDB client library, and I am looking forward to people in the OSS community trying to find bugs and peculiarities&mdash;it is after all, a work in progress!

_So enjoy developing your SimpleDB applications now, not later!_

## Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added support for the new API version"`)
4. Push to an upstream branch (`git push -u origin feature-branch`)
5. Create a [pull request][pulls] describing your fix/feature

## Licence

Released under [GNU General Public License v3 (GPLv3)][licence]

[latortuga]: https://github.com/latortuga/simpledb-dev
[licence]: LICENSE
[pip]: https://pip.pypa.io/
[pulls]: https://github.com/rcook/simpledb-dev2/pulls
[simpledb-dev]: http://code.google.com/p/simpledb-dev/
[web-py]: http://webpy.org/
