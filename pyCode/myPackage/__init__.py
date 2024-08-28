from myPackage import module1, module2

print(f'The name of this package is {__name__}')



#
__all__ = [
    'module1',  # export the module 1 class to be accessed directly by its name when importing the all package and when we use import * in the packages file
]
