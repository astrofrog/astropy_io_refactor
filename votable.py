# FILE FORMAT-SPECIFIC CLASS

from registry import BaseIO
class VOTableIO(BaseIO):

    _format_name = 'votable'
    _supported_class = 'Table'
    _kwargs = {}
    _kwargs['table_id'] = ('str', "The ID of the table in the VO table file")

    @staticmethod
    def identify(origin, filepath, fileobj, *args, **kwargs):
        return True

    @staticmethod
    def read(input, table_id=None):
        "Read a VO table"
        return 'table'

    @staticmethod
    def write(input, output, table_id=None):
        pass
