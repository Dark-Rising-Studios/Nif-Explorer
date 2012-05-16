The Nif Explorer is a tool used to explore multiple NIF files in a single directory for an indicated block.

Requirements
------------

* `pyffi 2.2.0 or newer <http://sourceforge.net/projects/pyffi/files/pyffi-py3k/>`_

Fork
----

* git clone git://github.com/Aaron1178/nif_explorer.git
* http://github.com/Aaron1178/nif_explorer

How it works?

Nif Explorer uses Pyffi and python to interact with nif files and check their data.

*    Opens all nif files in a selected folder
*    Checks if the nif file has the indicated instance(NifFormat.NiNode for example)
*    If so, it copies that nif file to the result_path folder.

Why should we use it?

You don't have to, it's just another tool to make life easier

Bugs
-------------

There are two main bugs that I have found while testing.

*    If the result_path is inside search_path and you run the test again, it will check all the nif files in result_path directory as well, so it's best to keep them as two separate directories.
*    If %python_path% inside buildenv is not set, the tests will not work