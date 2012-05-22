import sys

from __init__ import nif_explorer_base

from pyffi.formats.nif import NifFormat

class test_ninodes(nif_explorer_base):
    search_path = sys.argv[3] if (len(sys.argv) >= 4) else ""
    result_path = sys.argv[4] if (len(sys.argv) >= 5) else None
    instance =  getattr(NifFormat, sys.argv[1]) if (len(sys.argv) >= 2) else None
    property = None
    if len(sys.argv) >= 3:
        if sys.argv[2] == "None":
            property = None
        else:
            property = sys.argv[2]
     
        
    def main(self):
        nif_explorer_base.__init__(self)
        nif_explorer_base.nif_explore(self)
        

test_ninodes.main(test_ninodes)