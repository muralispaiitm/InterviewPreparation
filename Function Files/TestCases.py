from Activities_ForestPath import Activities_ForestPath_
from GlobalVariables import Variables
import unittest
# import pandas as pd

# ........................................................ NOTE ........................................................
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Setup before nunning Test cases
# 1. Paste the below class code in the "Action.py" file.
import pandas as pd
class Actions:
    def __init__(self):
        # Constant class variables
        self.FilePath = "D:/DataScience/02 INEURON/ML_Projects/Internal Projects (Practicing)/Work/Masters Projects/Chandana Projects/Assingment 02/Camelot v1.2 Windows - (Testing)-2022-04-08/TestCases/"
        self.startStr = "start "
        self.ActionsData = pd.DataFrame(columns=["CommandResult"])
        self.ActionsData.to_csv(self.FilePath+"Result_SC_AFP_Start.csv", index=False)


    def Execute_Command(self, command, wait=False):
        result = self.startStr + command

        Output_SC_AFP_Start = pd.read_csv(self.FilePath + "Output_SC_AFP_Start.csv")
        row = len(Output_SC_AFP_Start)
        self.ActionsData.loc[row] = [result]
        Output_SC_AFP_Start.to_csv(self.FilePath+"Result_SC_AFP_Start.csv", index=False)
        return True

class Test_Activities_ForestPath(unittest.TestCase):

    def test_SC_AFP_Start(self):
        FilePath = "D:/DataScience/02 INEURON/ML_Projects/Internal Projects (Practicing)/Work/Masters Projects/Chandana Projects/Assingment 02/Camelot v1.2 Windows - (Testing)-2022-04-08/TestCases/"
        ResultFileName = "Output_SC_AFP_Start.csv"
        TestFileName = "test_SC_AFP_Start.csv"
        ResultData = pd.read_csv(FilePath + ResultFileName)
        TestData = pd.read_csv(FilePath + TestFileName)
        for i in range(len(TestData)):
            self.assertAlmostEqual(ResultData.loc[i, "CommandResult"], TestData.loc[i, "CommandResult"])


def preProcess():
    V = Variables()
    AFP = Activities_ForestPath_(V)
    V.Status_AFP = AFP.SC_AFP_Start()
    # V.Status_AFP += AFP.UC_Task00_Select_Task()



# ..................................................... SECTION 2 ......................................................
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if __name__ == "__main__":
    preProcess()
    unittest.main()
