import os.path
import os
import shutil
import time

from pyffi.formats.nif import NifFormat
from xmlrpc.client import DateTime

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

    """Here we run an initial check to see if paths exists, if not create them or errors"""
    def __init__(self):
        if not os.path.exists(self.search_path):
            print("Cannot find search folder %s" % self.search_path);

        if not os.path.exists(self.result_path):
            print("Cannot find folder %s, creating it now!" % self.result_path);
            os.mkdir(self.result_path)
            
        elif os.path.exists(self.search_path):
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
                                self.files.append(stream.name.replace("\\","/"))
                self.fIndex += 1
            except Exception:
                print("Warning: read failed due to corrupt file",
                      ", corrupt format description or bug")

        for file in self.files:
            shutil.copy(file, self.result_path)
        if self.instance_count > 1:
            print("%s instance blocks in %s" % (self.instance_count, self.instance_cname))
        print("Counted %s objects in %ss" % (self.index, time.time()-oldtime))
        print("Output folder %s" % self.result_path)