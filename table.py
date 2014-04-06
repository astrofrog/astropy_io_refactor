from registry import fix_docstring, read, initialize_io_classes

class Table(object):
    
    @classmethod
    @fix_docstring
    @initialize_io_classes
    def read(cls, *args, **kwargs):
        """
        Read and parse a data table and return as a Table.
        """
        read(cls, *args, **kwargs)