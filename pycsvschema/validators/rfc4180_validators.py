#!/usr/bin/python
# -*-coding: utf-8 -*-

from pycsvschema import exceptions

# RFC 4180 Validators
# https://tools.ietf.org/html/rfc4180

# Parameter strict of csv.reader handles:
# Point 5 - wrongly quoted
# Point 7 - unescaped quote


def number_of_fields(row, row_number, header_length):
    """
    RFC 4180 - Section 2. Definition of the CSV Format
    Point 2 - too many ending line break
    Point 4 - extra comma in some lines
    Point 6 - wrongly quoted causing wrong field number in a line
    Make sure each line contains the same number of fields
    """
    if len(row) != header_length:
        yield exceptions.ValidationError(message="Illegal null value", row_number=row_number)


RFC4180_VALIDATIONS = {"number_of_fields": number_of_fields}
