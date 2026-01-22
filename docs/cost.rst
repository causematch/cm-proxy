Cost
-----

One of the things we like about cm-proxy is it is so cheap to run.  It
might even be free, depending on your AWS consumption.  Here are 
estimated monthly costs, assuming request and response size of 2kB.

=================== =============================== ==========
Proxy               Monthly cost (1000 requests)    Free Tier
=================== =============================== ==========
Unidirectional      $0.0011                         1M requests
Bidirectional       $0.0275                         4k requests
=================== =============================== ==========

If you want to see the nitty-gritty details of the calculation,
we prepared `a spreadsheet`_ for you.


.. _a spreadsheet: https://docs.google.com/spreadsheets/d/1dXMDdsDZUxtvPN71j4FucChoTzNHDsD8QcYLL25L2x4/edit?usp=sharing
