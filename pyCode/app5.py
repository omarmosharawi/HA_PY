# units convertor

units = {'mg': 0.001, 'cg': 0.01, 'dg': 0.1, 'g': 1, 'kg': 1000}

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a value from one unit of measurement to another."""
    if (from_unit not in units or to_unit not in units):
        raise ValueError("Invalid unit")
    return value * (units[to_unit] / units[from_unit])

# Test the function with some example values
print('1)', convert(5, 'kg', 'g'))
print('2)', convert(37.2, 'cg', 'kg'))
print('3)', convert(10, 'mg', 'g'))
