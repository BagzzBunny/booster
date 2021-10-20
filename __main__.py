from drift import Drift
from cpymad.madx import Madx


madx = Madx()
#madx.options(echo = True)
madx.input('CALL, FILE="booster.madx";')