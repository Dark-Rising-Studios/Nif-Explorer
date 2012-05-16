import os.path
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
    files = []
    """The resulted success files"""
    index = 0
    """The number of files parsed"""
    fIndex = 0
    """The number of files with 'instance' found"""

    def __init__(self):
        if not os.path.exists(self.search_path):
            print("Cannot find folder %s" % self.search_path);
            return
        
        if not os.path.exists(self.result_path):
            os.mkdir(self.result_path)
                
    def nif_explore(self):
        oldtime = time.time()
        for stream, data in NifFormat.walkData(self.search_path):
            self.index += 1
            try:
                print("Reading %s" % stream.name)
                data.read(stream)
                for root in data.roots:
                    for block in root.tree():
                        if isinstance(block, self.instance):
                            self.files.append(stream.name.replace("\\","/"))
                self.fIndex += 1
            except Exception:
                print("Warning: read failed due to corrupt file",
                      ", corrupt format description or bug")

        for file in self.files:
            shutil.copy(file, self.result_path)
            
        print("Counted %s objects in %ss" % (self.index, time.time()-oldtime))
        print("Output folder %s" % self.result_path)