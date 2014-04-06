# REGISTRY CODE

# The following code will live in a registry.py module that deals with keeping
# track of registered IO classes, as well as defining the base IO classes.

import six
from collections import OrderedDict

_io_classes = {}

class MetaRegisterBaseIO(type):
    """
    A meta-class that auto-registers IO classes with the registry
    """

    def __init__(cls, name, bases, members):

        super(MetaRegisterBaseIO, cls).__init__(name, bases, members)

        # Each sub-class should define ``_format_name`` which is the
        # string-based name of the format, e.g. ``fits`` or ``votable``.
        format_abbreviation = members.get('_format_name')
        if format_abbreviation is None:
            return  # don't register base classes

        # Each sub-class should also define ``_supported_class`` which is the
        # data class that the IO class supports, e.g. ``Table`` or ``NDData``.
        supported_class = members.get('_supported_class')
        if supported_class is None:
            raise ValueError("_supported_class is not defined")

        # Finally, we register the IO class, references by the format and the
        # data class (since this is how we will access them later)
        _io_classes[(format_abbreviation, supported_class)] = cls



@six.add_metaclass(MetaRegisterBaseIO)
class BaseIO(object):
    """
    The base class for any IO class
    """
    _format_name = None
    _supported_class = None
    _read_kwargs = OrderedDict()


def read(cls, *args, **kwargs):
    """
    The read function called by any data read method. Takes care of finding
    the correct reader and passing the appropriate arguments.
    """

    # Here we can try and explicitly extract the path to the file, as well as
    # obtain a file object, but this is beyond the scope of the example, and
    # already exists in the current registry.
    path = fileobj = None

    # We now try and identify the format of the file
    fmt = _get_valid_format('read', cls, path, fileobj, args, kwargs)

    # Once we have the format, we can access the readaer
    reader = _io_classes[(fmt, cls)]

    # And finally we can read the actual table and return it
    table = reader(*args, **kwargs)

    return table


READ_TEMPLATE = """
        Parameters
        ----------
        format : str
            Explicilty specify the format. See the `Notes`_ below for the
            available formats and options.

        Notes
        -----
        In addition to the ``format`` argumnet, the remaining arguments
        depend on the format used. The following formats are availale, along
        with the relevant arguments in each case:

"""

def initialize_io_classes(func):
    # If needed, we initialize the I/O classes
    if not _io_classes:
        import votable
    return func


def fix_docstring(func):
    """
    Add information about formats to the read/write method docstrings
    """

    func.__doc__ += READ_TEMPLATE

    for fmt, cl in _io_classes:
        func.__doc__ += "        * ``format='{0}'``\n\n".format(fmt)

        cls = _io_classes[(fmt, cl)]
        for kwarg in cls._read_kwargs:
            func.__doc__ += "            {0} : {1}\n                 {2}\n".format(kwarg, *cls._read_kwargs[kwarg])

    return func
