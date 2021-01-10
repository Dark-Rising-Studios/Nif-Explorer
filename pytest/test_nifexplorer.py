import pytest
import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
path = path.replace("\\pytest", "")
sys.path.append(path)
path += "\\pyffi"
sys.path.append(path)

from NifExplorer import NifExplorer
from NifExplorer import NifFormat

@pytest.fixture(autouse=True)
def setup_nifExplorer():
    '''Returns a Nif Explorer Instance'''        
    explorer = NifExplorer()

    explorer.BlockType = NifFormat.NiNode
    explorer.ResultPath = "String"
    explorer.SearchPath = None
        
    return explorer   

@pytest.mark.usefixtures("setup_nifExplorer")
class TestNifExplorer:

    def BlockType_None(self, setup_nifExplorer):
        assert setup_nifExplorer.BlockType == None

    def SearchPath_None(self, setup_nifExplorer):
        assert setup_nifExplorer.SearchPath == None

    def ResultPath_None(self, setup_nifExlorer):
        assert setup_nifExlorer.ResultPath == None
        
    @pytest.mark.parametrize('funcs', [SearchPath_None, ResultPath_None, BlockType_None])
    def test_NifExplorer_Variables_Equal_None(self, setup_nifExplorer, funcs):
        funcs(self,setup_nifExplorer)

    def test_Class_Is_None(self, setup_nifExplorer):
        assert setup_nifExplorer == None

    def test_BlockType_Not_None(self, setup_nifExplorer):
        assert setup_nifExplorer.BlockType != None

    def test_BlockType_Is_None(self, setup_nifExplorer):
        assert setup_nifExplorer.BlockType == None

    def test_BlockType_Is_String(self, setup_nifExplorer):
        assert isinstance(setup_nifExplorer.BlockType, str)

    def test_BlockType_Not_String(self, setup_nifExplorer):
        assert not isinstance(setup_nifExplorer.BlockType, str)   
        
    def test_SearchPath_Not_None(self, setup_nifExplorer):
        assert setup_nifExplorer.SearchPath != None
    
    def test_SearchPath_Is_None(self, setup_nifExplorer):
        assert setup_nifExplorer.SearchPath == None
    
    def test_SearchPath_Is_String(self, setup_nifExplorer):
        assert isinstance(setup_nifExplorer.SearchPath, str)
  
    def test_SearchPath_Not_String(self, setup_nifExplorer):
        assert not isinstance(setup_nifExplorer.SearchPath, str)

    def test_SearchPath_Directory_Does_Exist(self, setup_nifExplorer):
        assert os.path.exists(setup_nifExplorer.SearchPath) == True

    def test_SearchPath_Directory_Does_Not_Exist(self, setup_nifExplorer):
        if setup_nifExplorer.SearchPath == None or os.path.exists(setup_nifExplorer.SearchPath) == False:
            assert True

    def test_ResultPath_Not_None(self, setup_nifExplorer):
        assert setup_nifExplorer.ResultPath != None
    
    def test_ResultPath_Is_None(self, setup_nifExplorer):
        assert setup_nifExplorer.ResultPath == None
    
    def test_ResultPath_Is_String(self, setup_nifExplorer):
        assert isinstance(setup_nifExplorer.ResultPath, str)
  
    def test_ResultPath_Not_String(self, setup_nifExplorer):
        assert not isinstance(setup_nifExplorer.ResultPath, str)
        
    def test_ResultPath_Directory_Does_Exist(self, setup_nifExplorer):
        assert os.path.exists(setup_nifExplorer.ResultPath) == True

    def test_ResultPath_Directory_Does_Not_Exist(self, setup_nifExplorer):
        if setup_nifExplorer.ResultPath == None or os.path.exists(setup_nifExplorer.ResultPath) == False:
            assert True


if __name__ == "__main__":
    pytest.main()