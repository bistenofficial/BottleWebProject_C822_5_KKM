import unittest
import re
from datetime import datetime

re_field = r"(^(1\.0))|(^[0]*[.][0-9]+$)|(^0)"

def fieldTest(field):
    result =  re.fullmatch(re_field, field)
    if result:
       return True
    else:
       return False