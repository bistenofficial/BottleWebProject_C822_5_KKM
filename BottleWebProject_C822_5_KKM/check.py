import unittest
import re
from datetime import datetime

re_field = r"^\d.\d{1,5}$"

def fieldTest(field):
    result =  re.match(re_field, field) is not None
    return result