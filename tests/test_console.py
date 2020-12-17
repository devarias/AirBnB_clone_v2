#!/usr/bin/python3
"""Test File for Console"""
import unittest
import pep8


class tests_Console(unittest.TestCase):
    """Unittest"""

    def test_pep8_conformance(self):
        """test PEP8 for console.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """test PEP8 for the test of console.py"""
        p = pep8.StyleGuide(quiet=True)
        result = p.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """test docstring of the console.py"""
        self.assertIsNot("console".__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len("console".__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """tests docstring of the HBNBCommand classes"""
        self.assertIsNot("HBNBCommand".__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len("HBNBCommand".__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
