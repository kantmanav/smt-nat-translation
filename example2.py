from pysmt.smtlib.parser import get_formula
from pysmt.shortcuts import is_sat
from pysmt.walkers.nat_var_lift_dag import NatVarLiftDagWalker
from io import StringIO

smtlib_content = r"""
(assert (exists ((x Nat)) (< x 0)))
"""

formula = get_formula(StringIO(smtlib_content))
print("Formula: " + str(formula))
sat = is_sat(formula, solver_name="cvc5")
print("Sat: " + str(sat))