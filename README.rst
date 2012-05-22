The Nif Explorer is a tool used to explore multiple NIF files in a single directory for an indicated block.

Requirements
------------

* `pyffi 2.2.0 or newer <http://sourceforge.net/projects/pyffi/files/pyffi-py3k/>`_

Fork
----

* git clone git://github.com/Aaron1178/nif_explorer.git
* http://github.com/Aaron1178/nif_explorer

Parameters
----------

There are two ways to use Nif Explorer.

* 1. You use Nif Explorer to run a python file, that the user has created based off the template
* 2. The user uses Nif Explorer to run via console commands. This includes setting the block, property, searchPath and resultPath

The commands are as follows:

* 1. nif_explorer.bat -file@mytestfile.py - this will run the user file based off the template file
* 2. nif_explorer.bat -block@NiNode -property@None searchPath@test/my/folder/full/of/nifs -resultPath@test/my/test/results

For command #2, all parameters are required, except for -resultPath

So the parameters are as follows:

* -file
* -block
* -property
* -searchPath
* -resultPath

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