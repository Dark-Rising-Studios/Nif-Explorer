import sys

from __init__ import nif_explorer_base

from pyffi.formats.nif import NifFormat

class test_ninodes(nif_explorer_base):
    search_path = sys.argv[3] if (len(sys.argv) >= 4) else ""
    result_path = sys.argv[4] if (len(sys.argv) >= 5) else None
    instance =  getattr(NifFormat, sys.argv[1]) if (len(sys.argv) >= 2) else None
    property = sys.argv[2] if (len(sys.argv) >= 3) else None
        
    def main(self):
        nif_explorer_base.__init__(self)
        nif_explorer_base.nif_explore(self)
        

test_ninodes.main(test_ninodes)