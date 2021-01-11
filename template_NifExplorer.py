import sys
import os

from NifExplorer import NifExplorer

def main():
    
    explorer = NifExplorer()

    explorer.SetBlockType("NiNode")

    #This is valid syntax. Nif Explorer will resolve the Block Type to a string.
    #explorer.SetBlockType(NifFormat.NiNode)

    #You do not have to implicitly call SetProperty if you do not require said functionality.
    explorer.SetProperty(None)

    explorer.SetSearchPath("pytest/nif")
    explorer.SetResultPath("pytest/template_Results")

    explorer.RunNifExplorer()

if __name__ == "__main__":
    main()