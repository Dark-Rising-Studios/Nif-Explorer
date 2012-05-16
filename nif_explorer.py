import os
import site # get site-packages into sys.path
import sys

# add local addons folder to sys.path so blender finds it
sys.path = (
    [os.path.join(os.path.dirname(__file__), 'test')]
    + sys.path
    )

# run nosetests
# this assumes that the builder is called as
# "blender --background --factory-startup --python blender-nosetests.py -- ..."
# pass the correct arguments by dropping the arguments prior to --
