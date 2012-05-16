import sys

from __init__ import nif_explorer_base

from pyffi.formats.nif import NifFormat

class test_ninodes(nif_explorer_base):
    search_path = "test/nif/base/"
    result_path = "test/nif/ninodes"
    instance = NifFormat.NiNode
    
    def main(self):
        nif_explorer_base.__init__(self)
        nif_explorer_base.nif_explore(self)


test_ninodes.main(test_ninodes)s