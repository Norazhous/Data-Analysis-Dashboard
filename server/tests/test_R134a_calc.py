import unittest
from unittest.mock import patch, MagicMock
import CoolProp

import sys
import os

# Add the parent directory of the current script to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you should be able to import modules
# from modules import R134aSimpleCycleCalculationPloting
from modules import globalVariables 
from modules.R134aSimpleCycleCalculationPloting import systemCalculation 


class systemCalculation(unittest.TestCase):

    @patch('modules.globalVariables')
    @patch('CoolProp.CoolProp.PropsSI')
    @patch('CoolProp.Plots.PropertyPlot')
    @patch('CoolProp.Plots.SimpleCompressionCycle')
    @patch('matplotlib.pyplot.savefig')
    def test_systemCalculation(self, mock_savefig, mock_cycle, mock_plot, mock_propssi, mock_globals):
        # Setup mock data
        mock_globals.Parameters_MeasuredData = {
            "T1": 15, "T2": 68, "T3": 43, "T4": 3.65, "T5": 2.82,
            "P1": 2.41, "P2": 10.18, "ASP": 1, "F": 4.43
        }
        mock_globals.Parameters_StudentCaculation = {
            "H1_Stu": 200, "H2_Stu": 250, "H3_Stu": 225, "H4_Stu": 150, "H5_Stu": 100,
            "m_Stu": 0.001, "QL_Stu": 1.0, "QH_Stu": 1.2, "W_Stu": 0.5, "COP_Stu": 2.0, "n_Stu": 4.0
        }
        
        mock_propssi.side_effect = [100000, 200000, 150000, 80000, 70000]

        # Call the function to be tested
        systemCalculation()

        # Assertions for updated global variables
        updated_params_sys = mock_globals.Parameters_SystemCaculation
        self.assertAlmostEqual(updated_params_sys["H1_Sys"], 410823.8061406922)
        self.assertAlmostEqual(updated_params_sys["H2_Sys"], 447981.3841019895)
        self.assertAlmostEqual(updated_params_sys["H3_Sys"], 260908.47213709648)
        self.assertAlmostEqual(updated_params_sys["H4_Sys"], 204923.6128030088)
        self.assertAlmostEqual(updated_params_sys["H5_Sys"], 203805.01604391987)
        self.assertAlmostEqual(updated_params_sys["m_Sys"], 0.0014151388888888887)
        self.assertAlmostEqual(updated_params_sys["QL_Sys"], 291.3773708218967)
        self.assertAlmostEqual(updated_params_sys["W_Sys"], 264.7341527792076)
        self.assertAlmostEqual(updated_params_sys["QH_Sys"], 52.58313358995252)
        self.assertAlmostEqual(updated_params_sys["COP_Sys"], 5.541270573451951)
        self.assertAlmostEqual(updated_params_sys["n_Sys"], 4.224066390041493)
        
        updated_params_dev = mock_globals.Parameters_DeviationCaculation
        self.assertIn("H1_Dev", updated_params_dev)
        self.assertIn("H2_Dev", updated_params_dev)
        self.assertIn("H3_Dev", updated_params_dev)
        self.assertIn("H4_Dev", updated_params_dev)
        self.assertIn("H5_Dev", updated_params_dev)
        self.assertIn("m_Dev", updated_params_dev)
        self.assertIn("QL_Dev", updated_params_dev)
        self.assertIn("QH_Dev", updated_params_dev)
        self.assertIn("W_Dev", updated_params_dev)
        self.assertIn("COP_Dev", updated_params_dev)
        self.assertIn("n_Dev", updated_params_dev)

        updated_params_sat = mock_globals.Parameters_SaturatedValue
        self.assertIn("SaturT_P1", updated_params_sat)
        self.assertIn("SaturT_P2", updated_params_sat)
        self.assertIn("SaturP_T3", updated_params_sat)
        self.assertIn("SaturP_T5", updated_params_sat)

        # Verify plot methods called
        mock_plot.assert_called()
        mock_cycle.assert_called()

if __name__ == '__main__':
    unittest.main()

