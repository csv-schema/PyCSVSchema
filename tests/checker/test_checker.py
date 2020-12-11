#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import json
import os
import unittest

from pycsvschema.checker import Validator
from tests import TEST_DIR

def validate(csv_file, schema_file):
    """Validate a CSV file against a given schema file."""
    with open(schema_file, "r") as schema_stream:
        schema = json.load(schema_stream)
    v = Validator(csvfile=csv_file, schema=schema)
    v.validate()

class TestChecker(unittest.TestCase):
    """Test that a given csv and schema pair rent the expected result."""

    def setUp(self):
        self._this_dir = os.path.join(TEST_DIR, "checker")

    def test_example1(self):
        """Test the example from https://github.com/csv-schema/csv-schema."""
        schema_file = os.path.join(self._this_dir, "schema.json")
        csv_file = os.path.join(self._this_dir, "example.csv")
        validate(csv_file, schema_file)


if __name__ == "__main__":
    unittest.main()
