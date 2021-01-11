import sys
import os

from NifExplorer import NifExplorer

print("Nif Explorer Console")
print("")
print("Search all .nif files in a directory structure recursively looking for a specific blocktype.")
print("")

def main():
    Explorer = NifExplorer()

    print("Please input a search path: ")
    print("")

    Explorer.SetSearchPath(input())
    print("")
    print("Search Path Set: %s" % Explorer.SearchPath)
    print("")

    print("Please input a result path:")
    print("")
    Explorer.SetResultPath(input())
    print("")

    print("Result Path Set: %s" % Explorer.ResultPath)
    print("")

    print("Please Input a Block Type to search for:")
    print("")
    Explorer.SetBlockType(input())
    print("")

    print("")
    print("Block Type Set: %s" % Explorer.BlockType)
    print("")

    Explorer.RunNifExplorer()

if __name__ == "__main__":
    main()

