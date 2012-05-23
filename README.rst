Nif Explorer is a tool that allows a user to quickly scan through a multiple .nif files, 
looking for a certain block type or property. Nif Explorer can walk through a directory
containing a lot of .nif files, search for the block or property of the block, then output
its results a an user defined result path.

Not only that, Nif Explorer as of version 0.1.0, Nif Explorer can search through BSA archives 
searching for .nif files with the block or block property.

Requirements
------------

* `pyffi 2.2.0 or newer <http://sourceforge.net/projects/pyffi/files/pyffi-py3k/>`_

Fork
----

* git clone git://github.com/Aaron1178/nif_explorer.git
* http://github.com/Aaron1178/nif_explorer

Parameters
----------

Nif Explorer has two sets of parameters to use in buildenv. 

* 1. nif_explorer.bat -file@mytestfile.py - this will run the user file based off the template file
* 2. nif_explorer.bat -block@NiNode -property@None searchPath@None -bsa@None -resultPath@None

Note* To execute #2 option, all parameters must be typed in that order for Nif Explorer to work.
Note* Even though -searchPath and -bsa are set to None, one of them is required. 
Note* -resultPath is not a required parameter. If it is not supplied, it will create a default results directory in the location buildenv is using Nif Explorer from.
For command #2, all parameters are required, except for -resultPath

So the parameters are as follows:

* -file - To load user defined searches from .py files
* -block - A NifFormat block. e.g NiNode
* -property - A property of -block. It must be a property or an error will occur
* -searchPath - Moves Nif Explorer to load from a directory
* -bsa - Moves Nif Explorer to load its .nifs from a .BSA archive
* -resultPath - An optinal parameter. This sets the result path for Nif Explorer

How it works?

Nif Explorer uses Pyffi and Python 3.2 to interact with .nif and .bsa files and check their data.

Why should we use it?

You don't have to, it's just another tool to make life easier.

Bugs
-------------
*    If %python_path% inside buildenv is not set, the tests will not work
*    The -bsa path MUST have a following / on the end. e.g C:/Users/Bobb/Desktop/bsa/ 
Bugs - Fixed
*    If the result_path is inside search_path and you run the test again, it will check all the nif files in result_path directory as well, so it's best to keep them as two separate directories.
