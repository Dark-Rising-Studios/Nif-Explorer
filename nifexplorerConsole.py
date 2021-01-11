from NifExplorer import NifExplorer
from NifExplorer import NifFormat

print("Nif Explorer Console")
print("")
print("Search all .nif files in a directory structure recursively looking for a specific blocktype.")
print("")

class nifexplorer(nif_explorer_base):
    search_path = None
    result_path = None
    instance = None
    property = None
    bsa = None
        
    def main(self):
        print("Please input a search path: ")
        print("")

        self.search_path = input()
        print("")
        print("Search Path Set: %s" % self.search_path)
        print("")

        print("Please input a result path:")
        print("")
        self.result_path = input()
        print("")

        print("Result Path Set: %s" % self.result_path)
        print("")

        print("Please Input a Block Type to search for:")
        print("")
        self.instance = input()
        print("")

        print("")
        print("Block Type Set: %s" % self.instance)
        print("")

        nif_explorer_base.__init__(self)
        nif_explorer_base.nif_explore(self)
        
nifexplorer.main(nifexplorer)

