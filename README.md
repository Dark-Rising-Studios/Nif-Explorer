![Run Nif Explorer](https://github.com/Dark-Rising-Studios/Nif-Explorer/workflows/Run%20Nif%20Explorer/badge.svg) ![Nif Explorer PyTests](https://github.com/Dark-Rising-Studios/Nif-Explorer/workflows/Nif%20Explorer%20PyTests/badge.svg)

Nif Explorer is a tool that scans recursively through a specified directory, looking for .nif
files containing certain Block Types or Properties of certain Block Types. The result will copy
all .nif files which meet the specified parameters to the specified results path. 

Nif Explorer has been re-designed to be as optimal and as bug free as possible for it's official stable release.

There a two ways in which Nif Explorer can be run. 

Requirements
------------
1.  Python 3.9.1
2.  Pyffi

Running Nif Explorer via nifexplorerConsole.py
----------------------------------------------
This option provides a user with the hassle free option of not having to edit code. nifexplorerConsole.py provides an
easy to read, interactive console, where a user can specify a Search Path, a Result Path, a Block Type to search for, 
and even a Property of said Block Type.

To run Nif Explorer:

1.  Open up a terminal inside the Nif Explorer installation directory.
2.  run: python nifexplorerConsole.py
3.  Input the necessary parameters as promted.
4.  Once Nif Explorer has been run, you can find the results in the <resultspath>/<BlockType>/

Running Nif Explorer from a user defined .py file
-------------------------------------------------
To run Nif Explorer via a user derinded .py file, some programming knowledge is required.
A template file has been included.

You can run Nif Explorer similar to the method above:

1.  Open up a terminal inside the Nif Explorer installation directory.
2.  run: python <userdefinedfile>.py
3.  Once Nif Explorer has been run, you can find the results in the <resultspath>/<BlockType>/

Parameters
----------
* **BlockType**: The specified Block Type to search for. In a userdefined .py file, this can be either a string, or a NifFormat.BlockType class. Nif Explorer resolves all Block Types to strings. Cannot be None
* **Property**: The speccidied Property to search for in Block Type. Can be None. 
* **SearchPath**: The Search Path in which a directory or any sub-directories contain .nif files. Will throw an error if no .nif files were found. Cannot be None
* **ResultPath**: The Results Path in which the results will be copied to. If the directory does not exist, it will be created for you. Cannot be None
