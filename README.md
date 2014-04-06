This is a demonstration of a proposed new I/O unified framework. The goal of
this framework is to:

* define readers/writers/identifiers as file format-specific and data-class
  specific IO classes (e.g. VOTableIO)
* define all the documentation related to each reader/writer locally to the
  actual code.
* defer importing the classes defining I/O until the last minute.
