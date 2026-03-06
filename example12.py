from io import StringIO

from pysmt.smtlib.parser import get_formula
from pysmt.shortcuts import is_sat
from pysmt.logics import LIA

smtlib_content = r"""
(assert (exists ((x Nat) (y Nat)) (< (+ x y) x)))
"""

formula = get_formula(StringIO(smtlib_content))
print("Formula: " + str(formula))
sat = is_sat(formula, solver_name="cvc5", logic=LIA)
print("Sat: " + str(sat))