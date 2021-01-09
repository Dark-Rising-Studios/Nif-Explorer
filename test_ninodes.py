import sys
import os

#import first, as __init__ sets the python module search path for pyffi
from __init__ import nif_explorer_base

from pyffi.formats.nif import NifFormat

class test_ninodes(nif_explorer_base):
    search_path = "tests/nif/base"
    result_path = "tests/test outputs/"
    instance = NifFormat.NiNode
    property = None
    bsa = None
        
    def main(self):
        nif_explorer_base.__init__(self)
        nif_explorer_base.nif_explore(self)
        
test_ninodes.main(test_ninodes)