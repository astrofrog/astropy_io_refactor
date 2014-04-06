from registry import fix_docstring, read

class Table(object):
    
    @classmethod
    @fix_docstring
    def read(cls, *args, **kwargs):
        """
        Read and parse a data table and return as a Table.
        """
        read(cls, *args, **kwargs)