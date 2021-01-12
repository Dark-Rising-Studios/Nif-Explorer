import pytest
import os
import sys

sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__).replace("pytest","")), "pyffi"))
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__).replace("pytest","")))

from NifExplorer import NifExplorer
from pyffi.formats.nif import NifFormat

@pytest.fixture(autouse=True, scope='session')
def setup_nifExplorer():
    Explorers = []

    explorer = NifExplorer()
    explorer.SetBlockType(NifFormat.NiNode)
    explorer.SetResultPath("pytest/results")
    explorer.SetSearchPath("pytest\nif\\base")
    explorer.SetProperty("name")

    explorer2 = NifExplorer()
    explorer2.SetBlockType(NifFormat.bhkCollisionObject)
    explorer2.SetResultPath("\\pytest\\results")
    explorer2.SetSearchPath("\\pytest\\nif\\base")
    explorer2.SetProperty("flags")

    explorer3 = NifExplorer()
    explorer3.SetBlockType("NiNode")
    explorer3.SetResultPath("\\pytest\\results")
    explorer3.SetSearchPath("\\pytest\\nif\\base")
    explorer3.SetProperty("Rotation")

    Explorers.append(explorer)
    Explorers.append(explorer2)
    Explorers.append(explorer3)

    return Explorers   

@pytest.mark.usefixtures("setup_nifExplorer")
class TestNifExplorer:
    def NifExlorer_BlockType_Is_Not_None(self, setup_nifExplorer):
        assert setup_nifExplorer.BlockType != None

    def NifExplorer_SearchPath_Is_Not_None(self, setup_nifExplorer):
        assert setup_nifExplorer.SearchPath != None

    def NifExplorer_ResultPath_Is_Not_None(self, setup_nifExlorer):
        assert setup_nifExlorer.ResultPath != None
        
    @pytest.mark.parametrize('funcs', (NifExplorer_SearchPath_Is_Not_None, NifExplorer_ResultPath_Is_Not_None, NifExlorer_BlockType_Is_Not_None))
    def test_NifExplorer_Variables_Equal_Not_None(self, setup_nifExplorer, funcs):
        for obj in setup_nifExplorer:
            funcs(self,obj)
        
    def NifExplorer_ResultPath_Directory_Exists(self, setup_nifExplorer):
        assert os.path.exists(setup_nifExplorer.ResultPath) == True

    def NifExplorer_SearchPath_Directory_Exists(self, setup_nifExplorer):
        assert os.path.exists(setup_nifExplorer.SearchPath) == True

    @pytest.mark.parametrize('funcs', [NifExplorer_ResultPath_Directory_Exists, NifExplorer_SearchPath_Directory_Exists])
    def test_NifExplorer_Directories_Exist_And_Paths_Contain_No_Forward_Slashes(self, setup_nifExplorer, funcs):
        for obj in setup_nifExplorer:
            funcs(self,obj)

    def NifExplorer_SearchPath_Contains_Nif_Files_Recursively(self, setup_nifExplorer):
        assert setup_nifExplorer.DirectoryContainsNifRecursively(setup_nifExplorer.SearchPath) == True

    @pytest.mark.parametrize('funcs', [NifExplorer_SearchPath_Contains_Nif_Files_Recursively])
    def test_NifExplorer_SearchPath_Contains_Nif_Files(self, setup_nifExplorer, funcs):
        for obj in setup_nifExplorer:
            funcs(self,obj)

    def NifExplorer_Search_Nifs_For_BlockType(self, setup_nifExplorer):        
        assert setup_nifExplorer.SearchForBlockType() != None
        assert len(setup_nifExplorer.SearchForBlockType()) > 0

    def NifExplorer_Search_Nifs_For_Property(self, setup_nifExplorer):
        assert setup_nifExplorer.SearchForProperty() != None 
        assert len(setup_nifExplorer.SearchForProperty()) > 0

    def NifExplorer_Copy_All_Files_To_Results(self, setup_nifExplorer):
        BlockTypeFiles = setup_nifExplorer.SearchForBlockType()
        PropertyFiles  = setup_nifExplorer.SearchForProperty()

        assert setup_nifExplorer.CopyFilesToResultPath(BlockTypeFiles,PropertyFiles)

    @pytest.mark.parametrize('funcs', [NifExplorer_Search_Nifs_For_BlockType, NifExplorer_Copy_All_Files_To_Results,NifExplorer_Search_Nifs_For_Property])
    def test_NifExplorer(self, setup_nifExplorer, funcs):
        for obj in setup_nifExplorer:
            funcs(self, obj)

if __name__ == "__main__":
    pytest.main()