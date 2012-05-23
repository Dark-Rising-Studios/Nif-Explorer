import sys

from __init__ import nif_explorer_base

from pyffi.formats.nif import NifFormat

class test_ninodes(nif_explorer_base):
    search_path = None
    result_path = sys.argv[5] if (len(sys.argv) >= 6) else None
    instance =  getattr(NifFormat, sys.argv[1]) if (len(sys.argv) >= 2) else None
    property = None
    bsa = None
    if len(sys.argv) >= 4:
        if sys.argv[3] == "None":
            search_path = None
        else:
            search_path = sys.argv[3]
    if len(sys.argv) >= 3:
        if sys.argv[2] == "None":
            property = None
        else:
            property = sys.argv[2]
    if len(sys.argv) >= 5:
        if sys.argv[4] == "None":
            bsa = None
        else:
            bsa = sys.argv[4]
    def main(self):
        nif_explorer_base.__init__(self)
        if self.search_path == None:
            nif_explorer_base.bsa_explore(self)
            return
        nif_explorer_base.nif_explore(self)
        

test_ninodes.main(test_ninodes)