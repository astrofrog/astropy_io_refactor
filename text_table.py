# FILE FORMAT-SPECIFIC CLASS

import numpy as np
from registry import BaseIO

class FilenameIO(BaseIO):
    """
    A base class for all IO classes that have ``filename`` as their first
    argument.

    This is just to demonstrate the dynamic docstring generation, and not
    intended for use in astropy.
    """

    _read_kwargs = BaseIO._read_kwargs.copy()
    _read_kwargs['filename'] = ('str', "The name of the file to read from")


class TextTableIO(FilenameIO):

    _format_name = 'txt'
    _supported_class = 'Table'  # use str to prevent circular imports

    @staticmethod
    def identify(origin, *args, **kwargs):
        return args[0].endswith('.txt')

    _read_kwargs = FilenameIO._read_kwargs.copy()
    _read_kwargs['skiprows'] = ('int', "How many rows to skip at the start of the file")

    @staticmethod
    def read(filename, skiprows=0):
        "Read a text table"
        from table import Table  # prevent circular imports
        return Table(np.loadtxt(filename, skiprows=skiprows))
