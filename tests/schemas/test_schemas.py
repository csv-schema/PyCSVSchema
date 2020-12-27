#!/usr/bin/python
# -*-coding: utf-8 -*-

import json
import os
import unittest

import jsonschema
from pycsvschema import definitions
from tests import TEST_DIR


class TestSchemas(unittest.TestCase):
    """Test if schemas match the meta schema."""

    def setUp(self):
        with open(definitions.META_SCHEMA_PATH, "r") as meta_schema:
            self._meta_schema = json.load(meta_schema)
        self._this_dir = os.path.join(TEST_DIR, "schemas")

    def valdiate_schema(self, schema_file):
        """Open a single schema and validates it agaist the metaschema."""
        with open(schema_file, "r") as schema:
            jsonschema.validate(json.load(schema), self._meta_schema)

    def test_schema_with_annotator_keywords(self):
        filename = "schema_with_annotator_keywords.json"
        schema_file = os.path.join(self._this_dir, filename)
        self.valdiate_schema(schema_file)

    def test_schema_with_regex(self):
        filename = "schema_with_regex.json"
        schema_file = os.path.join(self._this_dir, filename)
        self.valdiate_schema(schema_file)



if __name__ == "__main__":
    unittest.main()
