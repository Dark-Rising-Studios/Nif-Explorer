from pyffi.formats.nif import NifFormat

class NifExplorer():
    """Utility class to scan .nif files searching for user-defined Block Types"""

    """The Blocktype that this instance is searching for"""
    BlockType = None

    """The search path where the .nif files are located. Will scan through all sub-directories recursively"""
    SearchPath = None

    """The result path where the .nif files will be copied too. Result will be <ResultPath>/<BlockType>/"""
    ResultPath = None





