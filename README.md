About
-----

This is a demonstration of a proposed new I/O unified framework. The goal of
this framework is to:

* define readers/writers/identifiers as file format-specific and data-class
  specific IO classes (e.g. VOTableIO)
* define all the documentation related to each reader/writer locally to the
  actual code.
* defer importing the classes defining I/O until the last minute.

Issues currently:

* fix_docstring doesn't yet know how to pick only IO classses that explicitly support e.g. read, and also for the specific class requested. We could pass arguments to the decorator, though the class itself cannot be passed (but class name can).

Example
-------

    In [1]: from table import Table

    In [2]: Table.read?
    Type:        instancemethod
    String form: <bound method type.read of <class 'table.Table'>>
    File:        /Users/tom/Desktop/io_refactor/table.py
    Definition:  Table.read(cls, *args, **kwargs)
    Docstring:
    Read and parse a data table and return as a Table.

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

    * ``format='votable'``

        filename : str
             The name of the file to read from
        table_id : str
             The ID of the table in the VO table file
        
In the above example, the docstring was generated automatically