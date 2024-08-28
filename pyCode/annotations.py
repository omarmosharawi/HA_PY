# Annotations method used to define data type

def duplicate(value: float) -> float:
    """"this is a docstring for the function 'duplicate'.""" # This annotation is not used in the code. It will be ignored by Python.
    return value*2.0

print(duplicate(5.5))
