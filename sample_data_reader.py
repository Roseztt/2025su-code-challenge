import json

class SampleDataReader:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.data = json.load(f)
        self.index = 0
        if not isinstance(self.data, list):
            raise ValueError("Data must be a list in the JSON file.")

    def get(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            return None
