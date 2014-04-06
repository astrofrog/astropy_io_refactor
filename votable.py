# FILE FORMAT-SPECIFIC CLASS

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


class VOTableIO(FilenameIO):

    _format_name = 'votable'
    _supported_class = 'Table'

    @staticmethod
    def identify(origin, filepath, fileobj, *args, **kwargs):
        return True

    _read_kwargs = FilenameIO._read_kwargs.copy()
    _read_kwargs['table_id'] = ('str', "The ID of the table in the VO table file")

    @staticmethod
    def read(input, table_id=None):
        "Read a VO table"
        return 'table'

