About
-----

This is a demonstration of a proposed new I/O unified framework. The goal of
this framework is to:

* define readers/writers/identifiers as file format-specific and data-class
  specific IO classes (e.g. VOTableIO)
* define all the documentation related to each reader/writer locally to the
  actual code.
* defer importing the classes defining I/O until the last minute.

Downsides of the current approach:

* We have to refer to the supported class (e.g. ``Table`` or ``NDData``) by
  name instead of by the class itself - this is needed for two reasons:

    * To prevent circular imports, ``_supported_class`` has to be a string,
      not the data class.

    * the ``fix_docstring`` decorator can't take the class itself, it has to
      take the name of the class.

Notes:

* The code is very hacky - things like text wrap and so on can be dealt with
  much better, but this is just meant to be a 'toy model' of the
  infrastructure.


Example
-------

    In [1]: from table import Table

    In [2]: print(Table.read.__doc__)

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

            * ``format='txt'``

                filename : str
                     The name of the file to read from
                skiprows : int
                     How many rows to skip at the start of the file


    In [3]: t = Table.read('data.txt')

    In [4]: print(t)
    [ 1.  2.  3.]
        
In the above example, the docstring was generated automatically