import json
import os

class DataReader:
    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data

    @staticmethod
    def get_test_data():
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'test_data.json')
        return DataReader.read_json(file_path)
