import unittest
import json
from unittest.mock import patch, MagicMock
from flask import Flask
from flask.testing import FlaskClient


import sys
import os

# Add the parent directory of the current script to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from enthalpy import saveDataFile,saveImgFile,enthalpy

class TestMain(unittest.TestCase):
    # def setUp(self):
    #     self.app = enthalpy.test_client()
    #     self.app.testing = True

    # @patch('enthalpy.R134aSimpleCycleCalculationPloting.systemCalculation')
    # @patch('enthalpy.imgEncode', return_value='encoded_image_data')
    # def test_get_enthalpy(self, mock_imgEncode, mock_systemCalculation):
    #     response = self.app.get('/enthalpy')
    #     data = json.loads(response.data)
        
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('Parameters_MeasuredData', data)
    #     self.assertIn('Parameters_StudentCaculation', data)
    #     self.assertIn('Parameters_SystemCaculation', data)
    #     self.assertIn('Parameters_DeviationCaculation', data)
    #     self.assertIn('Parameters_SaturatedValue', data)
    #     self.assertIn('img_data', data)
    #     self.assertEqual(data['img_data'], 'encoded_image_data')

    # @patch('enthalpy.R134aSimpleCycleCalculationPloting.systemCalculation')
    # def test_post_measured_data(self, mock_systemCalculation):
    #     post_data = {
    #         "dataType": "Measured",
    #         "MeasuredTime": "12:00",
    #         "T1": 14.49,
    #         "T2": 68.02,
    #         "T3": 43.1,
    #         "T4": 3.65,
    #         "T5": 2.82,
    #         "P1": 2.41,
    #         "P2": 10.18,
    #         "P3": 1.0,
    #         "E": 1.0,
    #         "F": 4.43,
    #         "ASP": 1011.6
    #     }
    #     response = self.app.post('/enthalpy', data=json.dumps(post_data), content_type='application/json')
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['status'], 'success')
    #     self.assertEqual(data['message'], 'Parameters_MeasuredData added!')
    #     mock_systemCalculation.assert_not_called()  # Assuming the calculation is not triggered

    # @patch('enthalpy.R134aSimpleCycleCalculationPloting.systemCalculation')
    # @patch('enthalpy.imgEncode', return_value='encoded_image_data')
    # def test_post_calculated_data(self, mock_imgEncode, mock_systemCalculation):
    #     post_data = {
    #         "dataType": "Calculation",
    #         "H1": 200,
    #         "H2": 250,
    #         "H3": 225,
    #         "H4": 150,
    #         "H5": 100,
    #         "m": 0.001,
    #         "QL": 1.0,
    #         "QH": 1.2,
    #         "W": 0.5,
    #         "COP": 2.0,
    #         "n": 4.0
    #     }
    #     response = self.app.post('/enthalpy', data=json.dumps(post_data), content_type='application/json')
    #     data = json.loads(response.data)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['status'], 'success')
    #     self.assertEqual(data['message'], 'Parameters_StudentCaculation added!')
    #     mock_systemCalculation.assert_not_called()  # Assuming the calculation is not triggered

    # @patch('enthalpy.saveDataFile')
    # @patch('enthalpy.saveImgFile')
    # @patch('enthalpy.imgEncode', return_value='encoded_image_data')
    # @patch('modules.R134aSimpleCycleCalculationPloting.systemCalculation')
    # def test_combined_measured_and_calculated_data(self, mock_systemCalculation, mock_imgEncode, mock_saveImgFile, mock_saveDataFile):
    #     # Post Measured Data
    #     post_measured_data = {
    #         "dataType": "Measured",
    #         "MeasuredTime": "12:00",
    #         "T1": 14.49,
    #         "T2": 68.02,
    #         "T3": 43.1,
    #         "T4": 3.65,
    #         "T5": 2.82,
    #         "P1": 2.41,
    #         "P2": 10.18,
    #         "P3": 1.0,
    #         "E": 1.0,
    #         "F": 4.43,
    #         "ASP": 1011.6
    #     }
    #     response = self.app.post('/enthalpy', data=json.dumps(post_measured_data), content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
        
    #     # Post Calculated Data
    #     post_calculated_data = {
    #         "dataType": "Calculation",
    #         "H1": 200,
    #         "H2": 250,
    #         "H3": 225,
    #         "H4": 150,
    #         "H5": 100,
    #         "m": 0.001,
    #         "QL": 1.0,
    #         "QH": 1.2,
    #         "W": 0.5,
    #         "COP": 2.0,
    #         "n": 4.0
    #     }
    #     response = self.app.post('/enthalpy', data=json.dumps(post_calculated_data), content_type='application/json')
    #     data = json.loads(response.data)
        
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['status'], 'success')
    #     self.assertEqual(data['message'], 'Parameters_StudentCaculation added!')
    #     mock_systemCalculation.assert_called_once()
    #     mock_imgEncode.assert_called_once()
    #     mock_saveImgFile.assert_called_once()
    #     mock_saveDataFile.assert_called_once()

if __name__ == '__main__':
    unittest.main()
