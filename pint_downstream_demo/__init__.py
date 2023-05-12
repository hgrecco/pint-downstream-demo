"""This is a demo project.
"""

import pint

ureg = pint.UnitRegistry()

# Length of Cruiser
rotterdam = 81.8 * ureg.meter
titanic = 269.1 * ureg.meter
wonder_of_the_seas = 362.04 * ureg.meter

__all__ = ["rotterdam", "titanic", "wonder_of_the_seas"]
