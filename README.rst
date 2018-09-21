##############################################
CHD - Courses downloader for coursehunters.net
##############################################

Requirements
============

* `Python 3.6 <https://www.python.org/downloads/release/python-366/>`_ or higher. 


Installation
============


.. code-block:: bash

    pip install chd

Usage
-----

.. code-block:: bash

    chd url [-p path] [-s start_lesson] [-e end_lesson] [-v]

.. code-block:: bash

    positional arguments:
    url                       course url

    optional arguments:
    -h, --help                show this help message and exit
    -p PATH, --path PATH      download path, default is <course-name>
    -s START, --start START   the lesson number from which to start the download
                            
    -e END, --end END         the lesson number at which the download will be
                              completed
    -v, --version             print version information and exit