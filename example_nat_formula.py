# from pysmt.smtlib.parser import get_formula
from pysmt.smtlib.parser import get_formula
from io import StringIO

smtlib_content = """
(declare-fun x () Nat)
(assert (> x 0))
"""
formula = get_formula(StringIO(smtlib_content))
print(formula)