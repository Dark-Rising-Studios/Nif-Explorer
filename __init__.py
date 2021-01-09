import os.path
import os
import shutil
import time
import io
from pyffi.formats.nif import NifFormat
from pyffi.formats.bsa import BsaFormat

class nif_explorer_base:
    """Base class for the Nif Explorer tool"""
    
    search_path = None
    """The path to search for the nif files"""
    result_path = None
    """The path where to store the result nifs"""
    instance = None
    """The instance/block to search for in the nif files"""
    property = None
    """instace property to search for"""
    files = []
    """The resulted success files"""
    index = 0
    """The number of files parsed"""
    fIndex = 0
    """The number of files with 'instance' found"""
    n_roots = []
    """root nodes"""
    n_blocks = []
    """Blocks of n_roots"""
    instance_count = 1
    """The count of multiple block 1 == default"""
    instance_cname = ""
    """The name of the multi instance file"""
    bsa = None
    """bsa name or None for no bsa search"""
    bsa_files = []
    bsa_offsets = []
    bsa_sizes = []
    """bsa related lists"""

    """A little function to get the file extension"""
    def getExtension(file):
        return file.split(".")[-1]

    """Here we run an initial check to see if paths exists, if not create them or errors"""
    def __init__(self):

        self.result_path = self.result_path + "/%s" % (self.__name__)
        self.result_path = self.result_path.replace("//", "/")

        if not self.search_path ==  None:
            if not os.path.exists(self.search_path) :
                print("Cannot find search folder %s" % self.search_path);
                return
            
        if not self.result_path ==  None:
            if not os.path.exists(self.result_path) :
                print("Cannot find result path, creating now!");
                os.mkdir(self.result_path)

        if self.result_path == None:
            if not os.path.exists("nif_explorer-results"):
                print("No result path specified, creating default now!");
                os.mkdir("nif_explorer-results")
            self.result_path = "nif_explorer-results"
                    
        elif not self.result_path ==  None:    
            if os.path.exists(self.result_path):
                print("Found %s, cleaning directory!" % self.result_path)
                fileList = [ f for f in os.listdir(self.result_path)]
                for f in fileList:
                    os.remove(self.result_path + "/%s" % f)
                          
    """This is the base method for searching nif files"""  
    def nif_explore(self):
        oldtime = time.time() #Start the clock :)
        """NifFormate.walkData searches the directory for files"""
        for stream, data in NifFormat.walkData(self.search_path):
            self.index += 1
            instance_count = 0;
            try:
                data.read(stream)
                
                for root in data.roots:
                    self.n_roots.append(root)
                    for block in root.tree():
                        self.n_blocks.append(block)
                        if isinstance(block, self.instance):
                            if stream.name.replace("\\","/") in self.files:
                                self.instance_count += 1
                                self.instance_cname = stream.name.replace("\\","/")
                            if self.property != None:
                                if getattr(block, self.property):
                                    print("%s found in %s" % (self.property, stream.name.replace("\\","/")))
                                    self.files.append(stream.name.replace("\\","/"))
                                else:
                                    print("Warning: No property %s found in %s" % (self.property, stream.name.replace("\\","/")))
                            else:  
                                print("Found block type: %s in %s" % (self.instance.__name__, stream.name.replace("\\","/")))
                                self.files.append(stream.name.replace("\\","/"))
                self.fIndex += 1
            except Exception:
                print("Warning: read failed due to corrupt file",
                      ", corrupt format description or bug")

        for file in self.files:
            shutil.copy(file, self.result_path)

        if self.instance_count > 1:
            print("%s instance blocks in %s" % (self.instance_count, self.instance_cname))

        if len(self.files) < 1: 
            print("Found %s of block type: %s" % (len(self.files), self.instance.__name__))
        else:
            print("Found %s of block type: %s" % (len(self.files), self.instance.__name__))
            print("Output folder %s" % self.result_path)

        print("Counted %s objects in %ss" % (self.index, time.time()-oldtime))

    def getExtension(file):
        return file.split(".")[-1]
    
    def renameFile(file, indexn):
        new = file.split(".")[0]
        nifExt = file.split(".")[-1]
        tmp = new + "_copy%s." % (indexn) + nifExt
        return tmp

        
    def bsa_explore(self):
        oldtime = time.time()
        
        if self.bsa == None:
            print("Trying to read BSA when no bsa file is found!")
            return
        
        if not os.path.isfile(self.bsa):
            print("Couldn't find BSA file!")
            return
        else:
            stream = open(self.bsa, "rb")
            
        data = BsaFormat.Data()
        data.inspect(stream)
        data.read(stream)
        """if os.path.exists(result):
            print("Found %s, cleaning directory!" % result)
            fileList = [ f for f in os.listdir(result)]
            for f in fileList:
                os.remove(result + "/%s" % f)
        
        elif not os.path.exists(result):
            print("Result path %s now found, creating it now!" % result);
            os.mkdir(result)
        """
        """Here we run over the nif files in the bsa and get their name, offset and size"""
        self.index = 0
        for folders in data.folders:
            for files in folders.files:
                if self.getExtension(files.name) != "nif":
                    break
                offset = files.offset;
                fSize = files.file_size.num_bytes
                self.bsa_files.append(files.name)
                self.bsa_offsets.append(offset)
                self.bsa_sizes.append(fSize)
                self.index += 1
        
        indexn = 0    
        self.index = 0
        for f in self.bsa_files:
            stream.seek(self.bsa_offsets[self.index])
            nif = stream.read(self.bsa_sizes[self.index])
            tmpByte = io.BytesIO()
            tmpByte.write(nif)
            tmpByte.seek(0)
            ndata = NifFormat.Data()
            ndata.inspect(tmpByte)
            ndata.read(tmpByte)
        
            for block in ndata.roots:
                if isinstance(block, NifFormat.NiNode):
                    if os.path.isfile(self.result_path + f):
                        f = self.renameFile(f, indexn)
                        indexn+=1
                    if self.property != None:
                        if getattr(block, self.property):
                            print("Notice: %s found in %s" % (self.property, f.split("/")[-1]))
                        else:
                            print("Warning: No property %s found in %s" % (self.property, f.split("/")[-1]))
                            break
                    streams = open(self.result_path + "/" + f, "wb")
                    ndata.write(streams)
                    print("Notice: Written to %s" % (f))
                    streams.close()
            self.index += 1 
        print("Counted %s objects in %ss" % (self.index, time.time()-oldtime))
        print("Output folder %s" % self.result_path)
        