import os
import sys
import time
import shutil

from pyffi.formats.nif import NifFormat

class NifExplorer():
    """Utility class to scan .nif files searching for user-defined Block Types"""

    """The Blocktype that this instance is searching for"""
    BlockType = None

    """The Property that this instance is searching for"""
    Property = None

    """The search path where the .nif files are located. Will scan through all sub-directories recursively"""
    SearchPath = None

    """The result path where the .nif files will be copied too. Result will be <ResultPath>/<BlockType>/"""
    ResultPath = None
   
    """Set the BlockType, will resolve down to a string, but a valid class can be passed. e.g: NifFormat.NiNode"""
    def SetBlockType(self, InBlockType):        
        if InBlockType == None:
            assert "NifExplorer.SetBlockType(): InBlockType is None!"
            sys.exit()

        if isinstance(InBlockType, str):
            if self.FindBlockTypeByName(InBlockType) == None:
                assert "NifExplorer.SetBlockType(): Cannot find BlockType!"
                sys.exit()

            else:
                self.BlockType = self.FindBlockTypeByName(InBlockType)

        else:
            BlockTypeToString = str(InBlockType)

            BlockTypeToString = BlockTypeToString.split("'")[1]

            self.BlockType = self.FindBlockTypeByName(BlockTypeToString)

            if self.BlockType == None:
                assert("NifExplorer.SetBlockType(): Cannot Resolve BlockType!")
                sys.exit()
    
    """Set the Property"""
    def SetProperty(self, InProperty):        
        if InProperty == None:
            assert "NifExplorer.SetProperty(): InProperty is None!"
            sys.exit()

        if isinstance(InProperty, str):
            if len(InProperty) < 1:
                assert "NifExplorer.SetProperty(): Cannot set Property!"
                sys.exit()

            else:
                self.Property = InProperty.lower()

        else: 
            assert "NifExplorer.SetProperty(): InProperty must be a string!"
            sys.exit()

    """Set the Search Path"""
    def SetSearchPath(self, InSearchPath):
        if not isinstance(InSearchPath, str):
            assert "NifExplorer.SetSearchPath(): InSearchPath must be a string!"
            sys.exit()

        elif self.MakeAbsolutePath(__file__, InSearchPath) != None:
            self.SearchPath = self.MakeAbsolutePath(__file__, InSearchPath)

            if not os.path.exists(self.SearchPath):
                print("Fake: %s" % self.SearchPath)
                assert "NifExplorer.SetSearchPath(): Search Path does not exist!"
                sys.exit()

            if not self.DirectoryContainsNifRecursively(self.SearchPath):
                assert "No .nif files found recursively!"
                sys.exit()
        else:
            assert "NifExplorer.SetSearchPath(): Cannot Resolve Search Path!"
            sys.exit()

    """Set the Result Path, if the specified path doesn't exist, it will create it"""
    def SetResultPath(self, InResultPath):
        if not isinstance(InResultPath, str):
            assert "NifExplorer.SetSearchPath(): InResultPath must be a string!"
            sys.exit()

        elif self.MakeAbsolutePath(__file__, InResultPath) != None:
            ResultPath = self.MakeAbsolutePath(__file__, InResultPath)

            ResultPath += (os.sep + self.BlockTypeToString(self.BlockType))

            if not os.path.exists(ResultPath):
                print("Could not find Result Path: '%s', Creating Now!" % ResultPath)
                os.makedirs(ResultPath)
    
            self.ResultPath = ResultPath

        else:
            assert "NifExplorer.SetResultPath(): Cannot Resolve Result Path!"
            sys.exit()
   
    """Get all nif files containing BlockType and return a list"""
    def SearchForBlockType(self):
        if (self.BlockType, self.ResultPath, self.SearchPath) == None:
            assert "NifExplorer.SearchForBlockType() No Nif Explorer variables have been set yet. Please configure Nif Explorer first!"
            sys.exit()

        ListofNifs = []

        for stream, data in NifFormat.walkData(self.SearchPath):            
            try:
                print("Reading %s" % stream.name.replace("\\","/"))
                data.read(stream)
                    
                for root in data.roots:
                    for block in root.tree():
                        if isinstance(block, self.BlockType):
                            ListofNifs.append(stream.name.replace("\\", "/"))                

            except Exception:
                print("Warning: Read failed due to corrupt file, corrupt format description, or a bug!")

        return ListofNifs

    """Get all nif files containing Property and return a list"""
    def SearchForProperty(self):
        if (self.BlockType and self.ResultPath and self.SearchPath) == None:
            assert "NifExplorer.SearchForBlockType() No Nif Explorer variables have been set yet. Please configure Nif Explorer first!"
            sys.exit()

        elif self.Property == None:
            return []

        ListofNifs = []

        for stream, data in NifFormat.walkData(self.SearchPath):            
            try:
                print("Reading Property from %s" % stream.name.replace("\\","/"))
                data.read(stream)
                    
                for root in data.roots:
                    for block in root.tree():
                        if isinstance(block, self.BlockType):
                            if getattr(block, self.Property):
                                ListofNifs.append(stream.name.replace("\\", "/")) 
                            else:
                                assert "NifExplorer.SearchForProperty(): Property not found!"     
            except Exception as e:
                print("Warning: Read failed due to corrupt file, corrupt format description, or a bug! %s " %e)
                return None

        return ListofNifs

    """Copy all search results to ResulT Path"""
    def CopyFilesToResultPath(self, BlockTypeFiles = None, PropertyFiles = None):
        if BlockTypeFiles != None:
            if len(BlockTypeFiles) > 0:
                for file in BlockTypeFiles:
                    try:
                        shutil.copy(file, self.ResultPath)

                    except IOError as error:
                        print("Cannot copy file: %s to Result Path: %s" % (file, error))

                return True
            return True

        elif PropertyFiles != None and len(PropertyFiles) > 0:
            for file in BlockTypeFiles:
                try:
                    shutil.copy(file, self.ResultPath)

                except IOError as error:
                    print("Cannot copy file: %s to Result Path: %s" % (file, error))

            return True

        else:
            assert "NifExplorer.CopyFilesToResultPath(): Nothing to do!"
            return False
        
    """Start and return a timer"""
    def StartTimer(self):
        return time.time()

    """Stops the timer and Returns the End Time"""
    def EndTimer(self, start):
        return time.time() - start

    """Find a BlockType by Name via a string instance"""
    def FindBlockTypeByName(self, BlockTypeName):
        BlockTypeName = str(BlockTypeName)

        if not isinstance(BlockTypeName, str):
            assert "NifExplorer.FindBlockTypeByName(): Parameter 'BlockTypeName' Must be a string!"

        for object in getattr(sys.modules["pyffi.formats.nif"], "NifFormat").__dict__.values():
            if hasattr(object, "__name__"):
                if object.__name__ == BlockTypeName and object != None:
                    return object

        return None

    """Searches for a directory recursively for .nif files"""
    @staticmethod
    def DirectoryContainsNifRecursively(path):
        for SubDirectrory, Directories, Files in os.walk(path):
            for FileName in Files:
                FilePath = SubDirectrory + os.sep + FileName

                if FilePath.endswith(".nif"):
                    return True

        return False        

    """Returns a string derived from a NifFormat BlockType"""
    @staticmethod
    def BlockTypeToString(BlockType):
        if BlockType == None:
            assert "NifExplorer.BlockTypeToString(): BlockType shouldn't be None"
            return

        s = str(BlockType)
        strings = s.split("'")

        if len(strings) > 0:
            return strings[1]

        else:
            assert "NifExplorer.BlockTypeToString(): Could not resolve BlockType!"

    """"Returns an absolute file path, where a could be __file__"""
    @staticmethod
    def MakeAbsolutePath(a,b):
        str = os.path.dirname(os.path.realpath(a))

        b = b.replace("\n", "\\n")

        if "\\" or "/" or r"\"" in b:
            b = b.replace("\\", os.sep)

            if os.sep == "\\":
                b = b.replace("\n", "\\n")

            if b[0] == "/":
                split = b.split("/", 1)
                b = split[1]
            elif b[0] == "\\":
                split = b.split("\\", 1)
                b = split[1]

        str = os.path.join(str, b)
        str = str.replace("/", os.sep)
        str = str.replace("\\", os.sep)

        if not os.path.isabs(str):
            assert "NifExplorer.MakeAbsolutePath(): Cou;d not make absolute path!"

        return str

    """Returns the count of .nif files found"""
    @staticmethod
    def GetNifFileCount(self, BlockTypeFiles = None, PropertyFiles = None):
        if BlockTypeFiles == None and PropertyFiles == None:
            return 0
        else:
            if BlockTypeFiles == None:
                return 0 + len(PropertyFiles)
            elif PropertyFiles == None:
                return 0 + len(BlockTypeFiles)
            else:
                return len(BlockTypeFiles) + len(PropertyFiles) 
