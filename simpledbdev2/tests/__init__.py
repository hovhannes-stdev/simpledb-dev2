##################################################
# Copyright (C) 2017, All rights reserved.
##################################################

from __future__ import print_function
import doctest
import importlib
import pkgutil
import unittest

def _get_module_names(package_name):
    return ["{}.{}".format(package_name, name) for _, name, _ in pkgutil.walk_packages([package_name])]

def _get_doctest_suite(imported_module):
    try:
        return doctest.DocTestSuite(imported_module)
    except ValueError:
        return

def suite():
    test_suite = unittest.TestSuite()
    for module_name in _get_module_names("simpledbdev2"):
        imported_module = importlib.import_module(module_name)

        unittest_suite = unittest.TestLoader().loadTestsFromModule(imported_module)
        if unittest_suite is not None:
            test_suite.addTests(unittest_suite)

        doctest_suite = _get_doctest_suite(imported_module)
        if doctest_suite is not None:
            test_suite.addTests(doctest_suite)

    return test_suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())