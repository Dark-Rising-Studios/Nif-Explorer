import os
import os.path
import io
from pyffi.formats.bsa import BsaFormat
from pyffi.formats.nif import NifFormat

path = "C:/Users/Aaron1178/Desktop/test.bsa"
result = "C:/Users/Aaron1178/Desktop/bsa/"
stream = open(path,'rb')

data = BsaFormat.Data()
data.inspect(stream)
data.read(stream)

n_files = []
n_offsets = []
n_sizes = []

def getExtension(file):
    return file.split(".")[-1]

def renameFile(file, indexn):
    new = file.split(".")[0]
    nifExt = file.split(".")[-1]
    tmp = new + "_copy%s." % (indexn) + nifExt
    return tmp

def bsa_explore():
        
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
    index = 0
    for folders in data.folders:
        for files in folders.files:
            if getExtension(files.name) != "nif":
                break
            offset = files.offset;
            fSize = files.file_size.num_bytes
            n_files.append(files.name)
            n_offsets.append(offset)
            n_sizes.append(fSize)
            index += 1
    
    indexn = 0    
    index = 0
    for f in n_files:
        stream.seek(n_offsets[index])
        nif = stream.read(n_sizes[index])
        tmpByte = io.BytesIO()
        tmpByte.write(nif)
        tmpByte.seek(0)
        ndata = NifFormat.Data()
        ndata.inspect(tmpByte)
        ndata.read(tmpByte)
    
        for block in ndata.roots:
            if isinstance(block, NifFormat.NiNode):
                if os.path.isfile(result + f):
                    f = renameFile(f, indexn)
                    indexn+=1
                streams = open(result + f, "wb")
                ndata.write(streams)
                print("written to %s" % (result + f))
                streams.close()
        index += 1 

bsa_explore()