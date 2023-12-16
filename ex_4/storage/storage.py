from ex_4.definitions import ROOT_DIR
from datetime import datetime
import json
import pathlib

class Storage():
    def __init__(self) -> None:
        self.storage_path = pathlib.Path(f"{ROOT_DIR}/storage/data.json")
        self.create_file()

    def create_file(self):
        if not self.storage_path.exists():
            with open(self.storage_path, 'x') as file:
                file.write(json.dumps({}))

    def read_data(self):
        if self.storage_path.exists():
            with open(self.storage_path, 'r') as file:
                return json.load(file)
        return {}

    def write_to_file(self, data):
        stored_data = self.read_data()
        print(stored_data)
        stored_data[datetime.now()] = data
        print(stored_data, json.dumps(stored_data))
        with open(self.storage_path, 'w') as file:
            file.write(json.dumps(stored_data))          
