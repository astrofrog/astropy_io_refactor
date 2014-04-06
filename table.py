from registry import fix_docstring, read, initialize_io_classes

class Table(object):
    
    def __init__(self, data):
        self.data = data
        
    def __str__(self):
        return self.data.__str__()
    
    @classmethod
    @fix_docstring
    @initialize_io_classes
    def read(cls, *args, **kwargs):
        """
        Read and parse a data table and return as a Table.
        """
        return read(cls, *args, **kwargs)