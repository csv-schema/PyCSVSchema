# PyCSVSchema

PyCSVSchema is an implementation of [CSV Schema](https://github.com/csvschema/csvschema) in Python.

This project is at Alpha version and still under heavy development.

## Example

```python
>>> from pycsvschema.checker import Validator
>>> # demo.csv:
... # id,name,value
... # 1,Ann,"5"
... # 2,Ben,"10"
... # 3,Tom,"14"
>>> schema = {
...     'fields': [
...         {
...             'name': 'value',
...             'type': 'number',
...             'multipleOf': 5
...         }
...     ]
... }
>>> v = Validator(csvfile='demo.csv', schema=schema)
>>> v.validate()

Traceback (most recent call last):
...
<ValidationError: 'Value 14.0 is not multiple of 5'; column name: value; row number: 3>
```

Note that the validator does not check if the parameters for reading csv file are correct. For example, if wrong delimiter is passed in, validator is unable to figure it out and would read the whole line as one cell.

The validator does not check the CSV file against RFC 4180 strictly. As it is using Python's built-in csv module, PyCSVSchema always tries to parse the file as CSV format, even if it does not follow RFC 4180 definition. For example, if double-quotes are used to enclose fields and an unescaped double-quote appears inside a field, it conflicts with RFC 4180 but PyCSVSchema would still read the file and escape the unescaped double-quote.

## Installation

```bash
pip install pycsvschema
```

## Requirements

Python 3.5 or above


## TODO
* Documentation and Examples
* Spec updates including adding descriptive fields and adding csv meta fields
* Decide whether to rely on Python's built-in int and float function to convert values
* Tests