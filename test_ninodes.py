import sys

from __init__ import nif_explorer_base

from pyffi.formats.nif import NifFormat

class test_ninodes(nif_explorer_base):
    search_path = "test/nif/base"
    result_path = "test/nif/base/bob"
    instance = NifFormat.NiNode
    property = "collision_object"
    bsa = None
        
    def main(self):
        nif_explorer_base.__init__(self)
        nif_explorer_base.nif_explore(self)
        

test_ninodes.main(test_ninodes)