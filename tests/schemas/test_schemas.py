#!/usr/bin/python
# -*-coding: utf-8 -*-

import json
import os
import unittest

import jsonschema
from pycsvschema import definitions
from tests import TEST_DIR


class TestSchemas(unittest.TestCase):
    def test_schema_with_annotator_keywords(self):
        with open(definitions.META_SCHEMA_PATH, "r") as meta_schema:
            with open(os.path.join(TEST_DIR, "schemas/schema_with_annotator_keywords.json"), "r") as schema:
                jsonschema.validate(json.load(schema), json.load(meta_schema))


if __name__ == "__main__":
    unittest.main()
