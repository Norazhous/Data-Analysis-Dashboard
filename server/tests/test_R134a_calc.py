import unittest
from unittest.mock import patch, MagicMock
import CoolProp

import sys
import os

# Add the parent directory of the current script to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you should be able to import modules
# from modules import R134aSimpleCycleCalculationPloting
from modules.R134aSimpleCycleCalculationPloting import systemCalculation,DeviationCalculation


class TestCalculation(unittest.TestCase):

    # @patch('CoolProp.CoolProp.PropsSI')
    # @patch('CoolProp.Plots.PropertyPlot')
    # @patch('CoolProp.Plots.SimpleCompressionCycle')
    # @patch('matplotlib.pyplot.savefig')
    def test_systemCalculation(self):
       
        Parameters_MeasuredData= {
                  "MeasuredTime": 30,
                  "T1": 15,
                  "T2": 68,
                  "T3": 43,
                  "T4": 3.65,
                  "T5": 2.82,
                  "P1": 2.41,
                  "P2": 10.18,
                  "P3": 10.5,
                  "E": 200,
                  "F": 4.43,
                  "ASP": 1,
                  "MeasuredDataStatus": 1
            }
        Parameters_SystemCaculation = {
                  "H1_Sys": 410823.8061406922,
                  "H2_Sys": 447981.3841019895,
                  "H3_Sys": 260908.47213709648,
                  "H4_Sys": 204923.6128030088,
                  "H5_Sys": 203805.01604391987,
                  "m_Sys": 0.0014151388888888887,
                  "QL_Sys": 291.3773708218967,
                  "QH_Sys": 264.7341527792076,
                  "W_Sys": 52.58313358995252,
                  "COP_Sys": 5.541270573451951,
                  "n_Sys": 4.224066390041493
            }
        Parameters_SaturatedValue ={
                  "SaturT_P1": 4.280896074225211,
                  "SaturT_P2": 43.58785669602315,
                  "SaturP_T3": 1100886.8247386036,
                  "SaturP_T5": 323932.30456048413
            }
        result = [Parameters_SystemCaculation,Parameters_SaturatedValue]

        self.assertEqual(systemCalculation(Parameters_MeasuredData),result)
        
        


    # test the deviationcalculation function 
    def test_DeviationCalculation(self):
        Parameters_StudentCaculation = {
                  "H1_Stu": 400,
                  "H2_Stu": 400,
                  "H3_Stu": 200,
                  "H4_Stu": 200,
                  "H5_Stu": 400,
                  "m_Stu": 0.01,
                  "QL_Stu": 60,
                  "QH_Stu": 50,
                  "W_Stu": 200,
                  "COP_Stu": 5,
                  "n_Stu": 5,
                  "CalculatedDataStatus": 1
            }
        Parameters_SystemCaculation = {
                  "H1_Sys": 410823.8061406922,
                  "H2_Sys": 447981.3841019895,
                  "H3_Sys": 260908.47213709648,
                  "H4_Sys": 204923.6128030088,
                  "H5_Sys": 203805.01604391987,
                  "m_Sys": 0.0014151388888888887,
                  "QL_Sys": 291.3773708218967,
                  "QH_Sys": 264.7341527792076,
                  "W_Sys": 52.58313358995252,
                  "COP_Sys": 5.541270573451951,
                  "n_Sys": 4.224066390041493,
                  "SystemDataStatus": 0
            }
        Parameters_DeviationCaculation = {
                  "H1_Dev": "3%",
                  "H2_Dev": "11%",
                  "H3_Dev": "23%",
                  "H4_Dev": "2%",
                  "H5_Dev": "96%",
                  "m_Dev": "607%",
                  "QL_Dev": "79%",
                  "QH_Dev": "81%",
                  "W_Dev": "280%",
                  "COP_Dev": "10%",
                  "n_Dev": "18%",
            }
        self.assertEqual(DeviationCalculation(Parameters_StudentCaculation,Parameters_SystemCaculation),Parameters_DeviationCaculation)

    #test the value of parameter is 0, the result from library will be error 


if __name__ == '__main__':
    unittest.main()

