#!/usr/bin/python
# -*-coding: utf-8 -*-

from pycsvschema import exceptions

# RFC 4180 Validators
# https://tools.ietf.org/html/rfc4180

# TODO: add more rfc 4180 requirements and unify the parameters of validators below


def number_of_fields(row, row_number, header_length):
    """
    RFC 4180 - Section 2. Definition of the CSV Format - 4
    Make sure each line contains the same number of fields
    """
    if len(row) != header_length:
        yield exceptions.ValidationError(message="Illegal null value", row_number=row_number)


RFC4180_VALIDATIONS = {
    "number_of_fields": number_of_fields,
}
