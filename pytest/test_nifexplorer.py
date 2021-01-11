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

@pytest.fixture(autouse=True, scope='session')
def setup_nifExplorer():
    '''Returns a Nif Explorer Instance'''        
    explorer = NifExplorer()

    explorer.SetBlockType(NifFormat.NiNode)
    explorer.SetResultPath("\\pytest\\results")
    explorer.SetSearchPath("\\pytest\\nif\\base")

    return explorer   

@pytest.mark.usefixtures("setup_nifExplorer")
class TestNifExplorer:

    def NifExlorer_BlockType_Is_Not_None(self, setup_nifExplorer):
        assert setup_nifExplorer.BlockType != None

    def NifExplorer_SearchPath_Is_Not_None(self, setup_nifExplorer):
        assert setup_nifExplorer.SearchPath != None

    def NifExplorer_ResultPath_Is_Not_None(self, setup_nifExlorer):
        assert setup_nifExlorer.ResultPath != None
        
    @pytest.mark.parametrize('funcs', [NifExplorer_SearchPath_Is_Not_None, NifExplorer_ResultPath_Is_Not_None, NifExlorer_BlockType_Is_Not_None])
    def test_NifExplorer_Variables_Equal_Not_None(self, setup_nifExplorer, funcs):
        funcs(self,setup_nifExplorer)
        
    def NifExplorer_ResultPath_Directory_Exists(self, setup_nifExplorer):
        print("NifExplorer_ResultPath_Directory_Exists[Directory]: %s" % setup_nifExplorer.ResultPath)
        assert os.path.exists(setup_nifExplorer.ResultPath) == True

    def NifExplorer_SearchPath_Directory_Exists(self, setup_nifExplorer):
        assert os.path.exists(setup_nifExplorer.SearchPath) == True

    def NifExplorer_SearchPath_Directory_Contains_No_Forward_Slashes(self, setup_nifExplorer):
        assert setup_nifExplorer.SearchPath.count('/') < 1

    def NifExplorer_ResultPath_Directory_Contains_No_Forward_Slashes(self, setup_nifExplorer):
        assert setup_nifExplorer.ResultPath.count('/') < 1

    @pytest.mark.parametrize('funcs', [NifExplorer_ResultPath_Directory_Exists, NifExplorer_SearchPath_Directory_Exists, NifExplorer_SearchPath_Directory_Contains_No_Forward_Slashes, NifExplorer_ResultPath_Directory_Contains_No_Forward_Slashes])
    def test_NifExplorer_Directories_Exist_And_Paths_Contain_No_Forward_Slashes(self, setup_nifExplorer, funcs):
        funcs(self, setup_nifExplorer)

if __name__ == "__main__":
    pytest.main()