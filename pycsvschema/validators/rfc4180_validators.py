#!/usr/bin/python
# -*-coding: utf-8 -*-

import re
from itertools import chain

from pycsvschema import defaults, exceptions, utilities

# Validators for root options
# Each validator should be a generator, accepting three parameters:
# :param header: csv header
# :param cell: cell data in dict like {'value': 1}, only for missingvalues
# :param schema: full csv schema
# :param column_validators: Validator.column_validators


# TODO: add more rfc 4180 requirements and unify the parameters of validators below
def number_of_fields(row, row_number, header_length):
    """
    RFC 4180 - Section 2. Definition of the CSV Format - 4
    Make sure each line contains the same number of fields
    """
    if len(row) != header_length:
        yield exceptions.ValidationError(message="Illegal null value", row=row_number)


RFC4180_VALIDATIONS = {
    "number_of_fields": number_of_fields,
}
