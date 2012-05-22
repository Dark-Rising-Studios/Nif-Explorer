import os
import os.path
import io
import sq
from pyffi.formats.bsa import BsaFormat
from pyffi.formats.nif import NifFormat

path = "C:/Users/Aaron1178/Desktop/test.bsa"
stream = open(path,'rb')

data = BsaFormat.Data()
data.inspect(stream)
data.read(stream)

n_files = []
b_files = []

for f in data.folders[0].files:
    n_files.append(f.name)

file = data.folders[0].files[0]
stream.seek(194)
nif = stream.read(2256)
byteii = io.BytesIO()
byteii.write(nif)
byteii.seek(0)

ndata = NifFormat.Data()
ndata.inspect(byteii)
ndata.read(byteii)
for block in ndata.roots:
    print(block)